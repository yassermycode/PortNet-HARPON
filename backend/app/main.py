from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from fastapi.staticfiles import StaticFiles
from app.api.v1.api import api_router
from app.db.session import get_db, engine
from app.db.base import Base
import os
=======
from app.api.v1.api import api_router
from app.db.session import get_db, engine
from app.db.base import Base
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

app = FastAPI(
    title="PortNet HARPON",
    version="1.0.0",
    openapi_tags=[
        {"name": "auth", "description": "Authentication operations"},
        {"name": "cases", "description": "Case management"},
        {"name": "documents", "description": "Document management"},
        {"name": "analysis", "description": "Analysis operations"},
    ]
)

# Configuration CORS - DOIT ÊTRE AVANT LES ROUTES
<<<<<<< HEAD
# Mode permissif pour le développement
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet toutes les origines en dev
=======
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

<<<<<<< HEAD
# Servir les fichiers statiques (uploads)
uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(uploads_dir, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=uploads_dir), name="uploads")

=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
# Routes de base
@app.get("/")
async def root():
    return {"message": "PortNet HARPON API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Créer les tables au démarrage
@app.on_event("startup")
async def startup():
    print("🚀 Démarrage de l'application...")
<<<<<<< HEAD
    print("✅ API prête sur http://127.0.0.1:8001")
    print("📚 Documentation sur http://127.0.0.1:8001/docs")
    print("📁 Dossier uploads:", os.path.abspath("uploads"))
=======
    print("✅ API prête sur http://127.0.0.1:8000")
    print("📚 Documentation sur http://127.0.0.1:8000/docs")
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
