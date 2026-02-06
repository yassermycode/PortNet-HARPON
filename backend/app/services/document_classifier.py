"""
Document Classifier Service
Classification des documents douaniers vs non-douaniers
"""

import re
from typing import Dict, Any


class DocumentClassifier:
    """Classification du type de document douanier"""
    
    # Mots-clés pour identifier les documents douaniers
    COMMERCIAL_INVOICE_KEYWORDS = [
        "FACTURE", "INVOICE", "COMMERCIAL INVOICE", "PROFORMA",
        "FACTURE COMMERCIALE", "FACTURE PROFORMA", "TOTAL AMOUNT",
        "INVOICE NUMBER", "INVOICE DATE", "SHIPPER", "CONSIGNEE",
        "SELLER", "BUYER", "VENDEUR", "ACHETEUR", "MONTANT TOTAL",
        "UNIT PRICE", "PRIX UNITAIRE", "QUANTITY", "QUANTITÉ"
    ]
    
    BILL_OF_LADING_KEYWORDS = [
        "BILL OF LADING", "CONNAISSEMENT", "B/L", "BL NUMBER",
        "OCEAN BILL", "SEA WAYBILL", "CARRIER", "VESSEL", "PORT OF LOADING",
        "PORT OF DISCHARGE", "CONTAINER NUMBER", "SEAL NUMBER",
        "SHIPPING", "EXPÉDITION", "NAVIRE", "CONTENEUR", "PORT DE CHARGEMENT",
        "PORT DE DÉCHARGEMENT", "TRANSPORTEUR", "ARMATEUR"
    ]
    
    PACKING_LIST_KEYWORDS = [
        "PACKING LIST", "LISTE DE COLISAGE", "LISTE D'EMBALLAGE",
        "PACKING DETAILS", "PACKAGE", "CARTON", "GROSS WEIGHT",
        "NET WEIGHT", "DIMENSIONS", "VOLUME", "POIDS BRUT",
        "POIDS NET", "COLIS", "PALETTE", "CBM", "KG", "PIECES"
    ]
    
    CERTIFICATE_KEYWORDS = [
        "CERTIFICATE", "CERTIFICAT", "CERTIFICATE OF ORIGIN",
        "CERTIFICAT D'ORIGINE", "PHYTOSANITARY", "SANITARY",
        "QUALITY CERTIFICATE", "INSPECTION CERTIFICATE",
        "CERTIFICAT SANITAIRE", "CERTIFICAT PHYTOSANITAIRE",
        "ATTESTATION", "CONFORMITÉ", "CONFORMITY"
    ]
    
    CUSTOMS_KEYWORDS = [
        "CUSTOMS", "DOUANE", "DECLARATION", "HS CODE", "TARIFF",
        "IMPORT", "EXPORT", "DUTY", "TAX", "CUSTOMS VALUE",
        "VALEUR EN DOUANE", "DROIT DE DOUANE", "DUM", "DÉCLARATION",
        "RÉGIME DOUANIER", "CODE SH", "NOMENCLATURE", "INCOTERM",
        "FOB", "CIF", "DAP", "DDP", "EXW"
    ]
    
    # Mots-clés de documents NON-douaniers
    NON_CUSTOMS_KEYWORDS = [
        # Programmation / IT
        "COURS", "LEÇON", "LESSON", "CHAPTER", "CHAPITRE",
        "EXERCICE", "EXERCISE", "TUTORIAL", "TUTORIEL",
        "PROGRAMMING", "PROGRAMMATION", "JAVA", "PYTHON", "JAVASCRIPT",
        "CLASS", "FUNCTION", "MÉTHODE", "METHOD", "VARIABLE",
        "CODE", "ALGORITHM", "ALGORITHME", "SOFTWARE", "LOGICIEL",
        "DATABASE", "BASE DE DONNÉES", "API", "FRAMEWORK",
        "PUBLIC STATIC VOID", "IMPORT JAVA", "SYSTEM.OUT", "PRINTLN",
        "DEF ", "RETURN ", "IF ", "ELSE ", "FOR ", "WHILE ",
        
        # Académique
        "ARTICLE", "RESEARCH", "ÉTUDE", "STUDY", "THESIS", "THÈSE",
        "UNIVERSITÉ", "UNIVERSITY", "PROFESSOR", "PROFESSEUR",
        "STUDENT", "ÉTUDIANT", "EXAM", "EXAMEN", "HOMEWORK",
        "BIBLIOGRAPHY", "BIBLIOGRAPHIE", "ABSTRACT", "RÉSUMÉ",
        
        # Autres documents non pertinents
        "RECIPE", "RECETTE", "COOKING", "CUISINE",
        "NOVEL", "ROMAN", "STORY", "HISTOIRE",
        "MUSIC", "MUSIQUE", "LYRICS", "PAROLES",
        "GAME", "JEU", "SPORT", "FOOTBALL", "BASKETBALL"
    ]
    
    @staticmethod
    def classify_document(text: str) -> Dict[str, Any]:
        """
        Classifie le document et détermine s'il est douanier
        
        Returns:
            {
                "is_customs_document": bool,
                "document_type": str,
                "confidence": float,
                "reason": str
            }
        """
        if not text or len(text.strip()) < 50:
            return {
                "is_customs_document": False,
                "document_type": "UNKNOWN",
                "confidence": 0.0,
                "reason": "Document trop court ou vide"
            }
        
        text_upper = text.upper()
        
        # D'abord, vérifier si c'est un document NON-douanier
        non_customs_found = []
        for kw in DocumentClassifier.NON_CUSTOMS_KEYWORDS:
            if kw in text_upper:
                non_customs_found.append(kw)
        
        # Compter les occurrences de mots-clés douaniers
        invoice_score = sum(1 for kw in DocumentClassifier.COMMERCIAL_INVOICE_KEYWORDS if kw in text_upper)
        bl_score = sum(1 for kw in DocumentClassifier.BILL_OF_LADING_KEYWORDS if kw in text_upper)
        packing_score = sum(1 for kw in DocumentClassifier.PACKING_LIST_KEYWORDS if kw in text_upper)
        cert_score = sum(1 for kw in DocumentClassifier.CERTIFICATE_KEYWORDS if kw in text_upper)
        customs_score = sum(1 for kw in DocumentClassifier.CUSTOMS_KEYWORDS if kw in text_upper)
        
        total_customs_score = invoice_score + bl_score + packing_score + cert_score + customs_score
        
        print(f"\n📊 SCORES DE CLASSIFICATION:")
        print(f"   Facture commerciale: {invoice_score}")
        print(f"   Connaissement: {bl_score}")
        print(f"   Liste de colisage: {packing_score}")
        print(f"   Certificat: {cert_score}")
        print(f"   Douane générale: {customs_score}")
        print(f"   TOTAL douanier: {total_customs_score}")
        print(f"   Mots-clés non-douaniers trouvés: {len(non_customs_found)}")
        if non_customs_found:
            print(f"   Exemples: {non_customs_found[:5]}")
        
        # Si beaucoup de mots-clés non-douaniers et peu de douaniers → REJETER
        if len(non_customs_found) >= 3 and total_customs_score < 5:
            return {
                "is_customs_document": False,
                "document_type": "NON_DOUANIER",
                "confidence": 0.0,
                "reason": f"Document non-douanier détecté (mots-clés: {', '.join(non_customs_found[:5])})"
            }
        
        # Déterminer le type de document
        scores = {
            "FACTURE_COMMERCIALE": invoice_score,
            "CONNAISSEMENT": bl_score,
            "LISTE_COLISAGE": packing_score,
            "CERTIFICAT": cert_score,
            "DOCUMENT_DOUANIER": customs_score
        }
        
        max_score = max(scores.values())
        
        # Seuil minimum pour être considéré comme document douanier
        MIN_THRESHOLD = 2
        
        if max_score < MIN_THRESHOLD:
            # Si peu de mots-clés douaniers
            if len(non_customs_found) > 0:
                return {
                    "is_customs_document": False,
                    "document_type": "NON_DOUANIER",
                    "confidence": 0.0,
                    "reason": f"Document non-douanier détecté : {', '.join(non_customs_found[:3])}"
                }
            
            return {
                "is_customs_document": False,
                "document_type": "INCONNU",
                "confidence": 0.0,
                "reason": f"Pas assez de mots-clés douaniers (score max: {max_score}, requis: {MIN_THRESHOLD})"
            }
        
        # Identifier le type principal
        doc_type = max(scores, key=scores.get)
        confidence = min(100.0, (max_score / 10) * 100)
        
        return {
            "is_customs_document": True,
            "document_type": doc_type,
            "confidence": confidence,
            "reason": f"Document identifié avec {max_score} mots-clés pertinents"
        }
