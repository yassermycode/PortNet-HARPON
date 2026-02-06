"""
Tests pour l'authentification
"""

import pytest
from fastapi import status


class TestLogin:
    """Tests pour le login."""
    
    def test_login_success(self, client, admin_user):
        """Test login avec credentials valides."""
        response = client.post(
            "/api/v1/auth/login",
            json={"username": "testadmin", "password": "testpassword"}
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    def test_login_invalid_username(self, client):
        """Test login avec username invalide."""
        response = client.post(
            "/api/v1/auth/login",
            json={"username": "wronguser", "password": "testpassword"}
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_login_invalid_password(self, client, admin_user):
        """Test login avec mot de passe invalide."""
        response = client.post(
            "/api/v1/auth/login",
            json={"username": "testadmin", "password": "wrongpassword"}
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_login_inactive_user(self, client, db, admin_user):
        """Test login avec utilisateur inactif."""
        admin_user.is_active = False
        db.commit()
        
        response = client.post(
            "/api/v1/auth/login",
            json={"username": "testadmin", "password": "testpassword"}
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestRegister:
    """Tests pour l'enregistrement."""
    
    def test_register_success(self, client, admin_user, auth_headers):
        """Test création d'utilisateur réussie."""
        response = client.post(
            "/api/v1/auth/register",
            headers=auth_headers,
            json={
                "username": "newuser",
                "email": "newuser@test.com",
                "password": "newpassword123",
                "full_name": "New User",
                "role": "ANALYST"
            }
        )
        
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["username"] == "newuser"
        assert data["email"] == "newuser@test.com"
        assert data["role"] == "ANALYST"
        assert "hashed_password" not in data
    
    def test_register_duplicate_username(self, client, admin_user, auth_headers):
        """Test création avec username déjà existant."""
        response = client.post(
            "/api/v1/auth/register",
            headers=auth_headers,
            json={
                "username": "testadmin",
                "email": "another@test.com",
                "password": "password123",
                "full_name": "Another User",
                "role": "ANALYST"
            }
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_register_duplicate_email(self, client, admin_user, auth_headers):
        """Test création avec email déjà existant."""
        response = client.post(
            "/api/v1/auth/register",
            headers=auth_headers,
            json={
                "username": "anotheruser",
                "email": "testadmin@test.com",
                "password": "password123",
                "full_name": "Another User",
                "role": "ANALYST"
            }
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_register_without_auth(self, client):
        """Test création sans authentification."""
        response = client.post(
            "/api/v1/auth/register",
            json={
                "username": "newuser",
                "email": "newuser@test.com",
                "password": "password123",
                "full_name": "New User",
                "role": "ANALYST"
            }
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetMe:
    """Tests pour récupérer les infos utilisateur."""
    
    def test_get_me_success(self, client, admin_user, auth_headers):
        """Test récupération infos utilisateur."""
        response = client.get("/api/v1/auth/me", headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["username"] == "testadmin"
        assert data["email"] == "testadmin@test.com"
        assert data["role"] == "ADMIN"
    
    def test_get_me_without_auth(self, client):
        """Test récupération sans authentification."""
        response = client.get("/api/v1/auth/me")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_get_me_invalid_token(self, client):
        """Test récupération avec token invalide."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "Bearer invalid_token"}
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetUsers:
    """Tests pour lister les utilisateurs."""
    
    def test_get_users_as_admin(self, client, admin_user, analyst_user, auth_headers):
        """Test liste utilisateurs en tant qu'admin."""
        response = client.get("/api/v1/auth/users", headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) >= 2
    
    def test_get_users_as_analyst(self, client, admin_user, analyst_user, analyst_headers):
        """Test liste utilisateurs en tant qu'analyst (devrait échouer)."""
        response = client.get("/api/v1/auth/users", headers=analyst_headers)
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_get_users_without_auth(self, client):
        """Test liste utilisateurs sans authentification."""
        response = client.get("/api/v1/auth/users")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

