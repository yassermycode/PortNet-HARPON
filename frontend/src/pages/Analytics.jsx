import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Layout from '../components/layout/Layout';
import { 
  Activity, 
  TrendingUp, 
  Zap, 
  Shield, 
  AlertTriangle,
  CheckCircle,
  BarChart3,
  Brain,
  Database,
  FileSearch
} from 'lucide-react';

const Analytics = () => {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Algorithmes disponibles dans le backend
  const algorithms = [
    {
      id: 1,
      name: 'Analyse de similarité documentaire',
      type: 'SIMILARITY',
      description: 'Détecte les documents similaires ou dupliqués en utilisant des embeddings et la distance cosinus',
      status: 'active',
      signalsDetected: 142,
      accuracy: 94.5,
      icon: FileSearch,
      color: 'blue',
      techniques: [
        'Embeddings de texte (Sentence Transformers)',
        'Calcul de distance cosinus',
        'Seuil de similarité configurable'
      ]
    },
    {
      id: 2,
      name: 'Détection d\'anomalies',
      type: 'ANOMALY',
      description: 'Identifie les comportements inhabituels dans les patterns de déclaration',
      status: 'active',
      signalsDetected: 87,
      accuracy: 89.2,
      icon: Activity,
      color: 'purple',
      techniques: [
        'Isolation Forest',
        'Z-score pour variables numériques',
        'Analyse de distribution'
      ]
    },
    {
      id: 3,
      name: 'Analyse de réseau d\'entités',
      type: 'NETWORK',
      description: 'Détecte les liens suspects entre importateurs, transporteurs et déclarants',
      status: 'active',
      signalsDetected: 63,
      accuracy: 91.7,
      icon: Shield,
      color: 'red',
      techniques: [
        'Analyse de graphes',
        'Détection de communautés',
        'Score de centralité'
      ]
    },
    {
      id: 4,
      name: 'Analyse de features numériques',
      type: 'FEATURE',
      description: 'Évalue les valeurs déclarées (montants, quantités, poids) pour détecter les incohérences',
      status: 'active',
      signalsDetected: 156,
      accuracy: 87.3,
      icon: TrendingUp,
      color: 'green',
      techniques: [
        'Régression linéaire',
        'Détection d\'outliers',
        'Validation de cohérence'
      ]
    },
    {
      id: 5,
      name: 'Classification ML',
      type: 'ML_CLASSIFIER',
      description: 'Modèle de machine learning entraîné pour classifier automatiquement le risque',
      status: 'training',
      signalsDetected: 0,
      accuracy: 0,
      icon: Brain,
      color: 'indigo',
      techniques: [
        'Random Forest',
        'Gradient Boosting',
        'Feature engineering automatique'
      ]
    },
    {
      id: 6,
      name: 'Analyse de séries temporelles',
      type: 'TEMPORAL',
      description: 'Détecte les patterns temporels suspects dans les déclarations',
      status: 'beta',
      signalsDetected: 34,
      accuracy: 82.1,
      icon: BarChart3,
      color: 'orange',
      techniques: [
        'Analyse de tendances',
        'Détection de saisonnalité',
        'Prédiction de valeurs futures'
      ]
    }
  ];

  const getStatusBadge = (status) => {
    const badges = {
      active: { text: 'Actif', color: 'bg-green-100 text-green-800' },
      training: { text: 'En formation', color: 'bg-yellow-100 text-yellow-800' },
      beta: { text: 'Beta', color: 'bg-blue-100 text-blue-800' },
      inactive: { text: 'Inactif', color: 'bg-gray-100 text-gray-800' }
    };
    return badges[status] || badges.inactive;
  };

  const getColorClasses = (color) => {
    const colors = {
      blue: 'border-blue-500 bg-blue-50',
      purple: 'border-purple-500 bg-purple-50',
      red: 'border-red-500 bg-red-50',
      green: 'border-green-500 bg-green-50',
      indigo: 'border-indigo-500 bg-indigo-50',
      orange: 'border-orange-500 bg-orange-50'
    };
    return colors[color] || 'border-gray-500 bg-gray-50';
  };

  const getIconColor = (color) => {
    const colors = {
      blue: 'text-blue-600',
      purple: 'text-purple-600',
      red: 'text-red-600',
      green: 'text-green-600',
      indigo: 'text-indigo-600',
      orange: 'text-orange-600'
    };
    return colors[color] || 'text-gray-600';
  };

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Algorithmes & Techniques</h1>
          <p className="text-gray-600 mt-1">
            Vue d'ensemble des algorithmes de détection de fraude
          </p>
        </div>

        {/* Global Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Algorithmes actifs</p>
                <p className="text-3xl font-bold text-gray-900 mt-1">
                  {algorithms.filter(a => a.status === 'active').length}
                </p>
              </div>
              <Zap className="text-green-600" size={32} />
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Signaux détectés</p>
                <p className="text-3xl font-bold text-gray-900 mt-1">
                  {algorithms.reduce((sum, a) => sum + a.signalsDetected, 0)}
                </p>
              </div>
              <AlertTriangle className="text-red-600" size={32} />
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Précision moyenne</p>
                <p className="text-3xl font-bold text-gray-900 mt-1">
                  {(algorithms.filter(a => a.accuracy > 0).reduce((sum, a) => sum + a.accuracy, 0) / algorithms.filter(a => a.accuracy > 0).length).toFixed(1)}%
                </p>
              </div>
              <CheckCircle className="text-blue-600" size={32} />
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">En développement</p>
                <p className="text-3xl font-bold text-gray-900 mt-1">
                  {algorithms.filter(a => a.status === 'training' || a.status === 'beta').length}
                </p>
              </div>
              <Brain className="text-purple-600" size={32} />
            </div>
          </div>
        </div>

        {/* Algorithms List */}
        <div className="space-y-4">
          <h2 className="text-2xl font-bold text-gray-900">Catalogue des algorithmes</h2>
          
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {algorithms.map(algo => {
              const Icon = algo.icon;
              const statusBadge = getStatusBadge(algo.status);
              
              return (
                <div 
                  key={algo.id} 
                  className={`card border-l-4 ${getColorClasses(algo.color)} hover:shadow-lg transition`}
                >
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex items-start space-x-3">
                      <div className={`p-2 rounded-lg bg-white`}>
                        <Icon className={getIconColor(algo.color)} size={24} />
                      </div>
                      <div className="flex-1">
                        <h3 className="text-lg font-bold text-gray-900">{algo.name}</h3>
                        <p className="text-sm text-gray-600 mt-1">{algo.description}</p>
                      </div>
                    </div>
                    <span className={`px-3 py-1 rounded-full text-xs font-medium ${statusBadge.color}`}>
                      {statusBadge.text}
                    </span>
                  </div>

                  {/* Metrics */}
                  <div className="grid grid-cols-2 gap-4 mb-4">
                    <div className="bg-white rounded-lg p-3">
                      <p className="text-xs text-gray-600">Signaux détectés</p>
                      <p className="text-2xl font-bold text-gray-900">{algo.signalsDetected}</p>
                    </div>
                    <div className="bg-white rounded-lg p-3">
                      <p className="text-xs text-gray-600">Précision</p>
                      <p className="text-2xl font-bold text-gray-900">
                        {algo.accuracy > 0 ? `${algo.accuracy}%` : 'N/A'}
                      </p>
                    </div>
                  </div>

                  {/* Techniques */}
                  <div className="bg-white rounded-lg p-3">
                    <p className="text-xs font-semibold text-gray-700 mb-2">Techniques utilisées:</p>
                    <ul className="space-y-1">
                      {algo.techniques.map((tech, idx) => (
                        <li key={idx} className="text-xs text-gray-600 flex items-start">
                          <span className="text-custom-primary mr-2">•</span>
                          {tech}
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Type badge */}
                  <div className="mt-3 pt-3 border-t border-gray-200">
                    <span className="text-xs text-gray-500">
                      Type: <span className="font-medium text-gray-700">{algo.type}</span>
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Pipeline Info */}
        <div className="card bg-gradient-to-r from-custom-primary to-primary-700 text-white">
          <div className="flex items-start space-x-4">
            <Database size={48} className="flex-shrink-0" />
            <div>
              <h3 className="text-xl font-bold mb-2">Pipeline d'analyse automatique</h3>
              <p className="text-primary-100 mb-4">
                Chaque dossier passe par plusieurs étapes d'analyse automatisée utilisant les algorithmes ci-dessus. 
                Les signaux détectés contribuent au score global de risque.
              </p>
              <div className="flex flex-wrap gap-2">
                <span className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm">
                  1. Extraction de features
                </span>
                <span className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm">
                  2. Analyse de similarité
                </span>
                <span className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm">
                  3. Détection d'anomalies
                </span>
                <span className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm">
                  4. Analyse de réseau
                </span>
                <span className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm">
                  5. Calcul du score
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Analytics;
