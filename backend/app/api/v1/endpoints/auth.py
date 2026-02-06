"""
Authentication Endpoints
Routes pour l'authentification et la gestion des utilisateurs.
"""

from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.db.models.user import User
from app.schemas.user import (
    UserCreate, UserResponse, UserUpdate, LoginRequest, Token
)
from app.core.security import (
    verify_password, get_password_hash, create_access_token
)
from app.api.dependencies.auth import get_current_user, get_current_admin
from app.core.rate_limit import limiter
from app.core.logging_config import log_security_event

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Enregistrer un nouveau utilisateur.
    
    Note : En production, cette route devrait être protégée (admin only).
    """
    # Vérifier si le username existe déjà
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ce nom d'utilisateur existe déjà"
        )
    
    # Vérifier si l'email existe déjà
    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cet email est déjà utilisé"
        )
    
    # Créer le nouvel utilisateur
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        full_name=user_data.full_name,
        role=user_data.role,
        is_active=True,
        is_superuser=False
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Log l'événement de création
    log_security_event(
        event_type="USER_CREATED",
        username=user_data.username,
        details=f"New user registered with role {user_data.role}",
        success=True
    )
    
    return new_user


@router.post("/login", response_model=Token)
@limiter.limit("5/minute")  # Max 5 tentatives par minute
async def login(
    request: Request,
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    Authentifier un utilisateur et retourner un token JWT.
    """
    # Rechercher l'utilisateur
    user = db.query(User).filter(User.username == login_data.username).first()
    
    if not user or not verify_password(login_data.password, user.hashed_password):
        # Log l'échec de connexion
        log_security_event(
            event_type="LOGIN",
            username=login_data.username,
            details="Invalid credentials",
            success=False
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Compte désactivé"
        )
    
    # Mettre à jour la date de dernière connexion
    user.last_login = datetime.utcnow()
    db.commit()
    
    # Log la connexion réussie
    log_security_event(
        event_type="LOGIN",
        username=user.username,
        details="User logged in successfully",
        success=True
    )
    
    # Créer le token
    # Note: "sub" (subject) doit être l'ID de l'utilisateur pour la compatibilité
    access_token = create_access_token(
        data={"sub": str(user.id), "username": user.username, "role": user.role}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """Récupère les informations de l'utilisateur actuellement connecté."""
    return current_user


@router.get("/users", response_model=list)
async def get_all_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Récupère la liste de tous les utilisateurs.
    
    Réservé aux administrateurs.
    """
    users = db.query(User).offset(skip).limit(limit).all()
    
    return [
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "full_name": u.full_name,
            "role": u.role,
            "is_active": u.is_active,
            "created_at": u.created_at,
            "last_login": u.last_login
        }
        for u in users
    ]


@router.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Met à jour un utilisateur.
    
    Réservé aux administrateurs.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    # Mettre à jour les champs fournis
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.full_name is not None:
        user.full_name = user_update.full_name
    if user_update.role is not None:
        user.role = user_update.role
    if user_update.is_active is not None:
        user.is_active = user_update.is_active
    if user_update.password is not None:
        user.hashed_password = get_password_hash(user_update.password)
    
    db.commit()
    db.refresh(user)
    
    return user


@router.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """
    Supprime un utilisateur.
    
    Réservé aux administrateurs.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    # Ne pas permettre de se supprimer soi-même
    if user.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Vous ne pouvez pas supprimer votre propre compte"
        )
    
    db.delete(user)
    db.commit()
    
    return {"success": True, "message": f"Utilisateur {user.username} supprimé"}
