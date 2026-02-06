from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class FeatureInDB(BaseModel):
    id: int
    case_id: int
    feature_name: str
    feature_value: Optional[float] = None
    # PAS de computed_at pour l'instant (colonne n'existe pas en DB)
    
    model_config = ConfigDict(from_attributes=True)
