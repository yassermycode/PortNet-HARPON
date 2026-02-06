from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Dict, Any, List

class EntityInDB(BaseModel):
    id: int
    name: str
    normalized_name: str
    entity_type: str
    risk_score_history: Optional[List[Any]] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class CaseEntityLinkInDB(BaseModel):
    id: int
    case_id: int
    entity_id: int
    role: str
    linked_at: Optional[datetime] = None  # ✅ OPTIONNEL car peut être None en DB
    entity: Optional[EntityInDB] = None
    
    model_config = ConfigDict(from_attributes=True)
