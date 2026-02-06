"""
User Model
Modèle pour les utilisateurs de l'application.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from sqlalchemy.sql import func
from datetime import datetime

from app.db.base_class import Base


class User(Base):
    """Modèle pour les utilisateurs."""
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(String, nullable=False, default="ANALYST")  # ADMIN, ANALYST, VIEWER
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Nouveaux champs de profil professionnel
    first_name = Column(String, nullable=True)  # Prénom
    last_name = Column(String, nullable=True)   # Nom
    position = Column(String, nullable=True)    # Poste
    badge_number = Column(String, unique=True, nullable=True)  # N° d'immatriculation
    birth_date = Column(Date, nullable=True)    # Date de naissance
    phone = Column(String, nullable=True)       # Téléphone
    professional_email = Column(String, nullable=True)  # Email professionnel
    avatar_url = Column(String, nullable=True)  # Photo de profil
    department = Column(String, nullable=True)  # Service/Département
