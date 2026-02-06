from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Dict, Any

class SignalInDB(BaseModel):
    id: int
    case_id: int
    algo_source: str
    signal_type: str
    severity: str
    score_contribution: Optional[int] = None
    evidence_json: Optional[Dict[str, Any]] = None
    detected_at: Optional[datetime] = None  # ✅ OPTIONNEL car peut être None
    
    model_config = ConfigDict(from_attributes=True)