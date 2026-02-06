from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from app.db.base_class import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    
    # Nom de la feature (ex: "amount_total", "nb_items")
    feature_name = Column(String, nullable=False)
    
    # Valeur numérique de la feature
    feature_value = Column(Float, nullable=True)
    
    __table_args__ = (
        UniqueConstraint('case_id', 'feature_name', name='uq_case_feature'),
    )
