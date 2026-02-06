"""
Batch Analysis Module
Analyse tous les cases avec les 3 algorithmes et enregistre les résultats.
"""

from sqlalchemy.orm import Session
from typing import List, Dict
import logging

from app.db.models.case import Case
from app.db.models.signal import Signal
from app.db.models.feature import Feature
from app.analysis.benford import analyze_case_benford
from app.analysis.isolation_forest import analyze_case_isolation_forest, train_isolation_forest
from app.analysis.rules_engine import RulesEngine
from app.analysis.scoring import calculate_case_scoring

logger = logging.getLogger(__name__)


def get_case_features(db: Session, case_id: int) -> List[Dict]:
    """Récupère les features d'un case."""
    features = db.query(Feature).filter(Feature.case_id == case_id).all()
    return [
        {
            'feature_name': f.feature_name,
            'feature_value': f.feature_value,
        }
        for f in features
    ]


def get_case_data(db: Session, case_id: int) -> Dict:
    """Récupère les données complètes d'un case."""
    case = db.query(Case).filter(Case.id == case_id).first()
    
    if not case:
        return {}
    
    # Charger les entity_links
    entity_links = [link.entity_id for link in case.entity_links]
    
    return {
        'id': case.id,
        'reference_id': case.reference_id,
        'entity_links': entity_links,
    }


def create_signal(
    db: Session,
    case_id: int,
    algo_source: str,
    signal_type: str,
    severity: str,
    score_contribution: float,
    evidence_json: Dict,
) -> Signal:
    """Crée un signal dans la DB."""
    signal = Signal(
        case_id=case_id,
        algo_source=algo_source,
        signal_type=signal_type,
        severity=severity,
        score_contribution=score_contribution,
        evidence_json=evidence_json,
    )
    db.add(signal)
    return signal


def analyze_single_case(
    db: Session,
    case_id: int,
    rules_engine: RulesEngine,
    isolation_model=None,
    isolation_scaler=None,
    isolation_features=None,
) -> Dict:
    """
    Analyse un seul case avec tous les algorithmes.
    
    Returns:
        Résultat du scoring complet
    """
    # Récupérer les données
    case_data = get_case_data(db, case_id)
    features = get_case_features(db, case_id)
    
    if not case_data or not features:
        logger.warning(f"Case {case_id}: pas de données disponibles")
        return None
    
    # Liste des résultats d'algorithmes
    algo_results = []
    
    # 1. Benford's Law
    try:
        benford_result = analyze_case_benford(case_id, features)
        algo_results.append(benford_result)
        
        # Créer un signal si anomalie
        if benford_result.get('has_anomaly'):
            create_signal(
                db=db,
                case_id=case_id,
                algo_source='BENFORD_LAW',
                signal_type='STATISTICAL_ANOMALY',
                severity='MEDIUM' if benford_result['score'] < 70 else 'HIGH',
                score_contribution=benford_result['score'],
                evidence_json=benford_result,
            )
    except Exception as e:
        logger.error(f"Erreur Benford pour case {case_id}: {e}")
    
    # 2. Isolation Forest
    try:
        isolation_result = analyze_case_isolation_forest(
            case_id, features, isolation_model, isolation_scaler, isolation_features
        )
        algo_results.append(isolation_result)
        
        if isolation_result.get('has_anomaly'):
            create_signal(
                db=db,
                case_id=case_id,
                algo_source='ISOLATION_FOREST',
                signal_type='OUTLIER_DETECTION',
                severity='MEDIUM' if isolation_result['score'] < 70 else 'HIGH',
                score_contribution=isolation_result['score'],
                evidence_json=isolation_result,
            )
    except Exception as e:
        logger.error(f"Erreur Isolation Forest pour case {case_id}: {e}")
    
    # 3. Rules Engine
    try:
        rules_result = rules_engine.analyze_case(case_id, case_data, features)
        algo_results.append(rules_result)
        
        if rules_result.get('has_anomaly'):
            # Créer un signal pour chaque violation
            for violation in rules_result.get('violations', []):
                create_signal(
                    db=db,
                    case_id=case_id,
                    algo_source='RULES_ENGINE',
                    signal_type='RULE_VIOLATION',
                    severity=violation['severity'],
                    score_contribution=violation['score'],
                    evidence_json=violation,
                )
    except Exception as e:
        logger.error(f"Erreur Rules Engine pour case {case_id}: {e}")
    
    # Calculer le scoring global
    scoring_result = calculate_case_scoring(algo_results)
    
    # Mettre à jour le case
    case = db.query(Case).filter(Case.id == case_id).first()
    if case:
        case.global_score = scoring_result['global_score']
        case.risk_level = scoring_result['risk_level']
        case.recommended_action = scoring_result['recommended_action']
        
        # Déterminer le statut
        if scoring_result['anomalies_detected'] > 0:
            case.status = 'FLAGGED'
        else:
            case.status = 'CLEAN'
    
    return scoring_result


def batch_analyze_all_cases(db: Session) -> Dict:
    """
    Analyse tous les cases de la base de données.
    
    Returns:
        Statistiques de l'analyse
    """
    logger.info("Début de l'analyse batch de tous les cases")
    
    # Récupérer tous les cases
    cases = db.query(Case).all()
    case_ids = [c.id for c in cases]
    
    logger.info(f"Nombre de cases à analyser: {len(case_ids)}")
    
    if not case_ids:
        return {
            'total_cases': 0,
            'cases_analyzed': 0,
            'cases_flagged': 0,
            'cases_clean': 0,
        }
    
    # Initialiser le rules engine
    rules_engine = RulesEngine()
    
    # Préparer l'Isolation Forest (entraîner sur tous les cases)
    logger.info("Entraînement du modèle Isolation Forest...")
    all_features = [get_case_features(db, cid) for cid in case_ids]
    isolation_model, isolation_scaler, isolation_feature_names = train_isolation_forest(
        all_features, contamination=0.1
    )
    
    # Supprimer les anciens signaux
    logger.info("Suppression des anciens signaux...")
    db.query(Signal).delete()
    db.commit()
    
    # Analyser chaque case
    stats = {
        'total_cases': len(case_ids),
        'cases_analyzed': 0,
        'cases_flagged': 0,
        'cases_clean': 0,
        'errors': 0,
    }
    
    for case_id in case_ids:
        try:
            result = analyze_single_case(
                db, case_id, rules_engine,
                isolation_model, isolation_scaler, isolation_feature_names
            )
            
            if result:
                stats['cases_analyzed'] += 1
                
                case = db.query(Case).filter(Case.id == case_id).first()
                if case and case.status == 'FLAGGED':
                    stats['cases_flagged'] += 1
                elif case and case.status == 'CLEAN':
                    stats['cases_clean'] += 1
            
            # Commit après chaque case
            db.commit()
            
            if stats['cases_analyzed'] % 10 == 0:
                logger.info(f"Progression: {stats['cases_analyzed']}/{len(case_ids)} cases analysés")
        
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse du case {case_id}: {e}")
            stats['errors'] += 1
            db.rollback()
    
    logger.info(f"Analyse batch terminée: {stats}")
    
    return stats


# Script de test
if __name__ == '__main__':
    from app.db.session import SessionLocal
    
    logging.basicConfig(level=logging.INFO)
    
    db = SessionLocal()
    
    try:
        stats = batch_analyze_all_cases(db)
        
        print("\n" + "="*60)
        print("RÉSULTATS DE L'ANALYSE BATCH")
        print("="*60)
        print(f"Total de cases:       {stats['total_cases']}")
        print(f"Cases analysés:       {stats['cases_analyzed']}")
        print(f"Cases signalés:       {stats['cases_flagged']}")
        print(f"Cases propres:        {stats['cases_clean']}")
        print(f"Erreurs:              {stats['errors']}")
        print("="*60)
        
    finally:
        db.close()
