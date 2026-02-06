"""
Script de génération de dossiers de test avec documents
Génère 15 dossiers variés avec des niveaux de risque différents
"""

import sys
import os
from pathlib import Path

# Ajouter le dossier parent au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.case import Case
from app.db.models.document import Document
from app.db.models.user import User
from datetime import datetime, timedelta
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def create_sample_pdf(filename: str, case_number: str, risk_type: str, upload_dir: str):
    """
    Créer un PDF de test avec des données réalistes
    
    risk_type: 'LOW', 'MEDIUM', 'HIGH'
    """
    file_path = os.path.join(upload_dir, filename)
    
    # Créer le PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    
    # En-tête
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, height - 1*inch, "FACTURE COMMERCIALE / COMMERCIAL INVOICE")
    
    # Numéro de facture
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 1.5*inch, f"Numéro de facture: INV-{case_number}-{random.randint(1000, 9999)}")
    c.drawString(1*inch, height - 1.7*inch, f"Date: {datetime.now().strftime('%d/%m/%Y')}")
    
    # Informations selon le niveau de risque
    if risk_type == 'LOW':
        # Dossier fiable - France, montants normaux
        c.drawString(1*inch, height - 2.2*inch, "EXPEDITEUR / SHIPPER:")
        c.drawString(1*inch, height - 2.4*inch, "TechParts SARL")
        c.drawString(1*inch, height - 2.6*inch, "45 Rue de la République")
        c.drawString(1*inch, height - 2.8*inch, "75001 Paris, FRANCE")
        
        c.drawString(1*inch, height - 3.3*inch, "IMPORTATEUR / CONSIGNEE:")
        c.drawString(1*inch, height - 3.5*inch, "Import Solutions Maroc")
        c.drawString(1*inch, height - 3.7*inch, "Boulevard Mohammed V")
        c.drawString(1*inch, height - 3.9*inch, "Casablanca, MAROC")
        
        # Produits avec montants normaux
        y_pos = height - 4.5*inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(1*inch, y_pos, "Description")
        c.drawString(3.5*inch, y_pos, "Quantité")
        c.drawString(4.5*inch, y_pos, "Prix Unit.")
        c.drawString(5.5*inch, y_pos, "Total")
        
        c.setFont("Helvetica", 9)
        items = [
            ("Pièces électroniques - Code HS 8542.31", "150", "12.50 EUR", "1875.00 EUR"),
            ("Connecteurs industriels - Code HS 8536.69", "200", "8.30 EUR", "1660.00 EUR"),
            ("Câbles électriques - Code HS 8544.42", "300", "5.20 EUR", "1560.00 EUR"),
            ("Composants LED - Code HS 8541.41", "100", "15.40 EUR", "1540.00 EUR"),
            ("Condensateurs - Code HS 8532.24", "250", "6.80 EUR", "1700.00 EUR"),
        ]
        
    elif risk_type == 'MEDIUM':
        # Dossier signalé - Pays risque modéré, montants suspects
        c.drawString(1*inch, height - 2.2*inch, "EXPEDITEUR / SHIPPER:")
        c.drawString(1*inch, height - 2.4*inch, "Global Trading Co.")
        c.drawString(1*inch, height - 2.6*inch, "Shenzhen Industrial Zone")
        c.drawString(1*inch, height - 2.8*inch, "Guangdong, CHINA")
        
        c.drawString(1*inch, height - 3.3*inch, "IMPORTATEUR / CONSIGNEE:")
        c.drawString(1*inch, height - 3.5*inch, "Commerce Express Maroc")
        c.drawString(1*inch, height - 3.7*inch, "Zone Industrielle")
        c.drawString(1*inch, height - 3.9*inch, "Tanger, MAROC")
        
        # Produits avec montants un peu suspects (distribution Benford anormale)
        y_pos = height - 4.5*inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(1*inch, y_pos, "Description")
        c.drawString(3.5*inch, y_pos, "Quantité")
        c.drawString(4.5*inch, y_pos, "Prix Unit.")
        c.drawString(5.5*inch, y_pos, "Total")
        
        c.setFont("Helvetica", 9)
        # Montants commençant souvent par 8 ou 9 (anormal pour Benford)
        items = [
            ("Smartphones - Code HS 8517.12", "500", "88.88 USD", "44440.00 USD"),
            ("Tablettes tactiles - Code HS 8471.30", "300", "92.22 USD", "27666.00 USD"),
            ("Écouteurs Bluetooth - Code HS 8518.30", "800", "8.95 USD", "7160.00 USD"),
            ("Chargeurs rapides - Code HS 8504.40", "600", "9.87 USD", "5922.00 USD"),
            ("Câbles USB-C - Code HS 8544.42", "1000", "2.99 USD", "2990.00 USD"),
            ("Adaptateurs - Code HS 8536.69", "400", "8.88 USD", "3552.00 USD"),
        ]
        
    else:  # HIGH
        # Dossier anomalie - Pays à haut risque, sous-valorisation évidente
        c.drawString(1*inch, height - 2.2*inch, "EXPEDITEUR / SHIPPER:")
        c.drawString(1*inch, height - 2.4*inch, "Tehran Export Trading")
        c.drawString(1*inch, height - 2.6*inch, "Industrial District 5")
        c.drawString(1*inch, height - 2.8*inch, "Tehran, IRAN")
        
        c.drawString(1*inch, height - 3.3*inch, "IMPORTATEUR / CONSIGNEE:")
        c.drawString(1*inch, height - 3.5*inch, "Import Rapide SARL")
        c.drawString(1*inch, height - 3.7*inch, "Quartier Industriel")
        c.drawString(1*inch, height - 3.9*inch, "Rabat, MAROC")
        
        # Produits de luxe sous-valorisés (fraude évidente)
        y_pos = height - 4.5*inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(1*inch, y_pos, "Description")
        c.drawString(3.5*inch, y_pos, "Quantité")
        c.drawString(4.5*inch, y_pos, "Prix Unit.")
        c.drawString(5.5*inch, y_pos, "Total")
        
        c.setFont("Helvetica", 9)
        # Prix ridiculement bas pour produits de luxe
        items = [
            ("iPhone 15 Pro Max - Code HS 8517.12", "500", "15.00 USD", "7500.00 USD"),
            ("MacBook Pro 16\" - Code HS 8471.30", "200", "50.00 USD", "10000.00 USD"),
            ("iPad Pro 12.9\" - Code HS 8471.30", "300", "25.00 USD", "7500.00 USD"),
            ("AirPods Pro - Code HS 8518.30", "1000", "5.00 USD", "5000.00 USD"),
            ("Apple Watch Ultra - Code HS 9102.11", "150", "20.00 USD", "3000.00 USD"),
            ("MacBook Air M2 - Code HS 8471.30", "100", "80.00 USD", "8000.00 USD"),
            ("iPad Air - Code HS 8471.30", "200", "30.00 USD", "6000.00 USD"),
            ("Magic Keyboard - Code HS 8471.60", "300", "8.00 USD", "2400.00 USD"),
        ]
    
    # Dessiner les items
    y_pos = height - 4.7*inch
    for item in items:
        c.setFont("Helvetica", 9)
        c.drawString(1*inch, y_pos, item[0])
        c.drawString(3.5*inch, y_pos, item[1])
        c.drawString(4.5*inch, y_pos, item[2])
        c.drawString(5.5*inch, y_pos, item[3])
        y_pos -= 0.25*inch
    
    # Total
    y_pos -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    total = sum([float(item[3].split()[0].replace(',', '')) for item in items])
    currency = items[0][3].split()[1]
    c.drawString(4.5*inch, y_pos, f"TOTAL: {total:.2f} {currency}")
    
    # Informations de transport
    y_pos -= 0.5*inch
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, y_pos, f"Port de chargement: {random.choice(['Shanghai', 'Hamburg', 'Rotterdam', 'Dubai'])}")
    c.drawString(1*inch, y_pos - 0.2*inch, "Port de déchargement: Casablanca, Maroc")
    c.drawString(1*inch, y_pos - 0.4*inch, f"Conteneur: {random.choice(['TCLU', 'MSCU', 'HLCU'])}{random.randint(1000000, 9999999)}")
    
    # Pied de page
    c.setFont("Helvetica", 8)
    c.drawString(1*inch, 1*inch, "Document généré automatiquement - PortNet HARPON Test Data")
    
    c.save()
    return file_path


def generate_test_data():
    """
    Générer 15 dossiers de test avec documents
    """
    db = SessionLocal()
    
    try:
        # Récupérer l'utilisateur admin
        admin = db.query(User).filter(User.username == "admin").first()
        
        if not admin:
            print("Erreur: Utilisateur admin non trouvé. Exécute d'abord create_admin.py")
            return
        
        # Créer le dossier uploads s'il n'existe pas
        upload_dir = os.path.join(os.path.dirname(__file__), '..', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        print("\n" + "="*60)
        print("Démarrage de la génération de 15 dossiers de test")
        print("="*60 + "\n")
        
        # Configuration des dossiers
        # 5 FIABLES (LOW), 7 SIGNALÉS (MEDIUM), 3 ANOMALIES (HIGH)
        case_configs = [
            # FIABLES (5)
            {"risk": "LOW", "importer": "Import Solutions Maroc", "declarant": "Déclarant Certifié A"},
            {"risk": "LOW", "importer": "TechImport SARL", "declarant": "Déclarant Agréé B"},
            {"risk": "LOW", "importer": "Euro Trading Maroc", "declarant": "Déclarant Pro C"},
            {"risk": "LOW", "importer": "Logistique Express", "declarant": "Déclarant Expert D"},
            {"risk": "LOW", "importer": "Commerce International", "declarant": "Déclarant Elite E"},
            
            # SIGNALÉS (7)
            {"risk": "MEDIUM", "importer": "Asia Import Co", "declarant": "Déclarant Standard F"},
            {"risk": "MEDIUM", "importer": "Global Trade Partners", "declarant": "Déclarant Normal G"},
            {"risk": "MEDIUM", "importer": "China Express Maroc", "declarant": "Déclarant Basic H"},
            {"risk": "MEDIUM", "importer": "Orient Trading", "declarant": "Déclarant Régulier I"},
            {"risk": "MEDIUM", "importer": "East Commerce", "declarant": "Déclarant Classique J"},
            {"risk": "MEDIUM", "importer": "Pacific Imports", "declarant": "Déclarant Simple K"},
            {"risk": "MEDIUM", "importer": "Dragon Trading Co", "declarant": "Déclarant Ordinaire L"},
            
            # ANOMALIES (3)
            {"risk": "HIGH", "importer": "Import Suspect SARL", "declarant": "Déclarant Nouveau M"},
            {"risk": "HIGH", "importer": "Commerce Douteux", "declarant": "Déclarant Inconnu N"},
            {"risk": "HIGH", "importer": "Trading Opaque Ltd", "declarant": "Déclarant Non-Certifié O"},
        ]
        
        created_count = 0
        
        for idx, config in enumerate(case_configs, 1):
            # Créer le dossier avec un numéro unique
            timestamp = int(datetime.now().timestamp() * 1000)
            case_number = f"CASE-{datetime.now().year}-{idx:03d}-{random.randint(1000, 9999)}"
            
            # Vérifier si le dossier existe déjà
            existing = db.query(Case).filter(Case.case_number == case_number).first()
            if existing:
                print(f"Dossier {case_number} existe déjà, passage...")
                continue
            
            new_case = Case(
                case_number=case_number,
                importer_name=config["importer"],
                declarant_name=config["declarant"],
                transporter_name=random.choice([
                    "Maersk Line", "CMA CGM", "MSC", "Hapag-Lloyd", 
                    "COSCO", "Evergreen", "ONE"
                ]),
                priority=random.choice(["NORMAL", "URGENT", "TRES_URGENT"]),
                status="OPEN",
                description=f"Dossier d'importation - Conteneur maritime - Niveau de risque: {config['risk']}",
                risk_score=0,
                risk_level="INCONNU",
                created_by=admin.id,
                created_at=datetime.now() - timedelta(days=random.randint(0, 30))
            )
            
            db.add(new_case)
            db.commit()
            db.refresh(new_case)
            
            # Créer 2-3 documents par dossier
            num_docs = random.randint(2, 3)
            
            for doc_idx in range(1, num_docs + 1):
                filename = f"{case_number}_facture_{doc_idx}.pdf"
                
                # Créer le PDF
                file_path = create_sample_pdf(
                    filename=filename,
                    case_number=case_number,
                    risk_type=config["risk"],
                    upload_dir=upload_dir
                )
                
                # Obtenir la taille du fichier
                file_size = os.path.getsize(file_path)
                
                # Créer le document dans la base
                new_doc = Document(
                    case_id=new_case.id,
                    filename=filename,
                    file_path=file_path,
                    file_type="application/pdf",
                    file_size=file_size,
                    uploaded_by=admin.id,
                    status="UPLOADED",
                    document_type="FACTURE_COMMERCIALE",
                    created_at=datetime.now() - timedelta(days=random.randint(0, 30))
                )
                
                db.add(new_doc)
            
            db.commit()
            
            created_count += 1
            
            # Afficher le progrès
            risk_icon = "[FIABLE]" if config["risk"] == "LOW" else "[SIGNALE]" if config["risk"] == "MEDIUM" else "[ANOMALIE]"
            print(f"{risk_icon} [{created_count}/15] Dossier créé: {case_number}")
            print(f"   Importateur: {config['importer']}")
            print(f"   Niveau: {config['risk']}")
            print(f"   Documents: {num_docs} PDF générés")
            print()
        
        print("\n" + "="*60)
        print(f"Génération terminée: {created_count} dossiers créés")
        print("="*60)
        print(f"\nRépartition:")
        print(f"   [FIABLE]    Fiables (LOW):    5 dossiers")
        print(f"   [SIGNALE]   Signalés (MEDIUM): 7 dossiers")
        print(f"   [ANOMALIE]  Anomalies (HIGH):  3 dossiers")
        print(f"\nDocuments PDF créés dans: {upload_dir}")
        print(f"\nProchaine étape: Ouvre l'application et analyse les documents!")
        print("   Vers Va dans 'Dossiers'")
        print("   Vers Ouvre un dossier")
        print("   Vers Clique sur 'Analyser' pour chaque document")
        
    except Exception as e:
        print(f"\nErreur: {e}")
        db.rollback()
        raise
    
    finally:
        db.close()


if __name__ == "__main__":
    generate_test_data()
