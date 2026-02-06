"""Test simple de l'endpoint d'upload"""
import requests

url = "http://127.0.0.1:8001/api/v1/cases/1/documents"

print(f"🧪 Test de connexion à: {url}")

try:
    # Test OPTIONS (CORS preflight)
    response = requests.options(url)
    print(f"✅ OPTIONS réponse: {response.status_code}")
    print(f"Headers CORS: {response.headers.get('Access-Control-Allow-Origin', 'Non défini')}")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
