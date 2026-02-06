import numpy as np
from typing import Dict, Any, List

try:
    from sklearn.ensemble import IsolationForest
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("⚠️  WARNING: scikit-learn not available. Isolation Forest will be disabled.")

class IsolationForestDetector:
    """
    Détecteur d'anomalies basé sur l'algorithme Isolation Forest
    
    Principe mathématique :
    - Construit des arbres binaires aléatoires (iTrees)
    - Mesure la longueur du chemin h(x) pour isoler chaque point
    - Score s(x,n) = 2^(-E(h(x))/c(n))
    - Les anomalies sont isolées rapidement (h(x) petit → score élevé)
    """
    
    def __init__(self, contamination=0.1, n_estimators=100, random_state=42):
        """
        Args:
            contamination: Proportion attendue d'anomalies (10% par défaut)
            n_estimators: Nombre d'arbres dans la forêt (100 = standard)
            random_state: Graine aléatoire pour reproductibilité
        """
        if not SKLEARN_AVAILABLE:
            raise ImportError("scikit-learn is not available. Cannot use Isolation Forest.")
            
        self.model = IsolationForest(
            contamination=contamination,
            n_estimators=n_estimators,
            random_state=random_state,
            max_samples=256,  # Sub-sampling pour éviter masking/swamping
            bootstrap=False
        )
        self.is_fitted = False
        self.feature_names = []
    
    @staticmethod
    def extract_features(document_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Extrait les features quantitatives d'un document pour l'analyse
        
        Features extraites :
        1. Ratio Valeur/Poids (DH/kg)
        2. Montant total
        3. Nombre de lignes de produits
        4. Score de risque initial
        5. Nombre de pays mentionnés
        6. Nombre de conteneurs
        
        Returns:
            Dict avec les features numériques
        """
        features = {}
        
        # Feature 1 : Ratio Valeur/Poids
        amounts = document_data.get("amounts", [])
        total_value = sum([a.get("amount", 0) for a in amounts if isinstance(a, dict)])
        
        # Estimation du poids (si disponible ou simulé)
        # Dans un vrai système, cela viendrait du connaissement
        estimated_weight = len(amounts) * 50  # Approximation : 50kg par ligne
        
        if estimated_weight > 0 and total_value > 0:
            features["value_weight_ratio"] = total_value / estimated_weight
        else:
            features["value_weight_ratio"] = 0
        
        # Feature 2 : Montant total
        features["total_value"] = total_value
        
        # Feature 3 : Nombre de lignes (indicateur de complexité)
        features["num_lines"] = len(amounts)
        
        # Feature 4 : Score de risque initial
        features["initial_risk_score"] = document_data.get("risk_score", 0)
        
        # Feature 5 : Nombre de pays
        countries = document_data.get("countries", [])
        features["num_countries"] = len(countries) if countries else 0
        
        # Feature 6 : Nombre de conteneurs
        containers = document_data.get("container_numbers", [])
        features["num_containers"] = len(containers) if containers else 0
        
        # Feature 7 : Longueur du texte (complexité du document)
        text_length = len(document_data.get("extracted_text", ""))
        features["text_length"] = text_length
        
        # Feature 8 : Nombre de facteurs de risque
        risk_factors = document_data.get("risk_factors", [])
        features["num_risk_factors"] = len(risk_factors) if risk_factors else 0
        
        return features
    
    def analyze_single_document(self, document_data: Dict[str, Any], 
                                historical_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyse UN document avec Isolation Forest
        
        Args:
            document_data: Données du document à analyser
            historical_data: Données historiques pour entraîner le modèle
                            (Si None, utilise seulement les features du doc)
        
        Returns:
            Dict avec :
            - isolation_score (0-1) : Score d'anomalie
            - is_anomaly (bool) : True si s > 0.7
            - interpretation (str) : Explication
            - features (dict) : Features utilisées
            - path_length (float) : Longueur moyenne du chemin
        """
        # Extraire les features du document
        doc_features = self.extract_features(document_data)
        
        # Convertir en array numpy
        feature_names = sorted(doc_features.keys())
        X_doc = np.array([[doc_features[f] for f in feature_names]])
        
        # Si données historiques fournies, entraîner le modèle
        if historical_data and len(historical_data) >= 10:
            # Extraire features de l'historique
            X_hist = []
            for hist_doc in historical_data:
                hist_features = self.extract_features(hist_doc)
                X_hist.append([hist_features.get(f, 0) for f in feature_names])
            
            X_hist = np.array(X_hist)
            
            # Combiner avec le document actuel
            X_combined = np.vstack([X_hist, X_doc])
            
            # Entraîner le modèle
            self.model.fit(X_combined)
            self.is_fitted = True
            self.feature_names = feature_names
            
        else:
            # Mode sans historique : créer un dataset synthétique "normal"
            # basé sur des valeurs typiques
            normal_samples = self._generate_normal_samples(feature_names, n=100)
            X_combined = np.vstack([normal_samples, X_doc])
            
            self.model.fit(X_combined)
            self.is_fitted = True
            self.feature_names = feature_names
        
        # Calculer le score d'anomalie
        # decision_function retourne l'opposé du score (négatif = anomalie)
        anomaly_score_raw = self.model.decision_function(X_doc)[0]
        
        # Normaliser le score entre 0 et 1
        # Plus le score est bas (négatif), plus c'est une anomalie
        # On transforme pour que 1 = anomalie forte, 0 = normal
        isolation_score = self._normalize_score(anomaly_score_raw)
        
        # Prédiction binaire
        prediction = self.model.predict(X_doc)[0]
        is_anomaly = (prediction == -1)  # -1 = anomalie dans sklearn
        
        # Interpréter le score
        interpretation = self._interpret_score(isolation_score)
        
        # Calculer la longueur moyenne du chemin (approximation)
        path_length = self._estimate_path_length(anomaly_score_raw)
        
        return {
            "isolation_score": round(isolation_score, 3),
            "is_anomaly": is_anomaly,
            "interpretation": interpretation,
            "confidence_level": self._get_confidence_level(isolation_score),
            "features": doc_features,
            "feature_names": feature_names,
            "path_length": round(path_length, 2),
            "raw_score": round(anomaly_score_raw, 4),
            "method": "Isolation Forest (iTrees)",
            "n_trees": self.model.n_estimators
        }
    
    def _generate_normal_samples(self, feature_names: List[str], n: int = 100) -> np.ndarray:
        """
        Génère des échantillons "normaux" synthétiques basés sur des distributions typiques
        """
        np.random.seed(42)
        samples = []
        
        for _ in range(n):
            sample = {}
            for fname in feature_names:
                if fname == "value_weight_ratio":
                    # Ratio typique : 100-10000 DH/kg pour marchandises normales
                    sample[fname] = np.random.lognormal(7, 1.5)
                elif fname == "total_value":
                    # Valeur typique : 1000-100000 DH
                    sample[fname] = np.random.lognormal(9, 1.5)
                elif fname == "num_lines":
                    # Nombre de lignes : 3-15
                    sample[fname] = np.random.randint(3, 16)
                elif fname == "initial_risk_score":
                    # Score de risque normal : 10-40
                    sample[fname] = np.random.normal(25, 10)
                elif fname == "num_countries":
                    # 1-3 pays
                    sample[fname] = np.random.randint(1, 4)
                elif fname == "num_containers":
                    # 1-5 conteneurs
                    sample[fname] = np.random.randint(1, 6)
                elif fname == "text_length":
                    # 500-5000 caractères
                    sample[fname] = np.random.randint(500, 5001)
                elif fname == "num_risk_factors":
                    # 0-3 facteurs
                    sample[fname] = np.random.randint(0, 4)
                else:
                    sample[fname] = 0
            
            samples.append([sample[f] for f in feature_names])
        
        return np.array(samples)
    
    def _normalize_score(self, raw_score: float) -> float:
        """
        Normalise le score brut entre 0 et 1
        
        sklearn.IsolationForest.decision_function retourne :
        - Valeurs positives pour points normaux
        - Valeurs négatives pour anomalies
        
        On transforme pour que :
        - 0 = très normal
        - 1 = anomalie forte
        """
        # Transformation sigmoïde inversée
        # Plus raw_score est négatif, plus le score normalisé est proche de 1
        normalized = 1 / (1 + np.exp(raw_score * 2))
        return max(0, min(1, normalized))
    
    def _estimate_path_length(self, raw_score: float) -> float:
        """
        Estime la longueur moyenne du chemin h(x)
        """
        # Approximation inverse : score faible → chemin court
        estimated_length = abs(raw_score) * 10 + 5
        return estimated_length
    
    def _interpret_score(self, score: float) -> str:
        """
        Interprète le score selon les seuils mathématiques
        
        Seuils basés sur la théorie d'Isolation Forest :
        - s > 0.7 : Anomalie forte (isolé en < 3 coupes)
        - 0.5 < s < 0.7 : Anomalie modérée
        - s ≈ 0.5 : Comportement normal
        - s < 0.5 : Très normal (enfoui profondément)
        """
        if score > 0.8:
            return "🔴 ANOMALIE CRITIQUE - Dossier statistiquement aberrant sur plusieurs dimensions"
        elif score > 0.7:
            return "🟠 ANOMALIE FORTE - Combinaison inhabituelle de caractéristiques détectée"
        elif score > 0.6:
            return "🟡 ANOMALIE MODÉRÉE - Certaines caractéristiques sortent de l'ordinaire"
        elif score > 0.5:
            return "🟢 LÉGÈREMENT ATYPIQUE - Dans les limites du normal mais à surveiller"
        else:
            return "✅ PROFIL NORMAL - Comportement statistiquement conforme à l'historique"
    
    def _get_confidence_level(self, score: float) -> str:
        """
        Retourne le niveau de confiance de la détection
        """
        if score > 0.8 or score < 0.3:
            return "HAUTE"
        elif score > 0.6 or score < 0.4:
            return "MOYENNE"
        else:
            return "FAIBLE"
