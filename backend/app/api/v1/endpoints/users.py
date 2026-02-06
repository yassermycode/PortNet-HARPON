"""
Users Endpoints
Routes pour la gestion des profils utilisateurs.
"""

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from datetime import date
from typing import Optional
import os
import shutil
import uuid
from pydantic import BaseModel

from app.db.session import get_db
from app.db.models.user import User
from app.api.dependencies.auth import get_current_user

router = APIRouter()


class UserProfileUpdate(BaseModel):
    """Modèle pour la mise à jour du profil utilisateur."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None
    badge_number: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    professional_email: Optional[str] = None
    department: Optional[str] = None


class UserProfileResponse(BaseModel):
    """Modèle de réponse du profil utilisateur."""
    id: int
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    position: Optional[str]
    badge_number: Optional[str]
    birth_date: Optional[date]
    phone: Optional[str]
    professional_email: Optional[str]
    department: Optional[str]
    role: str
    avatar_url: Optional[str]
    created_at: str
    last_login: Optional[str]

    class Config:
        from_attributes = True


@router.get("/me", response_model=UserProfileResponse)
async def get_my_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Récupérer le profil de l'utilisateur connecté
    """
    print(f"\n👤 Récupération du profil : {current_user.username}")
    
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "full_name": current_user.full_name,
        "position": current_user.position,
        "badge_number": current_user.badge_number,
        "birth_date": current_user.birth_date,
        "phone": current_user.phone,
        "professional_email": current_user.professional_email,
        "department": current_user.department,
        "role": current_user.role,
        "avatar_url": current_user.avatar_url,
        "created_at": current_user.created_at.isoformat() if current_user.created_at else None,
        "last_login": current_user.last_login.isoformat() if current_user.last_login else None
    }


@router.put("/me", response_model=UserProfileResponse)
async def update_my_profile(
    profile_data: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Mettre à jour le profil de l'utilisateur connecté
    """
    print(f"\n✏️ Mise à jour du profil : {current_user.username}")
    
    # Mettre à jour les champs fournis
    update_data = profile_data.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        if hasattr(current_user, field):
            setattr(current_user, field, value)
    
    # Mettre à jour full_name si prénom/nom changés
    if profile_data.first_name or profile_data.last_name:
        first = profile_data.first_name or (current_user.first_name or "")
        last = profile_data.last_name or (current_user.last_name or "")
        current_user.full_name = f"{first} {last}".strip()
    
    db.commit()
    db.refresh(current_user)
    
    print(f"✅ Profil mis à jour avec succès")
    
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "full_name": current_user.full_name,
        "position": current_user.position,
        "badge_number": current_user.badge_number,
        "birth_date": current_user.birth_date,
        "phone": current_user.phone,
        "professional_email": current_user.professional_email,
        "department": current_user.department,
        "role": current_user.role,
        "avatar_url": current_user.avatar_url,
        "created_at": current_user.created_at.isoformat() if current_user.created_at else None,
        "last_login": current_user.last_login.isoformat() if current_user.last_login else None
    }


@router.post("/me/avatar")
async def upload_avatar(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Télécharger une photo de profil
    """
    print(f"\n📸 Téléchargement d'avatar pour : {current_user.username}")
    
    # Vérifier le type de fichier
    allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Type de fichier non autorisé. Types acceptés: {', '.join(allowed_types)}"
        )
    
    # Vérifier la taille (max 5MB)
    max_size = 5 * 1024 * 1024  # 5MB
    content = await file.read()
    if len(content) > max_size:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Fichier trop volumineux. Taille max: 5MB"
        )
    
    # Créer le dossier s'il n'existe pas
    avatar_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "uploads", "avatars")
    os.makedirs(avatar_dir, exist_ok=True)
    
    # Générer un nom de fichier unique
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(avatar_dir, unique_filename)
    
    # Sauvegarder le fichier
    with open(file_path, "wb") as buffer:
        buffer.write(content)
    
    # Supprimer l'ancien avatar si existant
    if current_user.avatar_url:
        try:
            old_path = os.path.join(avatar_dir, os.path.basename(current_user.avatar_url))
            if os.path.exists(old_path):
                os.remove(old_path)
        except Exception as e:
            print(f"⚠️ Impossible de supprimer l'ancien avatar: {e}")
    
    # Mettre à jour l'URL de l'avatar dans la base de données
    current_user.avatar_url = f"/uploads/avatars/{unique_filename}"
    db.commit()
    db.refresh(current_user)
    
    print(f"✅ Avatar uploadé avec succès: {current_user.avatar_url}")
    
    return {
        "message": "Avatar uploadé avec succès",
        "avatar_url": current_user.avatar_url
    }


