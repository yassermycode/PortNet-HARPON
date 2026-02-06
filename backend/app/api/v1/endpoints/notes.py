from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from app.db.session import get_db
from app.db.models.case import Case
from app.db.models.note import Note
from app.db.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

class NoteCreate(BaseModel):
    content: str
    document_id: Optional[int] = None

class NoteResponse(BaseModel):
    id: int
    case_id: int
    document_id: Optional[int]
    content: str
    created_by: int
    created_by_name: str
    created_at: datetime

    class Config:
        from_attributes = True

@router.post("/cases/{case_id}/notes")
async def create_note(
    case_id: int,
    note_data: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Créer une note pour un dossier"""
    print(f"📝 Création d'une note pour le dossier {case_id}")

    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")

    note = Note(
        case_id=case_id,
        document_id=note_data.document_id,
        content=note_data.content,
        created_by=current_user.id
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    print(f"✅ Note créée: ID={note.id}")

    return {
        "id": note.id,
        "case_id": note.case_id,
        "document_id": note.document_id,
        "content": note.content,
        "created_by": note.created_by,
        "created_by_name": current_user.full_name,
        "created_at": note.created_at,
    }


@router.get("/cases/{case_id}/notes")
async def get_case_notes(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer toutes les notes d'un dossier"""
    notes = db.query(Note, User).join(User, Note.created_by == User.id).filter(Note.case_id == case_id).order_by(Note.created_at.desc()).all()

    return {
        "case_id": case_id,
        "total": len(notes),
        "notes": [
            {
                "id": note.id,
                "case_id": note.case_id,
                "document_id": note.document_id,
                "content": note.content,
                "created_by": note.created_by,
                "created_by_name": user.full_name,
                "created_at": note.created_at,
            }
            for note, user in notes
        ]
    }


@router.delete("/notes/{note_id}")
async def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Supprimer une note"""
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note non trouvée")

    if note.created_by != current_user.id and current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Non autorisé")

    db.delete(note)
    db.commit()

    return {"message": "Note supprimée avec succès"}
