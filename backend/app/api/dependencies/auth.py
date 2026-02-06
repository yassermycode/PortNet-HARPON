"""
Authentication Dependencies
Dépendances pour vérifier l'authentification et les permissions.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional

from app.db.session import get_db
from app.db.models.user import User
from app.core.security import decode_access_token

# HTTPBearer scheme pour récupérer le token
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Récupère l'utilisateur actuellement authentifié.
    
    Vérifie le token JWT et retourne l'utilisateur correspondant.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Impossible de valider les credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Récupérer le token depuis les credentials
    token = credentials.credentials
    
    # Décoder le token
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    
    # Récupérer l'ID utilisateur depuis le token (sub contient l'ID maintenant)
    user_id_str: str = payload.get("sub")
    if user_id_str is None:
        raise credentials_exception
    
    # Convertir l'ID en entier
    try:
        user_id = int(user_id_str)
    except (ValueError, TypeError):
        raise credentials_exception
    
    # Récupérer l'utilisateur par ID
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Utilisateur inactif"
        )
    
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Vérifie que l'utilisateur est actif."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Utilisateur inactif")
    return current_user


def require_role(required_roles: list):
    """
    Dépendance pour vérifier le rôle de l'utilisateur.
    
    Usage:
        @router.get("/admin-only", dependencies=[Depends(require_role(["ADMIN"]))])
    """
    async def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Accès refusé. Rôles requis : {required_roles}"
            )
        return current_user
    
    return role_checker


async def get_current_admin(
    current_user: User = Depends(get_current_user)
) -> User:
    """Vérifie que l'utilisateur est un administrateur."""
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Accès réservé aux administrateurs"
        )
    return current_user
