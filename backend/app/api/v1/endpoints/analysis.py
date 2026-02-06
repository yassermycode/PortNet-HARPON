"""
Analysis Endpoints
Routes pour l'analyse des cases avec les algorithmes de détection.
"""

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import Dict

from app.db.session import get_db
from app.db.models.case import Case
from app.analysis.batch_analyze import analyze_single_case, batch_analyze_all_cases
from app.analysis.rules_engine import RulesEngine
from app.api.dependencies.auth import get_current_user
from app.db.models.user import User

router = APIRouter()


@router.post("/cases/{case_id}/analyze", response_model=Dict)
async def analyze_case(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Analyse un case spécifique avec tous les algorithmes.
    
    Exécute :
    - Benford's Law
    - Isolation Forest
    - Rules Engine
    - Calcul du score global
    
    Retourne le résultat complet de l'analyse.
    """
    # Vérifier que le case existe
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case {case_id} non trouve")
    
    # Initialiser le rules engine
    rules_engine = RulesEngine()
    
    # Analyser le case
    try:
        scoring_result = analyze_single_case(
            db=db,
            case_id=case_id,
            rules_engine=rules_engine,
        )
        
        if not scoring_result:
            raise HTTPException(
                status_code=500,
                detail="Erreur lors de l'analyse du case"
            )
        
        # Récupérer le case mis à jour
        db.refresh(case)
        
        return {
            "success": True,
            "case_id": case_id,
            "reference_id": case.reference_id,
            "status": case.status,
            "global_score": case.global_score,
            "risk_level": case.risk_level,
            "recommended_action": case.recommended_action,
            "analysis_details": scoring_result,
            "message": f"Case {case_id} analyse avec succes"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de l'analyse: {str(e)}"
        )


@router.post("/batch/analyze/sync", response_model=Dict)
async def analyze_all_cases_sync(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Lance l'analyse de tous les cases de manière synchrone.
    
    Cette opération peut prendre du temps selon le nombre de cases.
    """
    try:
        stats = batch_analyze_all_cases(db)
        
        return {
            "success": True,
            "message": "Analyse batch terminee",
            "statistics": stats
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de l'analyse batch: {str(e)}"
        )


@router.get("/cases/{case_id}/signals")
async def get_case_signals(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Récupère tous les signaux détectés pour un case.
    """
    from app.db.models.signal import Signal
    
    # Vérifier que le case existe
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case {case_id} non trouve")
    
    # Récupérer les signaux
    signals = db.query(Signal).filter(Signal.case_id == case_id).all()
    
    return {
        "case_id": case_id,
        "reference_id": case.reference_id,
        "total_signals": len(signals),
        "signals": [
            {
                "id": s.id,
                "algo_source": s.algo_source,
                "signal_type": s.signal_type,
                "severity": s.severity,
                "score_contribution": s.score_contribution,
                "evidence": s.evidence_json,
                "detected_at": s.detected_at.isoformat() if s.detected_at else None,
            }
            for s in signals
        ]
    }

@router.get("/stats/algorithms")
async def get_algorithm_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Statistiques sur les performances des algorithmes.
    
    Retourne :
    - Nombre de signaux par algorithme
    - Score moyen de contribution par algorithme
    - Répartition par sévérité
    """
    from sqlalchemy import func
    from app.db.models.signal import Signal
    
    # Total de signaux par algorithme
    signals_by_algo = db.query(
        Signal.algo_source,
        func.count(Signal.id).label('count')
    ).group_by(Signal.algo_source).all()
    
    # Score moyen de contribution par algorithme
    avg_contribution_by_algo = db.query(
        Signal.algo_source,
        func.avg(Signal.score_contribution).label('avg_contribution')
    ).group_by(Signal.algo_source).all()
    
    # Répartition par sévérité
    severity_distribution = db.query(
        Signal.severity,
        func.count(Signal.id).label('count')
    ).group_by(Signal.severity).all()
    
    # Signal par type
    signal_type_distribution = db.query(
        Signal.signal_type,
        func.count(Signal.id).label('count')
    ).group_by(Signal.signal_type).all()
    
    return {
        "total_signals": db.query(Signal).count(),
        "signals_by_algorithm": {
            algo: count for algo, count in signals_by_algo
        },
        "average_contribution_by_algorithm": {
            algo: round(float(avg), 2) for algo, avg in avg_contribution_by_algo if avg is not None
        },
        "severity_distribution": {
            severity: count for severity, count in severity_distribution
        },
        "signal_type_distribution": {
            sig_type: count for sig_type, count in signal_type_distribution
        }
    }
