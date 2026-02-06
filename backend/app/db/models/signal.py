"""
Signal Model
Représente un signal de fraude détecté par un algorithme.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, JSON
from datetime import datetime

from app.db.base_class import Base


class Signal(Base):
    """Modèle pour les signaux de fraude."""
    
    __tablename__ = "signals"
    
    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False, index=True)
    algo_source = Column(String, nullable=False, index=True)
    signal_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    score_contribution = Column(Float, nullable=True)
    evidence_json = Column(JSON, nullable=True)
    detected_at = Column(DateTime, default=datetime.utcnow)
