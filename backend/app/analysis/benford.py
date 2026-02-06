"""
Benford's Law Algorithm
Détecte les anomalies dans la distribution des premiers chiffres des montants.
"""

import numpy as np
from typing import Dict, List, Tuple
from scipy.stats import chisquare

BENFORD_DISTRIBUTION = {
    1: 0.301,
    2: 0.176,
    3: 0.125,
    4: 0.097,
    5: 0.079,
    6: 0.067,
    7: 0.058,
    8: 0.051,
    9: 0.046,
}


def get_first_digit(number: float) -> int:
    """Extrait le premier chiffre significatif d'un nombre."""
    if number == 0:
        return 0
    
    abs_number = abs(number)
    while abs_number < 1:
        abs_number *= 10
    while abs_number >= 10:
        abs_number /= 10
    
    return int(abs_number)


def calculate_observed_distribution(amounts: List[float]) -> Dict[int, float]:
    """Calcule la distribution observée des premiers chiffres."""
    if not amounts:
        return {}
    
    first_digits = [get_first_digit(amount) for amount in amounts if amount > 0]
    
    if not first_digits:
        return {}
    
    total = len(first_digits)
    distribution = {}
    
    for digit in range(1, 10):
        count = first_digits.count(digit)
        distribution[digit] = count / total
    
    return distribution


def benford_test(amounts: List[float]) -> Tuple[float, float, bool]:
    """Test de Benford sur une liste de montants."""
    if len(amounts) < 10:
        return 0.0, 1.0, False
    
    observed_dist = calculate_observed_distribution(amounts)
    
    if not observed_dist:
        return 0.0, 1.0, False
    
    observed_frequencies = [observed_dist.get(d, 0) * len(amounts) for d in range(1, 10)]
    expected_frequencies = [BENFORD_DISTRIBUTION[d] * len(amounts) for d in range(1, 10)]
    
    chi2_stat, p_value = chisquare(observed_frequencies, expected_frequencies)
    
    is_anomaly = p_value < 0.05
    
    return chi2_stat, p_value, is_anomaly


def analyze_case_benford(case_id: int, features: List[Dict]) -> Dict:
    """Analyse un case avec Benford's Law."""
    amount_features = [
        f['feature_value'] 
        for f in features 
        if f['feature_name'] in ['amount_total', 'price_per_unit'] 
        and f['feature_value'] is not None 
        and f['feature_value'] > 0
    ]
    
    if not amount_features:
        return {
            'case_id': case_id,
            'algo_source': 'BENFORD_LAW',
            'has_anomaly': False,
            'score': 0,
            'message': 'Pas de montants a analyser',
        }
    
    chi2_stat, p_value, is_anomaly = benford_test(amount_features)
    observed_dist = calculate_observed_distribution(amount_features)
    
    if is_anomaly:
        score = min(100, int((1 - p_value) * 100))
    else:
        score = 0
    
    return {
        'case_id': case_id,
        'algo_source': 'BENFORD_LAW',
        'has_anomaly': is_anomaly,
        'chi2_statistic': round(chi2_stat, 4),
        'p_value': round(p_value, 4),
        'score': score,
        'observed_distribution': {str(k): round(v, 4) for k, v in observed_dist.items()},
        'expected_distribution': {str(k): round(v, 4) for k, v in BENFORD_DISTRIBUTION.items()},
        'message': 'Anomalie detectee dans la distribution des montants' if is_anomaly else 'Distribution conforme',
    }
