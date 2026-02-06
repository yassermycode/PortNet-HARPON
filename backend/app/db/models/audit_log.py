from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, func
from app.db.base_class import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=True, index=True)
    actor = Column(String, nullable=True)
    event_type = Column(String, nullable=False, index=True)
    payload_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now(), index=True)

