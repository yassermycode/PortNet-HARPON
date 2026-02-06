from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_test_pdf():
    """Créer un PDF de test pour tester l'analyse IA"""
    
    # Créer le dossier uploads s'il n'existe pas
    os.makedirs("test_documents", exist_ok=True)
    
    filename = "test_documents/declaration_douane_test.pdf"
    
    # Créer le PDF
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Titre
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, "DÉCLARATION EN DOUANE")
    
    # Informations
    c.setFont("Helvetica", 12)
    y = height - 150
    
    content = [
        "Numéro de conteneur: ABCD1234567",
        "",
        "Importateur: ABC Import SARL",
        "Adresse: Casablanca, Maroc",
        "",
        "Pays d'origine: Chine",
        "Port de départ: Shanghai",
        "",
        "Description de la marchandise:",
        "Téléphones mobiles et accessoires électroniques",
        "",
        "Code HS: 851712",
        "",
        "Montant total: 250000 USD",
        "Poids brut: 15000 kg",
        "",
        "Déclarant: XYZ Customs Broker",
        "Transporteur: Fast Shipping Ltd",
        "",
        "Date: 2026-02-03",
    ]
    
    for line in content:
        c.drawString(100, y, line)
        y -= 20
    
    c.save()
    
    print(f"✅ PDF de test créé: {filename}")
    return filename

if __name__ == "__main__":
    create_test_pdf()
