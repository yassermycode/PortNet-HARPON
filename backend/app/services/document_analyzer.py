from typing import Dict
from app.services.pdf_extractor import PDFExtractor
from app.services.data_extractor import DataExtractor
from app.services.risk_analyzer import RiskAnalyzer
<<<<<<< HEAD
from app.services.document_classifier import DocumentClassifier
from app.services.isolation_forest_detector import IsolationForestDetector
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

class DocumentAnalyzer:
    """Service principal pour analyser un document"""
    
    @staticmethod
    def analyze_document(file_path: str) -> Dict:
        """
        Analyser un document complet
        
        Returns:
            Dict contenant:
            - extracted_text: le texte extrait
            - extracted_data: les données structurées
            - risk_analysis: le score et les facteurs de risque
<<<<<<< HEAD
            - analysis_status: SUCCESS, ERROR ou REJECTED
            - document_classification: type de document détecté
=======
            - analysis_status: SUCCESS ou ERROR
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        """
        
        print(f"\n{'='*60}")
        print(f"🤖 DÉBUT DE L'ANALYSE IA DU DOCUMENT")
        print(f"{'='*60}\n")
        
<<<<<<< HEAD
        result = {
            "analysis_status": "ERROR",
            "error": None,
            "extracted_text": "",
            "extracted_data": {},
            "risk_analysis": {},
            "document_classification": None
        }
        
        try:
            # ÉTAPE 1: Extraire le texte du PDF
            print("📄 ÉTAPE 1/4: Extraction du texte...")
            extracted_text = PDFExtractor.extract_text(file_path)
            
            if not extracted_text or len(extracted_text) < 10:
                result["error"] = "Impossible d'extraire le texte du document"
                return result
            
            result["extracted_text"] = extracted_text[:1000]  # Limiter pour la DB
            
            # ÉTAPE 1.5: CLASSIFICATION DU DOCUMENT
            print("\n🔍 ÉTAPE 1.5/4: Classification du type de document...")
            
            classification = DocumentClassifier.classify_document(extracted_text)
            result["document_classification"] = classification
            
            print(f"✅ Classification terminée:")
            print(f"   Type: {classification['document_type']}")
            print(f"   Document douanier: {classification['is_customs_document']}")
            print(f"   Confiance: {classification['confidence']:.1f}%")
            print(f"   Raison: {classification['reason']}")
            
            # Si ce n'est PAS un document douanier, REJETER
            if not classification["is_customs_document"]:
                result["analysis_status"] = "REJECTED"
                result["error"] = f"❌ DOCUMENT NON-DOUANIER - {classification['reason']}"
                
                print(f"\n{'='*60}")
                print(f"❌ ANALYSE REJETÉE")
                print(f"{'='*60}")
                print(f"Raison: {classification['reason']}")
                print(f"\nCe document ne semble pas être un document douanier.")
                print(f"Seuls les documents suivants sont acceptés:")
                print(f"  - Factures commerciales")
                print(f"  - Connaissements (Bill of Lading)")
                print(f"  - Listes de colisage")
                print(f"  - Certificats d'origine")
                print(f"  - Déclarations douanières")
                print(f"{'='*60}\n")
                
                return result
            
            # ÉTAPE 2: Extraire les données structurées
            print("\n🔍 ÉTAPE 2/4: Extraction des données structurées...")
            extracted_data = DataExtractor.extract_all_data(extracted_text)
            
            # ÉTAPE 2.5: ANALYSE ISOLATION FOREST
            print("\n🌲 ÉTAPE 2.5/4: Détection d'anomalies multi-dimensionnelles (Isolation Forest)...")
            
            try:
                iforest_detector = IsolationForestDetector(
                    contamination=0.15,  # 15% d'anomalies attendues
                    n_estimators=100,
                    random_state=42
                )
                
                # Préparer les données pour Isolation Forest
                document_for_iforest = {
                    "amounts": extracted_data.get("amounts", []),
                    "countries": extracted_data.get("countries", []),
                    "container_numbers": extracted_data.get("container_numbers", []),
                    "extracted_text": extracted_text,
                    "risk_score": 0,  # Sera recalculé après
                    "risk_factors": []
                }
                
                # Analyser avec Isolation Forest (sans historique pour l'instant)
                iforest_result = iforest_detector.analyze_single_document(
                    document_data=document_for_iforest,
                    historical_data=None  # TODO: Intégrer l'historique des dossiers
                )
                
                print(f"✅ Isolation Forest terminé:")
                print(f"   Score d'anomalie: {iforest_result['isolation_score']:.3f}/1.0")
                print(f"   Anomalie détectée: {iforest_result['is_anomaly']}")
                print(f"   Longueur de chemin: {iforest_result['path_length']:.2f}")
                print(f"   Interprétation: {iforest_result['interpretation']}")
                
                # Stocker le résultat dans extracted_data pour le frontend
                extracted_data["isolation_forest"] = iforest_result
            except Exception as e:
                print(f"⚠️  ATTENTION: Isolation Forest non disponible - {str(e)}")
                print(f"   L'analyse continue sans Isolation Forest...")
                # Créer un résultat par défaut
                extracted_data["isolation_forest"] = {
                    "isolation_score": 0.5,
                    "is_anomaly": False,
                    "interpretation": "Isolation Forest non disponible - sklearn non installé",
                    "confidence_level": "N/A",
                    "features": {},
                    "feature_names": [],
                    "path_length": 0,
                    "raw_score": 0,
                    "method": "Isolation Forest (non disponible)",
                    "n_trees": 0
                }
            
            result["extracted_data"] = extracted_data
            
            # ÉTAPE 3: Calculer le score de risque
            print("\n⚠️  ÉTAPE 3/4: Calcul du score de risque...")
            risk_analysis = RiskAnalyzer.calculate_risk_score(extracted_data, extracted_text)
            result["risk_analysis"] = risk_analysis
            
            # SUCCÈS
            result["analysis_status"] = "SUCCESS"
            
            print(f"\n{'='*60}")
            print(f"✅ ANALYSE TERMINÉE AVEC SUCCÈS")
            print(f"   Type de document: {classification['document_type']}")
=======
        try:
            # 1. Extraire le texte du PDF
            print("📄 ÉTAPE 1/3: Extraction du texte...")
            extracted_text = PDFExtractor.extract_text(file_path)
            
            if not extracted_text or len(extracted_text) < 10:
                return {
                    "analysis_status": "ERROR",
                    "error": "Impossible d'extraire le texte du document",
                    "extracted_text": "",
                    "extracted_data": {},
                    "risk_analysis": {}
                }
            
            # 2. Extraire les données structurées
            print("\n🔍 ÉTAPE 2/3: Extraction des données structurées...")
            extracted_data = DataExtractor.extract_all_data(extracted_text)
            
            # 3. Calculer le score de risque
            print("\n⚠️  ÉTAPE 3/3: Calcul du score de risque...")
            risk_analysis = RiskAnalyzer.calculate_risk_score(extracted_data, extracted_text)
            
            print(f"\n{'='*60}")
            print(f"✅ ANALYSE TERMINÉE AVEC SUCCÈS")
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            print(f"   Score de risque: {risk_analysis['risk_score']}/100")
            print(f"   Niveau: {risk_analysis['risk_level']}")
            print(f"   Facteurs détectés: {risk_analysis['total_factors']}")
            print(f"{'='*60}\n")
            
<<<<<<< HEAD
            return result
=======
            return {
                "analysis_status": "SUCCESS",
                "extracted_text": extracted_text[:1000],  # Limiter pour la DB
                "extracted_data": extracted_data,
                "risk_analysis": risk_analysis
            }
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            
        except Exception as e:
            print(f"\n❌ ERREUR LORS DE L'ANALYSE: {str(e)}")
            import traceback
            traceback.print_exc()
            
<<<<<<< HEAD
            result["error"] = str(e)
            return result
=======
            return {
                "analysis_status": "ERROR",
                "error": str(e),
                "extracted_text": "",
                "extracted_data": {},
                "risk_analysis": {}
            }
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
