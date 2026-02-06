import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { casesAPI } from '../api/apiClient';
import Layout from '../components/layout/Layout';
<<<<<<< HEAD
import containerBg from '../assets/container-bg.jpeg';
import StatsCard from '../components/dashboard/StatsCard';
import BarChart from '../components/charts/BarChart';
import PieChart from '../components/charts/PieChart';
import LineChart from '../components/charts/LineChart';
import { Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from 'chart.js';
import { FolderOpen, AlertTriangle, CheckCircle, Clock, Shield, TrendingUp, Activity } from 'lucide-react';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

=======
import StatsCard from '../components/dashboard/StatsCard';
import { FolderOpen, AlertTriangle, CheckCircle, Clock, Shield, TrendingUp, Activity } from 'lucide-react';

>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
const Dashboard = () => {
  const [stats, setStats] = useState({
    total_cases: 0,
    open_cases: 0,
    in_progress_cases: 0,
    closed_cases: 0,
    archived_cases: 0
  });
<<<<<<< HEAD
  const [riskDistribution, setRiskDistribution] = useState(null);
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  const [recentCases, setRecentCases] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchStats();
    fetchRecentCases();
<<<<<<< HEAD
    fetchRiskDistribution();
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  }, []);

  const fetchStats = async () => {
    setLoading(true);
    try {
      console.log('🔵 Chargement des statistiques...');
      const response = await casesAPI.getStats();
      console.log('✅ Stats reçues:', response.data);
      setStats(response.data);
    } catch (error) {
      console.error('❌ Erreur lors du chargement des stats:', error);
      // Garder les stats à 0 en cas d'erreur
    } finally {
      setLoading(false);
    }
  };

  const fetchRecentCases = async () => {
    try {
      console.log('🔵 Chargement des dossiers récents...');
      const response = await casesAPI.getAll({ limit: 5 });
      console.log('✅ Dossiers récents:', response.data);
      setRecentCases(response.data.cases || []);
    } catch (error) {
      console.error('❌ Erreur lors du chargement des dossiers récents:', error);
      setRecentCases([]);
    }
  };

<<<<<<< HEAD
  const fetchRiskDistribution = async () => {
    try {
      console.log('🔵 Chargement de la distribution des risques...');
      const response = await casesAPI.getRiskDistribution();
      console.log('✅ Distribution des risques reçue:', response.data);
      setRiskDistribution(response.data);
    } catch (error) {
      console.error('❌ Erreur chargement distribution risques:', error);
    }
  };

=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  if (loading) {
    return (
      <Layout>
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
        </div>
      </Layout>
    );
  }

  return (
<<<<<<< HEAD
    <Layout fullWidth>
      <div 
        className="relative min-h-screen w-screen ml-[calc(-50vw+50%)]"
        style={{
          backgroundImage: `url(${containerBg})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
          backgroundAttachment: 'fixed',
        }}
      >
        {/* Contenu du dashboard au-dessus de l'image */}
        <div className="relative z-10 p-6">
          <div className="space-y-6">
        {/* Header */}
        <div className="bg-white/90 dark:bg-gray-800/90 backdrop-blur-md rounded-lg p-6 mb-6 shadow-2xl" style={{ borderWidth: '2px', borderColor: 'rgb(35, 42, 86)' }}>
          <h1 className="text-4xl font-bold text-white mb-2">
            Dashboard PortNet HARPON
          </h1>
          <p className="text-gray-600 dark:text-gray-400">
            Vue d'ensemble des dossiers de fraude douanière
          </p>
        </div>

        {/* Stats Grid */}
        {/* Stats supprimées */}

        {/* Risk Level Distribution */}
        {/* Risk Level Distribution supprimée */}

        {/* Section Graphiques */}
        <div className="mt-8">
          <h2 className="text-2xl font-bold text-white mb-6">Visualisation des données</h2>
          
          {/* Graphique 1 : Évolution dans le temps */}
          <div className="bg-white/95 dark:bg-gray-800/95 backdrop-blur-md rounded-lg border border-gray-200 dark:border-gray-700 shadow-xl p-6 mb-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-bold text-white">Évolution des dossiers (7 derniers jours)</h3>
              <button
                onClick={fetchStats}
                className="px-3 py-1 text-white rounded-lg text-sm transition-colors"
                style={{ backgroundColor: 'rgb(35, 42, 86)' }}
                onMouseEnter={(e) => e.target.style.backgroundColor = 'rgb(30, 37, 76)'}
                onMouseLeave={(e) => e.target.style.backgroundColor = 'rgb(35, 42, 86)'}
              >
                Actualiser
              </button>
            </div>
            <LineChart
              title=""
              height={300}
              data={{
                labels: ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'],
                datasets: [
                  {
                    label: 'Nouveaux dossiers',
                    data: [12, 19, 15, 25, 22, 18, 20],
                    fill: true,
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    borderColor: 'rgb(59, 130, 246)',
                    borderWidth: 2,
                    tension: 0.4,
                  },
                ],
              }}
            />
          </div>
          
          {/* Diagramme de répartition des risques */}
          <div className="bg-white/95 dark:bg-gray-800/95 backdrop-blur-md rounded-lg border border-gray-200 dark:border-gray-700 shadow-xl p-6 mb-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-bold text-gray-900 dark:text-gray-100 flex items-center">
                Répartition des Dossiers Analysés par Niveau de Risque
              </h3>
              <button
                onClick={fetchRiskDistribution}
                className="px-3 py-1 text-white rounded-lg text-sm transition-colors"
                style={{ backgroundColor: 'rgb(35, 42, 86)' }}
                onMouseEnter={(e) => e.target.style.backgroundColor = 'rgb(30, 37, 76)'}
                onMouseLeave={(e) => e.target.style.backgroundColor = 'rgb(35, 42, 86)'}
              >
                Actualiser
              </button>
            </div>

            {riskDistribution && riskDistribution.total > 0 ? (
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* Graphique */}
                <div className="flex items-center justify-center">
                  <div style={{ height: '300px', width: '300px' }}>
                    <Pie
                      data={{
                        labels: ['Fiable', 'Signalé', 'Anomalie'],
                        datasets: [
                          {
                            label: 'Nombre de dossiers',
                            data: [
                              riskDistribution.fiable.count,
                              riskDistribution.signale.count,
                              riskDistribution.anomalie.count,
                            ],
                            backgroundColor: [
                              'rgba(16, 185, 129, 0.8)',   // Vert
                              'rgba(245, 158, 11, 0.8)',   // Orange
                              'rgba(239, 68, 68, 0.8)',    // Rouge
                            ],
                            borderColor: [
                              'rgb(16, 185, 129)',
                              'rgb(245, 158, 11)',
                              'rgb(239, 68, 68)',
                            ],
                            borderWidth: 2,
                          },
                        ],
                      }}
                      options={{
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {
                          legend: {
                            position: 'bottom',
                            labels: {
                              padding: 15,
                              font: { size: 12, weight: 'bold' },
                              color: '#ffffff',
                              generateLabels: (chart) => {
                                const data = chart.data;
                                if (data.labels.length && data.datasets.length) {
                                  return data.labels.map((label, i) => {
                                    const value = data.datasets[0].data[i];
                                    const total = data.datasets[0].data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return {
                                      text: `${label}: ${value} (${percentage}%)`,
                                      fillStyle: data.datasets[0].backgroundColor[i],
                                      strokeStyle: data.datasets[0].borderColor[i],
                                      lineWidth: 2,
                                      fontColor: '#ffffff',
                                      hidden: false,
                                      index: i,
                                    };
                                  });
                                }
                                return [];
                              },
                            },
                          },
                          tooltip: {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)',
                            titleFont: { size: 14, weight: 'bold' },
                            bodyFont: { size: 13 },
                            padding: 12,
                            callbacks: {
                              label: function (context) {
                                const label = context.label || '';
                                const value = context.parsed || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: ${value} dossiers (${percentage}%)`;
                              },
                            },
                          },
                        },
                      }}
                    />
                  </div>
                </div>

                {/* Statistiques détaillées */}
                <div className="space-y-4">
                  {/* Fiable */}
                  <div className="bg-green-50/90 dark:bg-green-900/30 backdrop-blur-md rounded-lg p-4 border-l-4 border-green-500 shadow-lg">
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center space-x-2">
                        <h4 className="font-bold text-white">
                          Fiable
                        </h4>
                      </div>
                      <span className="text-2xl font-bold text-green-700 dark:text-green-300">
                        {riskDistribution.fiable.count}
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <p className="text-xs text-green-700 dark:text-green-300">
                        {riskDistribution.fiable.description}
                      </p>
                      <span className="px-3 py-1 bg-green-200 dark:bg-green-800 text-green-800 dark:text-green-200 text-xs font-bold rounded-full">
                        {riskDistribution.fiable.percentage}%
                      </span>
                    </div>
                  </div>

                  {/* Signalé */}
                  <div className="bg-yellow-50/90 dark:bg-yellow-900/30 backdrop-blur-md rounded-lg p-4 border-l-4 border-yellow-500 shadow-lg">
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center space-x-2">
                        <h4 className="font-bold text-white">
                          Signalé
                        </h4>
                      </div>
                      <span className="text-2xl font-bold text-yellow-700 dark:text-yellow-300">
                        {riskDistribution.signale.count}
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <p className="text-xs text-yellow-700 dark:text-yellow-300">
                        {riskDistribution.signale.description}
                      </p>
                      <span className="px-3 py-1 bg-yellow-200 dark:bg-yellow-800 text-yellow-800 dark:text-yellow-200 text-xs font-bold rounded-full">
                        {riskDistribution.signale.percentage}%
                      </span>
                    </div>
                  </div>

                  {/* Anomalie */}
                  <div className="bg-red-50/90 dark:bg-red-900/30 backdrop-blur-md rounded-lg p-4 border-l-4 border-red-500 shadow-lg">
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center space-x-2">
                        <h4 className="font-bold text-white">
                          Anomalie
                        </h4>
                      </div>
                      <span className="text-2xl font-bold text-red-700 dark:text-red-300">
                        {riskDistribution.anomalie.count}
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <p className="text-xs text-red-700 dark:text-red-300">
                        {riskDistribution.anomalie.description}
                      </p>
                      <span className="px-3 py-1 bg-red-200 dark:bg-red-800 text-red-800 dark:text-red-200 text-xs font-bold rounded-full">
                        {riskDistribution.anomalie.percentage}%
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center py-12 bg-white/95 dark:bg-gray-800/95 backdrop-blur-md rounded-lg shadow-xl">
                <span className="text-6xl mb-4 block">📊</span>
                <p className="text-gray-900 dark:text-gray-100">
                  Aucun dossier analysé pour le moment
                </p>
                <p className="text-sm text-gray-600 dark:text-gray-400 mt-2">
                  Les statistiques s'afficheront après l'analyse des premiers documents
                </p>
              </div>
            )}
          </div>
          {/* Quick Actions */}
          {/* Actions rapides supprimées */}

          {/* Recent Activity */}
          <div className="bg-white/95 dark:bg-gray-800/95 backdrop-blur-md rounded-lg border border-gray-200 dark:border-gray-700 shadow-xl p-6">
            <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-4">Activité récente</h2>
            <p className="text-gray-600 dark:text-gray-400">Aucune activité récente à afficher.</p>
          </div>
        </div>  {/* ferme mt-8 Section Graphiques */}
      </div>  {/* ferme space-y-6 */}
      </div>  {/* ferme relative z-10 p-6 */}
    </div>    {/* ferme relative min-h-[calc(100vh-80px)] avec background maritime */}
=======
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600 mt-1">Vue d'ensemble des dossiers de fraude</p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {/* Total Cases */}
          <div className="card hover:shadow-lg transition">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Total des dossiers</p>
                <p className="text-3xl font-bold text-gray-900 mt-2">
                  {stats.total_cases}
                </p>
              </div>
              <div className="bg-blue-100 p-3 rounded-lg">
                <FolderOpen className="text-blue-600" size={24} />
              </div>
            </div>
          </div>

          {/* Open Cases */}
          <div className="card hover:shadow-lg transition">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Dossiers ouverts</p>
                <p className="text-3xl font-bold text-orange-600 mt-2">
                  {stats.open_cases}
                </p>
              </div>
              <div className="bg-orange-100 p-3 rounded-lg">
                <AlertTriangle className="text-orange-600" size={24} />
              </div>
            </div>
          </div>

          {/* In Progress */}
          <div className="card hover:shadow-lg transition">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">En cours</p>
                <p className="text-3xl font-bold text-yellow-600 mt-2">
                  {stats.in_progress_cases}
                </p>
              </div>
              <div className="bg-yellow-100 p-3 rounded-lg">
                <Clock className="text-yellow-600" size={24} />
              </div>
            </div>
          </div>

          {/* Closed */}
          <div className="card hover:shadow-lg transition">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">Dossiers fermés</p>
                <p className="text-3xl font-bold text-green-600 mt-2">
                  {stats.closed_cases}
                </p>
              </div>
              <div className="bg-green-100 p-3 rounded-lg">
                <CheckCircle className="text-green-600" size={24} />
              </div>
            </div>
          </div>
        </div>

        {/* Risk Level Distribution */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <StatsCard
            title="Risque Critique/Élevé"
            value={stats?.high_risk_cases || 0}
            icon={Shield}
            color="red"
            trend="+5% cette semaine"
          />
          <StatsCard
            title="Risque Moyen"
            value={stats?.medium_risk_cases || 0}
            icon={Activity}
            color="orange"
          />
          <StatsCard
            title="Risque Faible"
            value={stats?.low_risk_cases || 0}
            icon={TrendingUp}
            color="green"
            trend="-3% cette semaine"
          />
        </div>

        {/* Quick Actions */}
        <div className="card">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Actions rapides</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <button
              onClick={() => navigate('/cases')}
              className="p-4 border-2 border-gray-200 rounded-lg hover:border-primary-600 hover:bg-primary-50 transition text-left"
            >
              <FolderOpen className="text-primary-600 mb-2" size={24} />
              <h3 className="font-semibold text-gray-900">Voir tous les dossiers</h3>
              <p className="text-sm text-gray-600 mt-1">Consulter la liste complète des dossiers</p>
            </button>
            
            <button
              onClick={() => navigate('/cases?status=PENDING')}
              className="p-4 border-2 border-gray-200 rounded-lg hover:border-primary-600 hover:bg-primary-50 transition text-left"
            >
              <AlertTriangle className="text-yellow-600 mb-2" size={24} />
              <h3 className="font-semibold text-gray-900">Dossiers en attente</h3>
              <p className="text-sm text-gray-600 mt-1">Voir les dossiers PENDING</p>
            </button>

            <button
              onClick={() => navigate('/cases?status=FLAGGED')}
              className="p-4 border-2 border-gray-200 rounded-lg hover:border-red-600 hover:bg-red-50 transition text-left"
            >
              <Shield className="text-red-600 mb-2" size={24} />
              <h3 className="font-semibold text-gray-900">Dossiers signalés</h3>
              <p className="text-sm text-gray-600 mt-1">Dossiers avec signaux de fraude</p>
            </button>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="card">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Activité récente</h2>
          <p className="text-gray-600">Aucune activité récente à afficher.</p>
        </div>
      </div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    </Layout>
  );
};

export default Dashboard;
