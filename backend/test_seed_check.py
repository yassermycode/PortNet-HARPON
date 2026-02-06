from app.db.session import SessionLocal
from app.db.models.case import Case
from sqlalchemy import func, text

db = SessionLocal()

print("📊 Statistiques du seed :")
print(f"Cases : {db.query(Case).count()}")
print(f"Cases frauduleux (score > 70) : {db.query(Case).filter(Case.global_score > 70).count()}")
print(f"Cases normaux : {db.query(Case).filter(Case.global_score <= 70).count()}")

# Quelques exemples
frauds = db.query(Case).filter(Case.global_score > 70).limit(3).all()
print("\n🚨 Exemples de cases frauduleux :")
for c in frauds:
    print(f"  - {c.reference_id} : score={c.global_score}, risk={c.risk_level}")

db.close()