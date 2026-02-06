from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, Text, JSON
from sqlalchemy.sql import func
from app.db.base_class import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=True)
    file_size = Column(BigInteger, nullable=True)
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Statut de l'analyse
<<<<<<< HEAD
    status = Column(String, default="UPLOADED")  # UPLOADED, ANALYZING, ANALYZED, REJECTED, ERROR
    
    # Classification du document
    document_type = Column(String, nullable=True)  # Type de document détecté (FACTURE_COMMERCIALE, CONNAISSEMENT, etc.)
    classification_confidence = Column(Integer, nullable=True)  # Confiance 0-100
    
    # Résultats de l'analyse IA
    extracted_text = Column(Text, nullable=True)
    extracted_data = Column(JSON, nullable=True)
    risk_score = Column(Integer, nullable=True)
    risk_level = Column(String, nullable=True)  # FAIBLE, MOYEN, ÉLEVÉ
    risk_factors = Column(JSON, nullable=True)
    recommendation = Column(Text, nullable=True)
    
=======
    status = Column(String, default="UPLOADED")  # UPLOADED, ANALYZING, ANALYZED, ERROR
    
    # Résultats de l'analyse IA
    extracted_text = Column(Text, nullable=True)
    extracted_data = Column(JSON, nullable=True)
    risk_score = Column(Integer, nullable=True)
    risk_level = Column(String, nullable=True)  # FAIBLE, MOYEN, ÉLEVÉ
    risk_factors = Column(JSON, nullable=True)
    recommendation = Column(Text, nullable=True)
    
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    # Dates
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    analyzed_at = Column(DateTime(timezone=True), nullable=True)

