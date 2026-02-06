from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.base_class import Base

class DocumentSimilarity(Base):
    __tablename__ = "document_similarities"

    id = Column(Integer, primary_key=True, index=True)
    
    # Premier document
    doc_id_1 = Column(Integer, ForeignKey("documents.id"), nullable=False)
    
    # Second document
    doc_id_2 = Column(Integer, ForeignKey("documents.id"), nullable=False)
    
    # Score de similarité (0.0 à 1.0)
    similarity_score = Column(Float, nullable=False)
    
    # Méthode utilisée (cosine, jaccard, etc.)
    method = Column(String, nullable=True)
