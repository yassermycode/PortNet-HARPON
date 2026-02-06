"""
Script pour créer un utilisateur administrateur initial.
"""

from app.db.session import SessionLocal
from app.db.models.user import User
from app.core.security import get_password_hash

def create_admin():
    """Crée un utilisateur administrateur par défaut."""
    db = SessionLocal()
    
    try:
        # Vérifier si l'admin existe déjà
        existing_admin = db.query(User).filter(User.username == "admin").first()
        if existing_admin:
            print("❌ Un utilisateur 'admin' existe déjà")
            return
        
        # Créer l'admin
        admin = User(
            username="admin",
            email="admin@portnet.ma",
            hashed_password=get_password_hash("admin123"),
            full_name="Administrateur",
            role="ADMIN",
            is_active=True,
            is_superuser=True
        )
        
        db.add(admin)
        db.commit()
        
        print("✅ Utilisateur admin créé avec succès !")
        print("   Username: admin")
        print("   Password: admin123")
        print("   ⚠️  Changez ce mot de passe en production !")
        
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()
