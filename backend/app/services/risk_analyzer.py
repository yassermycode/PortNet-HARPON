from typing import Dict, List
from app.services.data_extractor import DataExtractor
<<<<<<< HEAD
from collections import Counter
import math

def analyze_benford_law(amounts):
    """
    Analyse la Loi de Benford sur les montants
    
    Args:
        amounts: Liste de montants numériques
    
    Returns:
        dict avec résultats de l'analyse
    """
    if not amounts or len(amounts) < 5:
        return {
            "applicable": False,
            "reason": "Pas assez de montants pour l'analyse de Benford (minimum 5)",
            "benford_score": 0,
            "is_suspicious": False
        }
    
    # Distribution théorique de Benford
    benford_distribution = {
        '1': 30.10,
        '2': 17.61,
        '3': 12.49,
        '4': 9.69,
        '5': 7.92,
        '6': 6.69,
        '7': 5.80,
        '8': 5.12,
        '9': 4.58
    }
    
    # Extraire les premiers chiffres des montants
    first_digits = []
    for amount in amounts:
        try:
            # Convertir en string et prendre le premier chiffre non-zéro
            amount_str = str(abs(float(amount))).replace('.', '').replace(',', '')
            for char in amount_str:
                if char != '0' and char.isdigit():
                    first_digits.append(char)
                    break
        except:
            continue
    
    if len(first_digits) < 5:
        return {
            "applicable": False,
            "reason": "Pas assez de premiers chiffres valides",
            "benford_score": 0,
            "is_suspicious": False
        }
    
    # Calculer la distribution observée
    digit_counts = Counter(first_digits)
    total = len(first_digits)
    
    observed_distribution = {}
    expected_counts = []
    observed_counts = []
    
    for digit in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        observed_pct = (digit_counts.get(digit, 0) / total) * 100
        observed_distribution[digit] = round(observed_pct, 2)
        
        expected_counts.append(benford_distribution[digit] * total / 100)
        observed_counts.append(digit_counts.get(digit, 0))
    
    # Calculer le Chi-carré manuellement (sans scipy)
    chi2_stat = 0
    for obs, exp in zip(observed_counts, expected_counts):
        if exp > 0:
            chi2_stat += ((obs - exp) ** 2) / exp
    
    # Calculer la p-value approximative (chi2 avec 8 degrés de liberté)
    # Approximation simple basée sur la table chi-carré
    if chi2_stat < 15.5:
        p_value = 0.5
    elif chi2_stat < 20.1:
        p_value = 0.1
    elif chi2_stat < 26.1:
        p_value = 0.01
    else:
        p_value = 0.001
    
    # Calculer un score de conformité (0-100)
    benford_score = max(0, min(100, 100 - (chi2_stat * 2)))
    
    # Déterminer si c'est suspect
    is_suspicious = chi2_stat > 20  # Seuil pour 8 degrés de liberté, alpha=0.01
    
    # Calculer l'écart moyen
    total_deviation = sum(
        abs(observed_distribution[d] - benford_distribution[d]) 
        for d in ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    )
    avg_deviation = total_deviation / 9
    
    interpretation = (
        "Distribution suspecte - Écart significatif avec Benford (possibilité de fraude)" 
        if is_suspicious 
        else "Distribution conforme à la Loi de Benford"
    )
    
    print(f"   Analyse Benford: {total} montants, chi2={chi2_stat:.2f}, suspect={is_suspicious}")
    
    return {
        "applicable": True,
        "sample_size": total,
        "benford_distribution": benford_distribution,
        "observed_distribution": observed_distribution,
        "chi2_statistic": round(chi2_stat, 2),
        "p_value": round(p_value, 4),
        "benford_score": round(benford_score, 1),
        "average_deviation": round(avg_deviation, 2),
        "is_suspicious": is_suspicious,
        "interpretation": interpretation
    }
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

class RiskAnalyzer:
    """Service pour calculer le score de risque d'un document"""
    
    # Seuils de prix suspects (en USD)
    SUSPICIOUS_AMOUNTS = {
        "very_low": 100,      # Moins de 100 USD
        "very_high": 100000,  # Plus de 100 000 USD
    }
    
    # Mots-clés suspects
    SUSPICIOUS_KEYWORDS = [
        "arme", "weapon", "explosive", "drogue", "drug", "cannabis",
        "cocaine", "héroïne", "contrefaçon", "counterfeit", "fake",
        "militaire", "military", "chimique", "chemical"
    ]
    
    @staticmethod
    def calculate_risk_score(extracted_data: Dict, full_text: str) -> Dict:
        """Calculer le score de risque (0-100)"""
        
        print("🔵 Calcul du score de risque...")
        
        risk_score = 0
        risk_factors = []
        
        # 1. Vérifier le pays d'origine (30 points max)
<<<<<<< HEAD
        origin = (extracted_data.get("origin_country") or "").lower()
=======
        origin = extracted_data.get("origin_country", "").lower()
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        if origin:
            for risky_country in DataExtractor.HIGH_RISK_COUNTRIES:
                if risky_country in origin:
                    risk_score += 30
                    risk_factors.append(f"Pays à haut risque: {origin}")
                    break
        
        # 2. Vérifier les montants (20 points max)
<<<<<<< HEAD
        # Utiliser amounts_raw pour l'analyse (liste de floats)
        amounts_raw = extracted_data.get("amounts_raw", [])
        # Fallback: si amounts_raw n'existe pas, extraire des amounts (objets)
        if not amounts_raw:
            amounts_objs = extracted_data.get("amounts", [])
            if amounts_objs and isinstance(amounts_objs[0], dict):
                amounts_raw = [a.get("amount", 0) for a in amounts_objs if isinstance(a, dict)]
            elif amounts_objs and isinstance(amounts_objs[0], (int, float)):
                amounts_raw = amounts_objs
        
        if amounts_raw:
            max_amount = max(amounts_raw)
            min_amount = min(amounts_raw)
=======
        amounts = extracted_data.get("amounts", [])
        if amounts:
            max_amount = max(amounts)
            min_amount = min(amounts)
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            
            if max_amount > RiskAnalyzer.SUSPICIOUS_AMOUNTS["very_high"]:
                risk_score += 15
                risk_factors.append(f"Montant très élevé: {max_amount:,.2f}")
            
            if min_amount < RiskAnalyzer.SUSPICIOUS_AMOUNTS["very_low"]:
                risk_score += 10
                risk_factors.append(f"Montant très faible: {min_amount:,.2f}")
        
        # 3. Vérifier les mots-clés suspects (25 points max)
        text_lower = full_text.lower()
        suspicious_found = []
        for keyword in RiskAnalyzer.SUSPICIOUS_KEYWORDS:
            if keyword in text_lower:
                suspicious_found.append(keyword)
        
        if suspicious_found:
            risk_score += min(25, len(suspicious_found) * 5)
            risk_factors.append(f"Mots-clés suspects: {', '.join(suspicious_found[:3])}")
        
        # 4. Vérifier l'absence de données importantes (15 points max)
        if not extracted_data.get("importer_name"):
            risk_score += 5
            risk_factors.append("Nom de l'importateur manquant")
        
        if not extracted_data.get("origin_country"):
            risk_score += 5
            risk_factors.append("Pays d'origine manquant")
        
        if not extracted_data.get("product_description"):
            risk_score += 5
            risk_factors.append("Description du produit manquante")
        
        # 5. Vérifier les codes HS (10 points max)
        hs_codes = extracted_data.get("hs_codes", [])
        if not hs_codes:
            risk_score += 10
            risk_factors.append("Code HS manquant")
        
<<<<<<< HEAD
        # 6. Analyse de Benford (15 points max)
        benford_risk = 0
        benford_analysis = {"applicable": False}
        
        # Utiliser amounts_raw pour l'analyse Benford
        if amounts_raw and len(amounts_raw) >= 5:
            print(f"   Analyse Benford sur {len(amounts_raw)} montants: {amounts_raw[:5]}...")
            benford_analysis = analyze_benford_law(amounts_raw)
            
            if benford_analysis.get("applicable"):
                if benford_analysis.get("is_suspicious"):
                    benford_risk = 15
                    risk_factors.append(
                        f"Distribution des montants suspecte selon Benford "
                        f"(écart moyen: {benford_analysis.get('average_deviation', 0):.1f}%)"
                    )
                elif benford_analysis.get("benford_score", 100) < 50:
                    benford_risk = 8
                    risk_factors.append(
                        f"Distribution des montants partiellement conforme à Benford "
                        f"(score: {benford_analysis.get('benford_score', 0)}/100)"
                    )
        
        risk_score += benford_risk
        
        # 7. Isolation Forest (20 points max) - récupéré depuis extracted_data
        iforest_risk = 0
        iforest_result = extracted_data.get("isolation_forest", {})
        
        if iforest_result.get("is_anomaly"):
            iforest_score = iforest_result.get("isolation_score", 0)
            
            if iforest_score > 0.8:
                iforest_risk = 20
                risk_factors.append(
                    f"🔴 Anomalie multi-dimensionnelle critique détectée "
                    f"(score: {iforest_score:.2f}, confiance: {iforest_result.get('confidence_level')})"
                )
                print(f"   🔴 Isolation Forest CRITIQUE: +{iforest_risk} points")
            elif iforest_score > 0.7:
                iforest_risk = 15
                risk_factors.append(
                    f"🟠 Anomalie forte - Combinaison inhabituelle de caractéristiques "
                    f"(score: {iforest_score:.2f})"
                )
                print(f"   🟠 Isolation Forest FORT: +{iforest_risk} points")
            elif iforest_score > 0.6:
                iforest_risk = 10
                risk_factors.append(
                    f"🟡 Anomalie modérée détectée (score: {iforest_score:.2f})"
                )
                print(f"   🟡 Isolation Forest MODÉRÉ: +{iforest_risk} points")
        else:
            print(f"   ✅ Isolation Forest: Profil normal (+0 points)")
        
        risk_score += iforest_risk
        
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        # Limiter le score à 100
        risk_score = min(risk_score, 100)
        
        # Déterminer le niveau de risque
        if risk_score >= 70:
            risk_level = "ÉLEVÉ"
            recommendation = "Inspection physique recommandée"
        elif risk_score >= 40:
            risk_level = "MOYEN"
            recommendation = "Vérification documentaire approfondie"
        else:
            risk_level = "FAIBLE"
            recommendation = "Contrôle standard"
        
        result = {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "recommendation": recommendation,
<<<<<<< HEAD
            "total_factors": len(risk_factors),
            "benford_analysis": benford_analysis
=======
            "total_factors": len(risk_factors)
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        }
        
        print(f"✅ Score de risque calculé: {risk_score}/100 ({risk_level})")
        print(f"   Facteurs de risque: {len(risk_factors)}")
<<<<<<< HEAD
        if benford_analysis.get("applicable"):
            print(f"   Benford: score={benford_analysis.get('benford_score')}, suspect={benford_analysis.get('is_suspicious')}")
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        
        return result
