"""
Configuration pytest
Fixtures et utilitaires pour les tests.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.base import Base
from app.db.session import get_db
from app.core.security import create_access_token, get_password_hash
from app.db.models.user import User


# Base de données de test en mémoire
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Fixture pour la base de données de test."""
    # Créer les tables
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Nettoyer après chaque test
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """Fixture pour le client de test FastAPI."""
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def admin_user(db):
    """Fixture pour créer un utilisateur admin."""
    user = User(
        username="testadmin",
        email="testadmin@test.com",
        full_name="Test Admin",
        hashed_password=get_password_hash("testpassword"),
        role="ADMIN",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture(scope="function")
def analyst_user(db):
    """Fixture pour créer un utilisateur analyst."""
    user = User(
        username="testanalyst",
        email="testanalyst@test.com",
        full_name="Test Analyst",
        hashed_password=get_password_hash("testpassword"),
        role="ANALYST",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture(scope="function")
def viewer_user(db):
    """Fixture pour créer un utilisateur viewer."""
    user = User(
        username="testviewer",
        email="testviewer@test.com",
        full_name="Test Viewer",
        hashed_password=get_password_hash("testpassword"),
        role="VIEWER",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture(scope="function")
def admin_token(admin_user):
    """Fixture pour générer un token admin."""
    return create_access_token(
        data={"sub": admin_user.username, "user_id": admin_user.id, "role": admin_user.role}
    )


@pytest.fixture(scope="function")
def analyst_token(analyst_user):
    """Fixture pour générer un token analyst."""
    return create_access_token(
        data={"sub": analyst_user.username, "user_id": analyst_user.id, "role": analyst_user.role}
    )


@pytest.fixture(scope="function")
def viewer_token(viewer_user):
    """Fixture pour générer un token viewer."""
    return create_access_token(
        data={"sub": viewer_user.username, "user_id": viewer_user.id, "role": viewer_user.role}
    )


@pytest.fixture(scope="function")
def auth_headers(admin_token):
    """Fixture pour les headers d'authentification admin."""
    return {"Authorization": f"Bearer {admin_token}"}


@pytest.fixture(scope="function")
def analyst_headers(analyst_token):
    """Fixture pour les headers d'authentification analyst."""
    return {"Authorization": f"Bearer {analyst_token}"}


@pytest.fixture(scope="function")
def viewer_headers(viewer_token):
    """Fixture pour les headers d'authentification viewer."""
    return {"Authorization": f"Bearer {viewer_token}"}
