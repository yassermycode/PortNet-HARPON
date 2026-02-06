from sqlalchemy import Column, Integer, String, DateTime, JSON, func, UniqueConstraint
from app.db.base_class import Base

class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    normalized_name = Column(String, nullable=False, index=True)
    entity_type = Column(String, nullable=False)
    risk_score_history = Column(JSON, nullable=True, default=list)
    created_at = Column(DateTime, default=func.now())
    
    __table_args__ = (
        UniqueConstraint('entity_type', 'normalized_name', name='uq_entity_type_normalized_name'),
    )

