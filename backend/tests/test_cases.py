"""
Tests pour les endpoints de cases (dossiers)
Tests adaptés à l'API réelle.
"""

import pytest
from fastapi import status


class TestListCases:
    """Tests pour lister les cases."""
    
    def test_list_cases_as_admin(self, client, admin_user, auth_headers):
        """Test liste des cases en tant qu'admin."""
        response = client.get("/api/v1/cases/", headers=auth_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "cases" in data
        assert isinstance(data["cases"], list)
    
    def test_list_cases_as_analyst(self, client, analyst_user, analyst_headers):
        """Test liste des cases en tant qu'analyst."""
        response = client.get("/api/v1/cases/", headers=analyst_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "cases" in data
    
    def test_list_cases_as_viewer(self, client, viewer_user, viewer_headers):
        """Test liste des cases en tant que viewer."""
        response = client.get("/api/v1/cases/", headers=viewer_headers)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "cases" in data
    
    def test_list_cases_without_auth(self, client):
        """Test liste des cases sans authentification."""
        response = client.get("/api/v1/cases/")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestCasePermissions:
    """Tests pour les permissions sur les cases."""
    
    def test_viewer_cannot_create_case(self, client, viewer_user, viewer_headers):
        """Test qu'un viewer ne peut pas créer de case."""
        case_data = {
            "case_number": "TEST-001",
            "importer_name": "Test Importer",
            "declarant_name": "Test Declarant"
        }
        
        response = client.post(
            "/api/v1/cases/",
            headers=viewer_headers,
            json=case_data
        )
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_create_case_without_auth(self, client):
        """Test création de case sans authentification."""
        case_data = {
            "case_number": "TEST-002",
            "importer_name": "Test Importer"
        }
        
        response = client.post("/api/v1/cases/", json=case_data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetCase:
    """Tests pour récupérer une case par ID."""
    
    def test_get_nonexistent_case(self, client, admin_user, auth_headers):
        """Test récupération d'une case inexistante."""
        response = client.get("/api/v1/cases/99999", headers=auth_headers)
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_get_case_without_auth(self, client):
        """Test récupération d'une case sans authentification."""
        response = client.get("/api/v1/cases/1")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

