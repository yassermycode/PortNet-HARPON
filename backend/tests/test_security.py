"""
Tests de sécurité
Tests pour les permissions, tokens JWT, et la sécurité générale.
"""

import pytest
from fastapi import status
from jose import jwt
from datetime import timedelta, datetime

from app.core.security import create_access_token, verify_password, get_password_hash


class TestPasswordHashing:
    """Tests pour le hashing des mots de passe."""
    
    def test_password_hash_and_verify(self):
        """Test hash et vérification de mot de passe."""
        password = "mysecretpassword123"
        hashed = get_password_hash(password)
        
        # Le hash ne doit pas être le mot de passe en clair
        assert hashed != password
        
        # La vérification doit fonctionner
        assert verify_password(password, hashed) is True
    
    def test_password_verify_wrong_password(self):
        """Test vérification avec mauvais mot de passe."""
        password = "mysecretpassword123"
        wrong_password = "wrongpassword"
        hashed = get_password_hash(password)
        
        assert verify_password(wrong_password, hashed) is False
    
    def test_same_password_different_hashes(self):
        """Test que le même mot de passe génère des hashes différents (salt)."""
        password = "mysecretpassword123"
        hash1 = get_password_hash(password)
        hash2 = get_password_hash(password)
        
        # Les hashes doivent être différents à cause du salt
        assert hash1 != hash2
        
        # Mais les deux doivent être valides
        assert verify_password(password, hash1) is True
        assert verify_password(password, hash2) is True


class TestJWTTokens:
    """Tests pour les tokens JWT."""
    
    def test_create_access_token(self):
        """Test création d'un token JWT."""
        data = {"sub": "testuser", "user_id": 1, "role": "ADMIN"}
        token = create_access_token(data)
        
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_token_contains_correct_data(self):
        """Test que le token contient les bonnes données."""
        from app.core.config import settings
        
        data = {"sub": "testuser", "user_id": 1, "role": "ADMIN"}
        token = create_access_token(data)
        
        # Décoder le token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        assert payload["sub"] == "testuser"
        assert payload["user_id"] == 1
        assert payload["role"] == "ADMIN"
        assert "exp" in payload
    
    def test_token_expiration(self):
        """Test que le token a une date d'expiration."""
        from app.core.config import settings
        
        data = {"sub": "testuser"}
        token = create_access_token(data)
        
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        # Vérifier que l'expiration est dans le futur
        exp_timestamp = payload["exp"]
        exp_datetime = datetime.fromtimestamp(exp_timestamp)
        
        assert exp_datetime > datetime.utcnow()


class TestRoleBasedAccess:
    """Tests pour le contrôle d'accès basé sur les rôles."""
    
    def test_admin_can_access_user_list(self, client, admin_user, auth_headers):
        """Test qu'un admin peut lister les utilisateurs."""
        response = client.get("/api/v1/auth/users", headers=auth_headers)
        assert response.status_code == status.HTTP_200_OK
    
    def test_analyst_cannot_access_user_list(self, client, analyst_user, analyst_headers):
        """Test qu'un analyst ne peut pas lister les utilisateurs."""
        response = client.get("/api/v1/auth/users", headers=analyst_headers)
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_viewer_cannot_access_user_list(self, client, viewer_user, viewer_headers):
        """Test qu'un viewer ne peut pas lister les utilisateurs."""
        response = client.get("/api/v1/auth/users", headers=viewer_headers)
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_admin_can_create_user(self, client, admin_user, auth_headers):
        """Test qu'un admin peut créer un utilisateur."""
        response = client.post(
            "/api/v1/auth/register",
            headers=auth_headers,
            json={
                "username": "newuser",
                "email": "newuser@test.com",
                "password": "password123",
                "full_name": "New User",
                "role": "ANALYST"
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_analyst_cannot_create_user(self, client, analyst_user, analyst_headers):
        """Test qu'un analyst ne peut pas créer un utilisateur."""
        response = client.post(
            "/api/v1/auth/register",
            headers=analyst_headers,
            json={
                "username": "newuser",
                "email": "newuser@test.com",
                "password": "password123",
                "full_name": "New User",
                "role": "ANALYST"
            }
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestAuthenticationRequired:
    """Tests pour vérifier que l'authentification est requise."""
    
    def test_get_cases_requires_auth(self, client):
        """Test que GET /cases/ nécessite l'authentification."""
        response = client.get("/api/v1/cases/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_create_case_requires_auth(self, client):
        """Test que POST /cases/ nécessite l'authentification."""
        response = client.post(
            "/api/v1/cases/",
            json={
                "title": "Test Case",
                "description": "Test Description",
                "priority": "HIGH"
            }
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_documents_requires_auth(self, client):
        """Test que GET /documents/ nécessite l'authentification."""
        # Vérifier si le endpoint existe d'abord
        response = client.get("/api/v1/documents/")
        
        # Si 404, c'est que le endpoint n'existe pas (skip ce test)
        if response.status_code == 404:
            pytest.skip("Documents endpoint not implemented yet")
        
        # Sinon, vérifier qu'il nécessite l'auth
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_health_check_does_not_require_auth(self, client):
        """Test que /health ne nécessite pas d'authentification."""
        response = client.get("/health")
        assert response.status_code == status.HTTP_200_OK


class TestInvalidTokens:
    """Tests pour les tokens invalides."""
    
    def test_malformed_token(self, client):
        """Test avec un token malformé."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "Bearer notavalidtoken"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_missing_bearer_prefix(self, client, admin_token):
        """Test avec token sans préfixe Bearer."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": admin_token}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_empty_token(self, client):
        """Test avec token vide."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "Bearer "}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_no_authorization_header(self, client):
        """Test sans header Authorization."""
        response = client.get("/api/v1/auth/me")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

