from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=True  # Affiche les requêtes SQL (utile en dev)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency pour FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
