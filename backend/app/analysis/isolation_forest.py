"""
Isolation Forest Algorithm
Détecte les outliers multivariés dans les features d'un case.
"""

import numpy as np
from typing import Dict, List, Optional
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def prepare_features_matrix(features_list: List[Dict]) -> tuple:
    """
    Prépare la matrice de features pour l'algorithme.
    
    Args:
        features_list: Liste de dicts avec 'feature_name' et 'feature_value'
    
    Returns:
        (feature_matrix, feature_names)
    """
    if not features_list:
        return np.array([]), []
    
    numerical_features = [
        'amount_total',
        'weight_kg',
        'price_per_unit',
        'hs_code_digit2',
        'hs_code_digit4',
        'container_count',
    ]
    
    features_dict = {f['feature_name']: f['feature_value'] for f in features_list}
    
    values = []
    selected_features = []
    
    for feat_name in numerical_features:
        if feat_name in features_dict and features_dict[feat_name] is not None:
            values.append(float(features_dict[feat_name]))
            selected_features.append(feat_name)
    
    if not values:
        return np.array([]), []
    
    return np.array(values).reshape(1, -1), selected_features


def train_isolation_forest(all_features: List[List[Dict]], contamination: float = 0.1):
    """
    Entraîne un modèle Isolation Forest sur un ensemble de cases.
    """
    all_matrices = []
    feature_names = None
    
    for features in all_features:
        matrix, feat_names = prepare_features_matrix(features)
        if matrix.size > 0:
            all_matrices.append(matrix[0])
            if feature_names is None:
                feature_names = feat_names
    
    if not all_matrices:
        return None, None, []
    
    X = np.array(all_matrices)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = IsolationForest(
        contamination=contamination,
        random_state=42,
        n_estimators=100,
    )
    model.fit(X_scaled)
    
    return model, scaler, feature_names


def analyze_case_isolation_forest(
    case_id: int,
    features: List[Dict],
    model: Optional[IsolationForest] = None,
    scaler: Optional[StandardScaler] = None,
    feature_names: Optional[List[str]] = None,
) -> Dict:
    """
    Analyse un case avec Isolation Forest.
    """
    matrix, feat_names = prepare_features_matrix(features)
    
    if matrix.size == 0:
        return {
            'case_id': case_id,
            'algo_source': 'ISOLATION_FOREST',
            'has_anomaly': False,
            'score': 0,
            'message': 'Pas de features numeriques disponibles',
        }
    
    if model is None or scaler is None:
        values = matrix[0]
        z_scores = np.abs((values - np.mean(values)) / (np.std(values) + 1e-10))
        max_z_score = float(np.max(z_scores))
        
        is_anomaly = max_z_score > 3
        score = min(100, int(max_z_score * 20))
        
        return {
            'case_id': case_id,
            'algo_source': 'ISOLATION_FOREST',
            'has_anomaly': is_anomaly,
            'max_z_score': round(max_z_score, 4),
            'score': score,
            'features_analyzed': feat_names,
            'message': 'Outlier detecte' if is_anomaly else 'Valeurs normales',
        }
    
    try:
        X_scaled = scaler.transform(matrix)
        prediction = model.predict(X_scaled)[0]
        anomaly_score = model.decision_function(X_scaled)[0]
        
        is_anomaly = prediction == -1
        
        score = 0
        if is_anomaly:
            score = min(100, int(abs(anomaly_score) * 200))
        
        return {
            'case_id': case_id,
            'algo_source': 'ISOLATION_FOREST',
            'has_anomaly': is_anomaly,
            'anomaly_score': round(float(anomaly_score), 4),
            'score': score,
            'features_analyzed': feature_names or feat_names,
            'message': 'Outlier multidimensionnel detecte' if is_anomaly else 'Comportement normal',
        }
    except Exception as e:
        return {
            'case_id': case_id,
            'algo_source': 'ISOLATION_FOREST',
            'has_anomaly': False,
            'score': 0,
            'error': str(e),
            'message': 'Erreur lors de analyse',
        }


if __name__ == '__main__':
    normal_cases = [
        [
            {'feature_name': 'amount_total', 'feature_value': 10000},
            {'feature_name': 'weight_kg', 'feature_value': 500},
            {'feature_name': 'price_per_unit', 'feature_value': 20},
        ],
        [
            {'feature_name': 'amount_total', 'feature_value': 12000},
            {'feature_name': 'weight_kg', 'feature_value': 600},
            {'feature_name': 'price_per_unit', 'feature_value': 20},
        ],
        [
            {'feature_name': 'amount_total', 'feature_value': 9500},
            {'feature_name': 'weight_kg', 'feature_value': 475},
            {'feature_name': 'price_per_unit', 'feature_value': 20},
        ],
    ]
    
    suspicious_case = [
        {'feature_name': 'amount_total', 'feature_value': 100000},
        {'feature_name': 'weight_kg', 'feature_value': 50},
        {'feature_name': 'price_per_unit', 'feature_value': 2000},
    ]
    
    print("Entrainement du modele sur les cas normaux...")
    model, scaler, feature_names = train_isolation_forest(normal_cases, contamination=0.1)
    
    print("\nAnalyse d'un cas normal:")
    result_normal = analyze_case_isolation_forest(1, normal_cases[0], model, scaler, feature_names)
    print(f"  Anomalie: {result_normal['has_anomaly']}, Score: {result_normal['score']}")
    print(f"  Message: {result_normal['message']}")
    
    print("\nAnalyse d'un cas suspect:")
    result_suspicious = analyze_case_isolation_forest(2, suspicious_case, model, scaler, feature_names)
    print(f"  Anomalie: {result_suspicious['has_anomaly']}, Score: {result_suspicious['score']}")
    print(f"  Message: {result_suspicious['message']}")
