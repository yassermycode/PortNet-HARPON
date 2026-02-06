from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

# Import uniquement pour le type checking (évite imports circulaires)
if TYPE_CHECKING:
    from app.schemas.signal import SignalInDB
    from app.schemas.feature import FeatureInDB
    from app.schemas.entity import CaseEntityLinkInDB
    from app.schemas.document import DocumentInDB

class CaseBase(BaseModel):
    reference_id: str

class CaseCreate(CaseBase):
    pass

class CaseInDB(CaseBase):
    id: int
    status: str
    global_score: int
    risk_level: Optional[str] = None
    recommended_action: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class CaseListItem(BaseModel):
    """Schema pour la liste des cases (version allégée)"""
    id: int
    reference_id: str
    status: str
    global_score: int
    risk_level: Optional[str] = None
    recommended_action: Optional[str] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class CaseDetail(CaseInDB):
    """Schema pour le détail complet d'un case (avec relations)"""
    signals: List["SignalInDB"] = []
    features: List["FeatureInDB"] = []
    entity_links: List["CaseEntityLinkInDB"] = []
    documents: List["DocumentInDB"] = []

# Force la résolution des forward references pour FastAPI
from app.schemas.signal import SignalInDB
from app.schemas.feature import FeatureInDB
from app.schemas.entity import CaseEntityLinkInDB
from app.schemas.document import DocumentInDB

CaseDetail.model_rebuild()

