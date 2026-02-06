import re
from typing import Dict, Optional, List
import spacy

# Charger le modèle français
try:
    nlp = spacy.load("fr_core_news_sm")
except:
    print("⚠️  Modèle spaCy français non trouvé. Installez avec: python -m spacy download fr_core_news_sm")
    nlp = None

class DataExtractor:
    """Service pour extraire les données structurées des documents"""
    
    # Pays à haut risque (exemple)
    HIGH_RISK_COUNTRIES = [
        "afghanistan", "iran", "irak", "syrie", "libye", "somalie",
        "soudan", "corée du nord", "yémen", "venezuela"
    ]
    
    # Ports à surveiller (exemple)
    MONITORED_PORTS = [
        "shanghai", "ningbo", "shenzhen", "hong kong", "busan",
        "singapour", "dubai", "rotterdam", "hambourg"
    ]
    
    @staticmethod
    def extract_importer_name(text: str) -> Optional[str]:
        """Extraire le nom de l'importateur"""
        patterns = [
            r"importateur\s*:?\s*([A-Z][A-Za-z\s&\-\.]+)",
            r"importer\s*:?\s*([A-Z][A-Za-z\s&\-\.]+)",
            r"consignee\s*:?\s*([A-Z][A-Za-z\s&\-\.]+)",
            r"destinataire\s*:?\s*([A-Z][A-Za-z\s&\-\.]+)",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    @staticmethod
<<<<<<< HEAD
    def extract_amounts(text: str) -> List[Dict]:
        """Extraire les montants en devise avec la devise associée"""
        amounts = []
        
        # Patterns améliorés pour détecter les montants avec devise
        patterns_with_currency = [
            # Format: 1,234.56 USD ou 1234.56 USD ou 550.00 USD
            (r"(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)\s*(USD|EUR|MAD)", 1, 2),
            # Format: USD 1,234.56 ou $1234
            (r"(USD|EUR|MAD|€|\$)\s*(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)", 2, 1),
            # Format: 125,000 USD
            (r"(\d{1,3}(?:,\d{3})+)\s*(USD|EUR|MAD)", 1, 2),
        ]
        
        for pattern, amount_group, currency_group in patterns_with_currency:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                amount_str = match.group(amount_group).replace(',', '').replace(' ', '')
                currency = match.group(currency_group).upper()
                if currency == '€':
                    currency = 'EUR'
                elif currency == '$':
                    currency = 'USD'
                try:
                    amount = float(amount_str)
                    if amount > 0:
                        amounts.append({"amount": amount, "currency": currency})
                except ValueError:
                    continue
        
        # Dédupliquer tout en gardant l'ordre
        seen = set()
        unique_amounts = []
        for a in amounts:
            key = (a["amount"], a["currency"])
            if key not in seen:
                seen.add(key)
                unique_amounts.append(a)
        
        return unique_amounts
    
    @staticmethod
    def extract_amounts_raw(text: str) -> List[float]:
        """Extraire uniquement les valeurs numériques des montants (pour analyse Benford)"""
=======
    def extract_amounts(text: str) -> List[float]:
        """Extraire les montants en devise"""
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        amounts = []
        
        # Patterns pour détecter les montants
        patterns = [
<<<<<<< HEAD
            r"(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)\s*(?:USD|EUR|MAD|€|\$)",
            r"(?:USD|EUR|MAD|€|\$)\s*(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)",
            r"(\d{1,3}(?:,\d{3})+)\s*(?:USD|EUR|MAD)",
            r"(\d+(?:,\d{3})*)\s+(?:USD|EUR|MAD)",
=======
            r"(\d{1,3}(?:[,\s]\d{3})*(?:\.\d{2})?)\s*(?:USD|EUR|MAD|€|\$)",
            r"(?:USD|EUR|MAD|€|\$)\s*(\d{1,3}(?:[,\s]\d{3})*(?:\.\d{2})?)",
            r"montant\s*:?\s*(\d{1,3}(?:[,\s]\d{3})*(?:\.\d{2})?)",
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                amount_str = match.group(1).replace(',', '').replace(' ', '')
                try:
                    amount = float(amount_str)
<<<<<<< HEAD
                    if amount > 0:
                        amounts.append(amount)
                except ValueError:
                    continue
        
        # Dédupliquer
        return list(dict.fromkeys(amounts))
=======
                    amounts.append(amount)
                except ValueError:
                    continue
        
        return amounts
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    
    @staticmethod
    def extract_origin_country(text: str) -> Optional[str]:
        """Extraire le pays d'origine"""
        patterns = [
            r"origine\s*:?\s*([A-Z][a-zA-Z\s]+)",
            r"origin\s*:?\s*([A-Z][a-zA-Z\s]+)",
            r"provenance\s*:?\s*([A-Z][a-zA-Z\s]+)",
            r"from\s*:?\s*([A-Z][a-zA-Z\s]+)",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                country = match.group(1).strip()
                # Vérifier que c'est un nom de pays (pas trop long)
                if len(country.split()) <= 3:
                    return country
        
        return None
    
    @staticmethod
    def extract_container_number(text: str) -> Optional[str]:
        """Extraire le numéro de conteneur"""
        # Format standard: 4 lettres + 7 chiffres
        pattern = r"\b([A-Z]{4}\d{7})\b"
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        return None
    
    @staticmethod
    def extract_hs_codes(text: str) -> List[str]:
        """Extraire les codes HS (tarif douanier)"""
        # Code HS: 6 à 10 chiffres
        pattern = r"\b(\d{6,10})\b"
        matches = re.findall(pattern, text)
        
        # Filtrer pour ne garder que les codes HS probables (6-10 chiffres)
        hs_codes = [code for code in matches if 6 <= len(code) <= 10]
        
        return list(set(hs_codes))  # Supprimer les doublons
    
    @staticmethod
    def extract_product_description(text: str) -> Optional[str]:
        """Extraire la description du produit"""
        patterns = [
            r"description\s*:?\s*(.{20,200})",
            r"marchandise\s*:?\s*(.{20,200})",
            r"goods\s*:?\s*(.{20,200})",
            r"produit\s*:?\s*(.{20,200})",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                desc = match.group(1).strip()
                # Nettoyer la description
                desc = re.sub(r'\s+', ' ', desc)
                return desc[:200]  # Limiter à 200 caractères
        
        return None
    
    @staticmethod
    def extract_all_data(text: str) -> Dict:
        """Extraire toutes les données du document"""
        print("🔵 Extraction des données structurées...")
        
<<<<<<< HEAD
        # Extraire les montants avec devises et les montants bruts
        amounts_with_currency = DataExtractor.extract_amounts(text)
        amounts_raw = DataExtractor.extract_amounts_raw(text)
        
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        data = {
            "importer_name": DataExtractor.extract_importer_name(text),
            "origin_country": DataExtractor.extract_origin_country(text),
            "container_number": DataExtractor.extract_container_number(text),
            "hs_codes": DataExtractor.extract_hs_codes(text),
<<<<<<< HEAD
            "amounts": amounts_with_currency,  # Pour affichage frontend
            "amounts_raw": amounts_raw,  # Pour analyse Benford
=======
            "amounts": DataExtractor.extract_amounts(text),
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            "product_description": DataExtractor.extract_product_description(text),
            "text_length": len(text),
        }
        
<<<<<<< HEAD
        print(f"✅ Données extraites:")
        print(f"   - Montants trouvés: {len(amounts_raw)}")
        print(f"   - HS codes: {len(data['hs_codes'])}")
        print(f"   - Pays origine: {data['origin_country']}")
=======
        print(f"✅ Données extraites: {data}")
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        
        return data
