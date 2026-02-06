"""
Scoring Module
Combine les résultats des différents algorithmes pour calculer un score global.
"""

from typing import Dict, List
from enum import Enum


class RiskLevel(str, Enum):
    """Niveaux de risque."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class RecommendedAction(str, Enum):
    """Actions recommandées."""
    RELEASE = "RELEASE"
    INSPECT = "INSPECT"
    SEIZE = "SEIZE"


# Poids des algorithmes dans le score global
ALGORITHM_WEIGHTS = {
    'BENFORD_LAW': 0.25,
    'ISOLATION_FOREST': 0.35,
    'RULES_ENGINE': 0.40,
}


def calculate_global_score(algo_results: List[Dict]) -> float:
    """
    Calcule le score global pondéré à partir des résultats des algorithmes.
    
    Args:
        algo_results: Liste des résultats de chaque algorithme
        
    Returns:
        Score global entre 0 et 100
    """
    if not algo_results:
        return 0.0
    
    weighted_sum = 0.0
    total_weight = 0.0
    
    for result in algo_results:
        algo_source = result.get('algo_source')
        score = result.get('score', 0)
        
        if algo_source in ALGORITHM_WEIGHTS:
            weight = ALGORITHM_WEIGHTS[algo_source]
            weighted_sum += score * weight
            total_weight += weight
    
    if total_weight == 0:
        return 0.0
    
    # Score global pondéré
    global_score = weighted_sum / total_weight
    
    return round(global_score, 2)


def determine_risk_level(global_score: float) -> RiskLevel:
    """
    Détermine le niveau de risque basé sur le score global.
    
    Args:
        global_score: Score entre 0 et 100
        
    Returns:
        Niveau de risque
    """
    if global_score >= 75:
        return RiskLevel.CRITICAL
    elif global_score >= 50:
        return RiskLevel.HIGH
    elif global_score >= 25:
        return RiskLevel.MEDIUM
    else:
        return RiskLevel.LOW


def determine_recommended_action(global_score: float, risk_level: RiskLevel) -> RecommendedAction:
    """
    Détermine l'action recommandée basée sur le score et le niveau de risque.
    
    Args:
        global_score: Score entre 0 et 100
        risk_level: Niveau de risque
        
    Returns:
        Action recommandée
    """
    if risk_level == RiskLevel.CRITICAL:
        return RecommendedAction.SEIZE
    elif risk_level == RiskLevel.HIGH:
        return RecommendedAction.INSPECT
    elif risk_level == RiskLevel.MEDIUM:
        # Pour les cas moyens, on inspecte si le score est > 35
        if global_score > 35:
            return RecommendedAction.INSPECT
        else:
            return RecommendedAction.RELEASE
    else:
        return RecommendedAction.RELEASE


def calculate_case_scoring(algo_results: List[Dict]) -> Dict:
    """
    Calcule le scoring complet d'un case.
    
    Args:
        algo_results: Résultats de tous les algorithmes
        
    Returns:
        Dict avec score global, niveau de risque, et action recommandée
    """
    global_score = calculate_global_score(algo_results)
    risk_level = determine_risk_level(global_score)
    recommended_action = determine_recommended_action(global_score, risk_level)
    
    # Compter les anomalies détectées
    anomalies_count = sum(1 for r in algo_results if r.get('has_anomaly', False))
    
    return {
        'global_score': global_score,
        'risk_level': risk_level.value,
        'recommended_action': recommended_action.value,
        'anomalies_detected': anomalies_count,
        'algorithms_run': len(algo_results),
        'details': {
            result['algo_source']: {
                'score': result.get('score', 0),
                'has_anomaly': result.get('has_anomaly', False),
                'message': result.get('message', ''),
            }
            for result in algo_results
        }
    }


def get_scoring_summary(scoring_result: Dict) -> str:
    """
    Génère un résumé textuel du scoring.
    
    Args:
        scoring_result: Résultat du scoring
        
    Returns:
        Résumé textuel
    """
    score = scoring_result['global_score']
    risk = scoring_result['risk_level']
    action = scoring_result['recommended_action']
    anomalies = scoring_result['anomalies_detected']
    
    summary = f"Score global: {score}/100 | Risque: {risk} | Action: {action}"
    
    if anomalies > 0:
        summary += f" | {anomalies} anomalie(s) détectée(s)"
    
    return summary


# Test rapide
if __name__ == '__main__':
    # Simulation de résultats d'algorithmes
    
    # Cas 1: Risque faible
    results_low_risk = [
        {'algo_source': 'BENFORD_LAW', 'score': 0, 'has_anomaly': False, 'message': 'OK'},
        {'algo_source': 'ISOLATION_FOREST', 'score': 10, 'has_anomaly': False, 'message': 'OK'},
        {'algo_source': 'RULES_ENGINE', 'score': 0, 'has_anomaly': False, 'message': 'OK'},
    ]
    
    # Cas 2: Risque moyen
    results_medium_risk = [
        {'algo_source': 'BENFORD_LAW', 'score': 45, 'has_anomaly': True, 'message': 'Anomalie détectée'},
        {'algo_source': 'ISOLATION_FOREST', 'score': 30, 'has_anomaly': True, 'message': 'Outlier'},
        {'algo_source': 'RULES_ENGINE', 'score': 35, 'has_anomaly': True, 'message': '1 règle violée'},
    ]
    
    # Cas 3: Risque critique
    results_critical_risk = [
        {'algo_source': 'BENFORD_LAW', 'score': 85, 'has_anomaly': True, 'message': 'Anomalie majeure'},
        {'algo_source': 'ISOLATION_FOREST', 'score': 90, 'has_anomaly': True, 'message': 'Outlier majeur'},
        {'algo_source': 'RULES_ENGINE', 'score': 95, 'has_anomaly': True, 'message': '4 règles violées'},
    ]
    
    print("=== CAS 1: RISQUE FAIBLE ===")
    scoring1 = calculate_case_scoring(results_low_risk)
    print(get_scoring_summary(scoring1))
    print(f"Détails: {scoring1}\n")
    
    print("=== CAS 2: RISQUE MOYEN ===")
    scoring2 = calculate_case_scoring(results_medium_risk)
    print(get_scoring_summary(scoring2))
    print(f"Détails: {scoring2}\n")
    
    print("=== CAS 3: RISQUE CRITIQUE ===")
    scoring3 = calculate_case_scoring(results_critical_risk)
    print(get_scoring_summary(scoring3))
    print(f"Détails: {scoring3}\n")
