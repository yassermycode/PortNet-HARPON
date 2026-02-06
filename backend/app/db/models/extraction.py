from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, UniqueConstraint
from app.db.base_class import Base

class Extraction(Base):
    __tablename__ = "extractions"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False, unique=True)
    
    # Texte brut extrait du PDF
    raw_text = Column(Text, nullable=True)
    
    # Données structurées extraites (clé-valeur)
    key_value_json = Column(JSON, nullable=True)
    
    __table_args__ = (
        UniqueConstraint('document_id', name='uq_document_extraction'),
    )
