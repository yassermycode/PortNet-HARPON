from fastapi import APIRouter
<<<<<<< HEAD
from app.api.v1.endpoints import cases, documents, analysis, auth, notes, users
=======
from app.api.v1.endpoints import cases, documents, analysis, auth, notes
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

api_router = APIRouter()

api_router.include_router(cases.router, prefix="/cases", tags=["cases"])
api_router.include_router(documents.router, tags=["documents"])  # Pas de prefix car les routes incluent déjà /cases
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
<<<<<<< HEAD
api_router.include_router(users.router, prefix="/users", tags=["users"])
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
api_router.include_router(notes.router, tags=["notes"])
