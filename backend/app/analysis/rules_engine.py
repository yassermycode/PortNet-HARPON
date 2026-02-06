"""
Rules Engine - Règles métier douanières
Vérifie la conformité avec les règles douanières spécifiques.
"""

from typing import Dict, List, Optional
from datetime import datetime


class Rule:
    """Classe de base pour une règle métier."""
    
    def __init__(self, rule_id: str, name: str, severity: str, score: int):
        self.rule_id = rule_id
        self.name = name
        self.severity = severity  # LOW, MEDIUM, HIGH, CRITICAL
        self.score = score  # Contribution au score global
    
    def check(self, case_data: Dict, features: List[Dict]) -> Optional[Dict]:
        """
        Vérifie si la règle est violée.
        
        Returns:
            Dict avec détails de la violation si applicable, None sinon
        """
        raise NotImplementedError


class HighValueLowWeightRule(Rule):
    """Règle: Montant élevé pour un poids faible (sous-évaluation suspectée)"""
    
    def __init__(self):
        super().__init__(
            rule_id='R001',
            name='Montant élevé / Poids faible',
            severity='HIGH',
            score=60
        )
    
    def check(self, case_data: Dict, features: List[Dict]) -> Optional[Dict]:
        features_dict = {f['feature_name']: f['feature_value'] for f in features}
        
        amount = features_dict.get('amount_total')
        weight = features_dict.get('weight_kg')
        
        if amount is None or weight is None or weight == 0:
            return None
        
        # Seuil: plus de 1000 USD par kg
        ratio = amount / weight
        
        if ratio > 1000:
            return {
                'rule_id': self.rule_id,
                'rule_name': self.name,
                'severity': self.severity,
                'score': self.score,
                'evidence': {
                    'amount_total': amount,
                    'weight_kg': weight,
                    'ratio_usd_per_kg': round(ratio, 2),
                    'threshold': 1000,
                },
                'message': f'Ratio montant/poids suspect: {ratio:.2f} USD/kg (seuil: 1000)',
            }
        
        return None


class SuspiciousOriginCountryRule(Rule):
    """Règle: Pays d'origine à risque élevé"""
    
    HIGH_RISK_COUNTRIES = ['CN', 'VN', 'IN', 'PK', 'BD']  # Exemples
    
    def __init__(self):
        super().__init__(
            rule_id='R002',
            name='Pays d\'origine à risque',
            severity='MEDIUM',
            score=40
        )
    
    def check(self, case_data: Dict, features: List[Dict]) -> Optional[Dict]:
        features_dict = {f['feature_name']: f['feature_value'] for f in features}
        
        origin_country = features_dict.get('origin_country')
        
        if origin_country in self.HIGH_RISK_COUNTRIES:
            return {
                'rule_id': self.rule_id,
                'rule_name': self.name,
                'severity': self.severity,
                'score': self.score,
                'evidence': {
                    'origin_country': origin_country,
                    'risk_level': 'HIGH',
                },
                'message': f'Pays d\'origine à risque élevé: {origin_country}',
            }
        
        return None


class UnusualHSCodeRule(Rule):
    """Règle: Code HS inhabituel pour le montant/poids"""
    
    def __init__(self):
        super().__init__(
            rule_id='R003',
            name='Code HS inhabituel',
            severity='MEDIUM',
            score=35
        )
    
    def check(self, case_data: Dict, features: List[Dict]) -> Optional[Dict]:
        features_dict = {f['feature_name']: f['feature_value'] for f in features}
        
        hs_code_2 = features_dict.get('hs_code_digit2')
        amount = features_dict.get('amount_total')
        
        if hs_code_2 is None or amount is None:
            return None
        
        # Règle simplifiée: certains HS codes (ex: 71 = métaux précieux) 
        # avec montants faibles sont suspects
        if hs_code_2 == 71 and amount < 5000:
            return {
                'rule_id': self.rule_id,
                'rule_name': self.name,
                'severity': self.severity,
                'score': self.score,
                'evidence': {
                    'hs_code_digit2': hs_code_2,
                    'amount_total': amount,
                    'expected_minimum': 5000,
                },
                'message': 'Code HS métaux précieux avec montant inhabituel',
            }
        
        return None


class FrequentDeclarantRule(Rule):
    """Règle: Déclarant avec historique suspect"""
    
    def __init__(self):
        super().__init__(
            rule_id='R004',
            name='Déclarant à risque',
            severity='HIGH',
            score=50
        )
    
    def check(self, case_data: Dict, features: List[Dict]) -> Optional[Dict]:
        # Cette règle nécessiterait l'accès à l'historique
        # Pour l'instant, on simule avec les entity_links
        
        # Si on détecte des entités liées multiples, c'est suspect
        entity_links = case_data.get('entity_links', [])
        
        if len(entity_links) > 3:
            return {
                'rule_id': self.rule_id,
                'rule_name': self.name,
                'severity': self.severity,
                'score': self.score,
                'evidence': {
                    'entity_count': len(entity_links),
                    'threshold': 3,
                },
                'message': f'Nombre élevé d\'entités liées: {len(entity_links)}',
            }
        
        return None


class LowPricePerUnitRule(Rule):
    """Règle: Prix unitaire anormalement bas (dumping suspecté)"""
    
    def __init__(self):
        super().__init__(
            rule_id='R005',
            name='Prix unitaire anormalement bas',
            severity='MEDIUM',
            score=45
        )
    
    def check(self, case_data: Dict, features: List[Dict]) -> Optional[Dict]:
        features_dict = {f['feature_name']: f['feature_value'] for f in features}
        
        price_per_unit = features_dict.get('price_per_unit')
        
        if price_per_unit is None:
            return None
        
        # Seuil: moins de 0.5 USD par unité est suspect
        if price_per_unit < 0.5:
            return {
                'rule_id': self.rule_id,
                'rule_name': self.name,
                'severity': self.severity,
                'score': self.score,
                'evidence': {
                    'price_per_unit': price_per_unit,
                    'threshold': 0.5,
                },
                'message': f'Prix unitaire très bas: {price_per_unit} USD',
            }
        
        return None


class RulesEngine:
    """Moteur de règles métier."""
    
    def __init__(self):
        self.rules = [
            HighValueLowWeightRule(),
            SuspiciousOriginCountryRule(),
            UnusualHSCodeRule(),
            FrequentDeclarantRule(),
            LowPricePerUnitRule(),
        ]
    
    def analyze_case(self, case_id: int, case_data: Dict, features: List[Dict]) -> Dict:
        """
        Analyse un case avec toutes les règles.
        
        Returns:
            Résultat avec violations détectées et score total
        """
        violations = []
        total_score = 0
        
        for rule in self.rules:
            violation = rule.check(case_data, features)
            if violation:
                violations.append(violation)
                total_score += violation['score']
        
        # Plafonner le score à 100
        total_score = min(100, total_score)
        
        return {
            'case_id': case_id,
            'algo_source': 'RULES_ENGINE',
            'has_anomaly': len(violations) > 0,
            'violations_count': len(violations),
            'violations': violations,
            'score': total_score,
            'message': f'{len(violations)} règle(s) violée(s)' if violations else 'Toutes les règles respectées',
        }


# Test rapide
if __name__ == '__main__':
    engine = RulesEngine()
    
    # Cas normal
    case_normal = {
        'id': 1,
        'entity_links': [],
    }
    features_normal = [
        {'feature_name': 'amount_total', 'feature_value': 10000},
        {'feature_name': 'weight_kg', 'feature_value': 500},
        {'feature_name': 'price_per_unit', 'feature_value': 20},
        {'feature_name': 'origin_country', 'feature_value': 'FR'},
    ]
    
    # Cas suspect
    case_suspicious = {
        'id': 2,
        'entity_links': [1, 2, 3, 4],  # Beaucoup d'entités
    }
    features_suspicious = [
        {'feature_name': 'amount_total', 'feature_value': 100000},
        {'feature_name': 'weight_kg', 'feature_value': 50},  # Ratio élevé
        {'feature_name': 'price_per_unit', 'feature_value': 0.1},  # Prix très bas
        {'feature_name': 'origin_country', 'feature_value': 'CN'},  # Pays à risque
    ]
    
    print("=== Analyse d'un cas NORMAL ===")
    result_normal = engine.analyze_case(1, case_normal, features_normal)
    print(f"Anomalie: {result_normal['has_anomaly']}")
    print(f"Score: {result_normal['score']}")
    print(f"Violations: {result_normal['violations_count']}")
    print(f"Message: {result_normal['message']}")
    
    print("\n=== Analyse d'un cas SUSPECT ===")
    result_suspicious = engine.analyze_case(2, case_suspicious, features_suspicious)
    print(f"Anomalie: {result_suspicious['has_anomaly']}")
    print(f"Score: {result_suspicious['score']}")
    print(f"Violations: {result_suspicious['violations_count']}")
    print(f"Message: {result_suspicious['message']}")
    
    if result_suspicious['violations']:
        print("\nDétail des violations:")
        for v in result_suspicious['violations']:
            print(f"  - [{v['rule_id']}] {v['rule_name']} ({v['severity']})")
            print(f"    {v['message']}")
