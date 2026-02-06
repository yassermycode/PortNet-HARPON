from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.models.case import Case
from app.core.security import get_password_hash

def init_db(db: Session) -> None:
    """Initialize database with default data"""
    
    # Créer les utilisateurs par défaut
    admin_user = db.query(User).filter(User.username == "admin").first()
    if not admin_user:
        admin_user = User(
            username="admin",
            email="admin@portnet.ma",
            full_name="Administrateur",
            hashed_password=get_password_hash("admin123"),
            role="ADMIN",
            is_active=True
        )
        db.add(admin_user)
        db.commit()
        print("✅ Utilisateur admin créé")
    
    analyst_user = db.query(User).filter(User.username == "analyst").first()
    if not analyst_user:
        analyst_user = User(
            username="analyst",
            email="analyst@portnet.ma",
            full_name="Analyste",
            hashed_password=get_password_hash("analyst123"),
            role="ANALYST",
            is_active=True
        )
        db.add(analyst_user)
        db.commit()
        print("✅ Utilisateur analyst créé")
    
    viewer_user = db.query(User).filter(User.username == "viewer").first()
    if not viewer_user:
        viewer_user = User(
            username="viewer",
            email="viewer@portnet.ma",
            full_name="Viewer",
            hashed_password=get_password_hash("viewer123"),
            role="VIEWER",
            is_active=True
        )
        db.add(viewer_user)
        db.commit()
        print("✅ Utilisateur viewer créé")
    
    # Créer quelques dossiers de test
    test_case = db.query(Case).filter(Case.case_number == "CASE-2026-001").first()
    if not test_case:
        test_case = Case(
            case_number="CASE-2026-001",
            importer_name="ABC Import SARL",
            declarant_name="XYZ Customs Broker",
            transporter_name="Fast Logistics",
            priority="HIGH",
            status="OPEN",
            description="Conteneur suspect en provenance de Chine",
            risk_score=75,
            created_by=admin_user.id
        )
        db.add(test_case)
        db.commit()
        print("✅ Dossier de test créé")
