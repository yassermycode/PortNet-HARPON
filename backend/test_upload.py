"""Script de test pour vérifier l'endpoint d'upload"""
import requests
import os

# Configuration
BACKEND_URL = "http://127.0.0.1:8001"
CASE_ID = 1  # Utilisez un ID de case existant

# Token d'authentification (remplacez par un vrai token)
# Pour obtenir un token, utilisez l'endpoint /api/v1/auth/login
TOKEN = "votre_token_ici"

def test_upload():
    """Test l'upload d'un document"""
    
    # Créer un fichier PDF de test
    test_file_path = "test_document.pdf"
    if not os.path.exists(test_file_path):
        with open(test_file_path, "wb") as f:
            f.write(b"%PDF-1.4\nTest PDF file\n%%EOF")
        print(f"✅ Fichier de test créé: {test_file_path}")
    
    # URL de l'endpoint
    url = f"{BACKEND_URL}/api/v1/cases/{CASE_ID}/documents"
    
    print(f"\n{'='*60}")
    print(f"📤 TEST D'UPLOAD")
    print(f"{'='*60}")
    print(f"URL: {url}")
    print(f"Case ID: {CASE_ID}")
    print(f"Fichier: {test_file_path}")
    
    # Headers
    headers = {}
    if TOKEN and TOKEN != "votre_token_ici":
        headers["Authorization"] = f"Bearer {TOKEN}"
    
    # Préparer le fichier
    with open(test_file_path, "rb") as f:
        files = {"file": (test_file_path, f, "application/pdf")}
        
        print(f"\n🔄 Envoi de la requête...")
        
        try:
            response = requests.post(url, headers=headers, files=files)
            
            print(f"\n✅ Réponse reçue:")
            print(f"Status Code: {response.status_code}")
            print(f"Headers: {dict(response.headers)}")
            print(f"Body: {response.text[:500]}")
            
            if response.status_code == 200:
                print(f"\n🎉 UPLOAD RÉUSSI!")
            else:
                print(f"\n❌ ERREUR: {response.status_code}")
                
        except requests.exceptions.ConnectionError as e:
            print(f"\n❌ ERREUR DE CONNEXION:")
            print(f"Le backend ne répond pas sur {BACKEND_URL}")
            print(f"Vérifiez que uvicorn tourne sur le port 8001")
            print(f"Détails: {e}")
            
        except Exception as e:
            print(f"\n❌ ERREUR INATTENDUE:")
            print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    test_upload()
