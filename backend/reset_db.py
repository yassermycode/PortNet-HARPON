from app.db.session import engine
from app.db.base import Base
from app.db.session import SessionLocal
from app.db.init_db import init_db

print("🗑️  Suppression des tables existantes...")
Base.metadata.drop_all(bind=engine)

print("🔨 Création des nouvelles tables...")
Base.metadata.create_all(bind=engine)

print("📊 Initialisation des données...")
db = SessionLocal()
try:
    init_db(db)
    print("✅ Base de données réinitialisée avec succès !")
finally:
    db.close()
