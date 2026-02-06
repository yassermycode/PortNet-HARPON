"""
User Schemas
Schémas de validation pour les utilisateurs.
"""

from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """Schéma de base pour un utilisateur."""
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    role: str = "ANALYST"
    
    @validator('role')
    def validate_role(cls, v):
        valid_roles = ["ADMIN", "ANALYST", "VIEWER"]
        if v not in valid_roles:
            raise ValueError(f"Role invalide. Valeurs acceptées : {valid_roles}")
        return v


class UserCreate(UserBase):
    """Schéma pour créer un utilisateur."""
    password: str
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError("Le mot de passe doit contenir au moins 6 caractères")
        return v


class UserUpdate(BaseModel):
    """Schéma pour mettre à jour un utilisateur."""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None


class UserInDB(UserBase):
    """Schéma pour un utilisateur en base de données."""
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserResponse(UserBase):
    """Schéma de réponse pour un utilisateur (sans infos sensibles)."""
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schéma pour un token JWT."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Données contenues dans un token."""
    username: Optional[str] = None
    user_id: Optional[int] = None
    role: Optional[str] = None


class LoginRequest(BaseModel):
    """Schéma pour une requête de login."""
    username: str
    password: str
