from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from pydantic import ValidationError

<<<<<<< HEAD
from app.config import settings
=======
from app.core.config import settings
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
from app.db.session import SessionLocal
from app.db.models.user import User
from app.core.security import ALGORITHM

# OAuth2 scheme pour extraire le token du header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")


def get_db() -> Generator:
    """Dépendance pour obtenir une session de base de données"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    Dépendance pour obtenir l'utilisateur connecté à partir du token JWT
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Décoder le token JWT
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[ALGORITHM]
        )
        
<<<<<<< HEAD
        user_id_str = payload.get("sub")
        
        if user_id_str is None:
            raise credentials_exception
        
        # Convertir en entier (le token peut contenir une chaîne)
        try:
            user_id: int = int(user_id_str)
        except (ValueError, TypeError):
=======
        user_id: int = payload.get("sub")
        
        if user_id is None:
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            raise credentials_exception
            
    except (JWTError, ValidationError):
        raise credentials_exception
    
    # Récupérer l'utilisateur depuis la base de données
    user = db.query(User).filter(User.id == user_id).first()
    
    if user is None:
        raise credentials_exception
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    return user


def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
 ) -> User:
    """
    Dépendance pour vérifier que l'utilisateur est un admin
    """
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    return current_user
