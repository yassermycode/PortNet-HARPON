from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.db.base_class import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    case_number = Column(String, unique=True, index=True, nullable=False)
    importer_name = Column(String, nullable=False)
    declarant_name = Column(String, nullable=True)
    transporter_name = Column(String, nullable=True)
    priority = Column(String, default="MEDIUM")
    status = Column(String, default="OPEN")
    description = Column(Text, nullable=True)
    
    # Score de risque global (basé sur les documents analysés)
    risk_score = Column(Integer, default=0)
    risk_level = Column(String, default="FAIBLE")  # FAIBLE, MOYEN, ÉLEVÉ
    
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())