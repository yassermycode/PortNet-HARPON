"""
Script pour créer la table users.
"""

from app.db.session import engine
from app.db.base import Base
from app.db.models.user import User

def create_user_table():
    """Crée la table users."""
    print("Création de la table users...")
    Base.metadata.create_all(bind=engine, tables=[User.__table__])
    print("Table users créée avec succès !")

if __name__ == "__main__":
    create_user_table()
