from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class DocumentBase(BaseModel):
    filename: str
    doc_type: Optional[str] = None

class DocumentCreate(DocumentBase):
    pass

class DocumentInDB(DocumentBase):
    id: int
    case_id: int
    storage_path: str
    file_hash: Optional[str] = None
    mime_type: Optional[str] = None
    size_bytes: int
    page_count: Optional[int] = None
    uploaded_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
