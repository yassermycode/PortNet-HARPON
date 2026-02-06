from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.db.base_class import Base

class CaseEntityLink(Base):
    __tablename__ = "case_entity_links"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    entity_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    role = Column(String, nullable=True)
    linked_at = Column(DateTime, default=func.now())
