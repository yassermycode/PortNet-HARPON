import os
import shutil
from datetime import datetime, timedelta
import random
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen import canvas

# Dossier de sortie
OUTPUT_DIR = "test_pdfs"

# Supprimer l'ancien dossier et recréer
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
    print(f"Ancien dossier '{OUTPUT_DIR}' supprime")

os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"Nouveau dossier '{OUTPUT_DIR}' cree\n")

# Listes de donnees
PAYS_RISQUE = ["Chine", "Iran", "Coree du Nord", "Syrie", "Venezuela", "Russie"]
PAYS_NORMAUX = ["France", "Allemagne", "Espagne", "Italie", "Maroc", "Tunisie", "Belgique", "Portugal"]
IMPORTATEURS = ["ABC Trading SARL", "Import Export Plus", "Global Commerce", "Mediterranean Trade Co.", "Atlas Import"]
EXPORTATEURS = ["Shanghai Export Ltd", "Beijing Trading Co", "Tehran Commerce", "European Exports GmbH", "Paris Trade SA"]

MOTS_SUSPECTS = ["armes", "militaire", "explosifs", "dual-use", "sanctionne", "contrebande"]

def generer_numero_facture():
    return f"INV-{random.randint(2023, 2026)}-{random.randint(1000, 9999)}"

def generer_numero_bl():
    return f"BL{random.randint(100000, 999999)}"

def generer_numero_conteneur():
    lettres = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
    chiffres = ''.join(random.choices('0123456789', k=7))
    return f"{lettres}{chiffres}"

# ============================================
# 1. FACTURE COMMERCIALE NORMALE (7 MONTANTS)
# ============================================
def generer_facture_normale(numero):
    """Genere une facture normale avec 7 montants"""
    filename = os.path.join(OUTPUT_DIR, f"{numero}_facture_normale.pdf")
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=30,
        alignment=1
    )
    
    story.append(Paragraph("FACTURE COMMERCIALE", title_style))
    story.append(Paragraph("COMMERCIAL INVOICE", styles['Heading2']))
    story.append(Spacer(1, 20))
    
    invoice_num = generer_numero_facture()
    date = datetime.now() - timedelta(days=random.randint(1, 30))
    
    info_data = [
        ["Numero de facture:", invoice_num],
        ["Date:", date.strftime("%d/%m/%Y")],
        ["Exportateur:", random.choice(EXPORTATEURS)],
        ["Importateur:", random.choice(IMPORTATEURS)],
        ["Pays d'origine:", random.choice(PAYS_NORMAUX)],
        ["Destination:", "Maroc"],
    ]
    
    info_table = Table(info_data, colWidths=[8*cm, 10*cm])
    info_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold', 10),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f3f4f6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("DESCRIPTION DES MARCHANDISES", styles['Heading3']))
    story.append(Spacer(1, 10))
    
    # 7 LIGNES DE PRODUITS (7 montants pour Benford)
    produits_data = [
        ["Qte", "Description", "Code HS", "Prix Unit.", "Total"],
        ["100", "Cotton T-Shirts", "6109.10", "5.50 USD", "550.00 USD"],
        ["200", "Electronic components", "8542.31", "12.00 USD", "2,400.00 USD"],
        ["50", "Plastic containers", "3923.30", "3.20 USD", "160.00 USD"],
        ["75", "Metal parts", "7326.90", "8.00 USD", "600.00 USD"],
        ["150", "Rubber seals", "4016.99", "2.50 USD", "375.00 USD"],
        ["300", "Packaging materials", "4819.20", "1.20 USD", "360.00 USD"],
        ["80", "Glass bottles", "7010.90", "4.50 USD", "360.00 USD"],
    ]
    
    produits_table = Table(produits_data, colWidths=[2*cm, 7*cm, 3*cm, 3*cm, 3*cm])
    produits_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563eb')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(produits_table)
    story.append(Spacer(1, 20))
    
    total_data = [["TOTAL:", "4,805.00 USD"]]
    total_table = Table(total_data, colWidths=[15*cm, 3*cm])
    total_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold', 12),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f3f4f6')),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    story.append(total_table)
    
    doc.build(story)
    print(f"  Genere: {filename} (7 montants)")

# ============================================
# 2. FACTURE PAYS A RISQUE (8 MONTANTS)
# ============================================
def generer_facture_pays_risque(numero):
    """Genere une facture avec pays a risque et 8 montants"""
    filename = os.path.join(OUTPUT_DIR, f"{numero}_facture_pays_risque.pdf")
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#dc2626'),
        spaceAfter=30,
        alignment=1
    )
    
    story.append(Paragraph("COMMERCIAL INVOICE", title_style))
    story.append(Spacer(1, 20))
    
    invoice_num = generer_numero_facture()
    date = datetime.now() - timedelta(days=random.randint(1, 30))
    pays_risque = random.choice(PAYS_RISQUE)
    
    info_data = [
        ["Invoice Number:", invoice_num],
        ["Date:", date.strftime("%d/%m/%Y")],
        ["Exporter:", "Beijing Industrial Corp"],
        ["Importer:", random.choice(IMPORTATEURS)],
        ["Country of Origin:", pays_risque],
        ["Destination:", "Morocco"],
    ]
    
    info_table = Table(info_data, colWidths=[8*cm, 10*cm])
    info_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold', 10),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#fee2e2')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("GOODS DESCRIPTION", styles['Heading3']))
    story.append(Spacer(1, 10))
    
    # 8 LIGNES AVEC MONTANTS ELEVES
    produits_data = [
        ["Qty", "Description", "HS Code", "Unit Price", "Total"],
        ["500", "Industrial Equipment", "8479.89", "250.00 USD", "125,000 USD"],
        ["200", "Machinery Parts", "8431.39", "180.00 USD", "36,000 USD"],
        ["300", "Electronic Circuits", "8542.31", "95.00 USD", "28,500 USD"],
        ["150", "Hydraulic Systems", "8412.21", "420.00 USD", "63,000 USD"],
        ["100", "Control Panels", "8537.10", "310.00 USD", "31,000 USD"],
        ["250", "Power Supplies", "8504.40", "78.00 USD", "19,500 USD"],
        ["180", "Sensor Modules", "9032.89", "165.00 USD", "29,700 USD"],
        ["90", "Motor Assemblies", "8501.31", "540.00 USD", "48,600 USD"],
    ]
    
    produits_table = Table(produits_data, colWidths=[2*cm, 6*cm, 3*cm, 3.5*cm, 3.5*cm])
    produits_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 9),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 8),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dc2626')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(produits_table)
    story.append(Spacer(1, 20))
    
    total_data = [["TOTAL:", "381,300 USD"]]
    total_table = Table(total_data, colWidths=[15*cm, 3*cm])
    total_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold', 14),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fee2e2')),
        ('BOX', (0, 0), (-1, -1), 2, colors.red),
    ]))
    
    story.append(total_table)
    
    doc.build(story)
    print(f"  Genere: {filename} (8 montants, PAYS: {pays_risque})")

# ============================================
# 3. FACTURE MOTS SUSPECTS (6 MONTANTS)
# ============================================
def generer_facture_mots_suspects(numero):
    """Genere une facture avec mots suspects et 6 montants"""
    filename = os.path.join(OUTPUT_DIR, f"{numero}_facture_mots_suspects.pdf")
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#ea580c'),
        spaceAfter=30,
        alignment=1
    )
    
    story.append(Paragraph("INVOICE", title_style))
    story.append(Spacer(1, 20))
    
    invoice_num = generer_numero_facture()
    
    info_data = [
        ["Invoice No:", invoice_num],
        ["Date:", datetime.now().strftime("%d/%m/%Y")],
        ["From:", "Defense Systems International"],
        ["To:", random.choice(IMPORTATEURS)],
    ]
    
    info_table = Table(info_data, colWidths=[8*cm, 10*cm])
    info_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # 6 LIGNES AVEC MOTS SUSPECTS
    produits_data = [
        ["Qty", "Description", "Total"],
        ["10", "Dual-use technology components for industrial applications", "45,000 USD"],
        ["5", "Military-grade surveillance equipment", "32,000 USD"],
        ["8", "Tactical communication systems", "28,500 USD"],
        ["12", "Advanced sensor arrays (dual-use)", "38,400 USD"],
        ["6", "Encrypted control modules", "19,800 USD"],
        ["15", "High-precision targeting systems", "67,500 USD"],
    ]
    
    produits_table = Table(produits_data, colWidths=[2*cm, 12*cm, 4*cm])
    produits_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#ea580c')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(produits_table)
    story.append(Spacer(1, 20))
    
    total_data = [["TOTAL:", "231,200 USD"]]
    total_table = Table(total_data, colWidths=[14*cm, 4*cm])
    total_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold', 12),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    story.append(total_table)
    
    doc.build(story)
    print(f"  Genere: {filename} (6 montants, MOTS SUSPECTS)")

# ============================================
# 4. FACTURE FALSIFIEE - BENFORD ANORMAL (10 montants)
# ============================================
def generer_facture_falsifiee_benford(numero):
    """Genere une facture avec distribution Benford anormale (fraude)"""
    filename = os.path.join(OUTPUT_DIR, f"{numero}_facture_FALSIFIEE_benford.pdf")
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#7c3aed'),
        spaceAfter=30,
        alignment=1
    )
    
    story.append(Paragraph("INVOICE", title_style))
    story.append(Spacer(1, 20))
    
    invoice_num = "INV-2025-FAKE"
    date_future = datetime.now() + timedelta(days=15)
    
    info_data = [
        ["Invoice Number:", invoice_num],
        ["Date:", date_future.strftime("%d/%m/%Y")],
        ["Exporter:", "Suspicious Trading Ltd"],
        ["Importer:", "Unknown Company"],
    ]
    
    info_table = Table(info_data, colWidths=[8*cm, 10*cm])
    info_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#faf5ff')),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # 10 MONTANTS INVENTES - DISTRIBUTION ANORMALE POUR BENFORD
    # Tous commencent par 5, 8, 9 (distribution non-naturelle)
    produits_data = [
        ["Qty", "Description", "Total"],
        ["100", "Item A", "5,000 USD"],  # Premier chiffre = 5
        ["200", "Item B", "8,000 USD"],  # Premier chiffre = 8
        ["150", "Item C", "9,000 USD"],  # Premier chiffre = 9
        ["180", "Item D", "5,500 USD"],  # Premier chiffre = 5
        ["220", "Item E", "8,500 USD"],  # Premier chiffre = 8
        ["190", "Item F", "9,200 USD"],  # Premier chiffre = 9
        ["170", "Item G", "5,800 USD"],  # Premier chiffre = 5
        ["210", "Item H", "8,800 USD"],  # Premier chiffre = 8
        ["160", "Item I", "9,500 USD"],  # Premier chiffre = 9
        ["140", "Item J", "5,200 USD"],  # Premier chiffre = 5
    ]
    
    produits_table = Table(produits_data, colWidths=[2*cm, 12*cm, 4*cm])
    produits_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7c3aed')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    story.append(produits_table)
    story.append(Spacer(1, 20))
    
    total_data = [["TOTAL:", "74,500 USD"]]
    total_table = Table(total_data, colWidths=[14*cm, 4*cm])
    total_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold', 12),
        ('BOX', (0, 0), (-1, -1), 2, colors.purple),
    ]))
    
    story.append(total_table)
    
    doc.build(story)
    print(f"  Genere: {filename} (10 montants, BENFORD ANORMAL)")

# ============================================
# 5. DOCUMENT NON-DOUANIER (cours)
# ============================================
def generer_document_non_douanier(numero):
    """Genere un document non-douanier"""
    filename = os.path.join(OUTPUT_DIR, f"{numero}_cours_java_NON_DOUANIER.pdf")
    
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        alignment=1
    )
    
    story.append(Paragraph("Introduction a Java", title_style))
    story.append(Spacer(1, 20))
    
    contenu = """
    <b>Chapitre 1: Les Bases de Java</b><br/><br/>
    
    Java est un langage de programmation oriente objet cree en 1995.
    Il fonctionne sur toutes les plateformes grace a la JVM.<br/><br/>
    
    <b>1.1 Variables</b><br/>
    - int: entiers<br/>
    - double: decimaux<br/>
    - String: texte<br/><br/>
    
    <b>Exemple:</b><br/>
    <font name="Courier">
    public class HelloWorld {<br/>
    &nbsp;&nbsp;public static void main(String[] args) {<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;System.out.println("Hello!");<br/>
    &nbsp;&nbsp;}<br/>
    }
    </font>
    """
    
    story.append(Paragraph(contenu, styles['Normal']))
    
    doc.build(story)
    print(f"  Genere: {filename} (DOIT ETRE REJETE)")

# ============================================
# FONCTION PRINCIPALE
# ============================================
def generer_tous_les_pdfs():
    print("\n" + "="*70)
    print("GENERATION DES PDFs DE TEST (AVEC 5+ MONTANTS POUR BENFORD)")
    print("="*70 + "\n")
    
    # Factures normales (7 montants chacune)
    print("Factures normales (7 montants)...")
    generer_facture_normale(1)
    generer_facture_normale(2)
    
    # Factures pays a risque (8 montants chacune)
    print("\nFactures pays a risque (8 montants)...")
    generer_facture_pays_risque(3)
    generer_facture_pays_risque(4)
    
    # Factures mots suspects (6 montants chacune)
    print("\nFactures mots suspects (6 montants)...")
    generer_facture_mots_suspects(5)
    generer_facture_mots_suspects(6)
    
    # Factures falsifiees avec Benford anormal (10 montants)
    print("\nFactures falsifiees - Benford anormal (10 montants)...")
    generer_facture_falsifiee_benford(7)
    generer_facture_falsifiee_benford(8)
    
    # Documents non-douaniers
    print("\nDocuments non-douaniers (a rejeter)...")
    generer_document_non_douanier(9)
    generer_document_non_douanier(10)
    
    print("\n" + "="*70)
    print(f"TERMINE ! {len(os.listdir(OUTPUT_DIR))} PDFs generes dans '{OUTPUT_DIR}/'")
    print("="*70 + "\n")
    
    print("RESUME :\n")
    print("  Factures normales (7 montants, risque faible) : 1_*, 2_*")
    print("  Factures pays risque (8 montants, risque moyen-eleve) : 3_*, 4_*")
    print("  Factures mots suspects (6 montants, risque eleve) : 5_*, 6_*")
    print("  Factures falsifiees Benford (10 montants, Benford ANORMAL) : 7_*, 8_*")
    print("  Documents non-douaniers (a rejeter) : 9_*, 10_*\n")
    print("  Tous les documents ont 5+ montants sauf les non-douaniers")
    print("  Les factures 7_* et 8_* ont une distribution Benford SUSPECTE")

if __name__ == "__main__":
    generer_tous_les_pdfs()
