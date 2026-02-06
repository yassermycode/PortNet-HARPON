import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { casesAPI } from '../api/apiClient';
import Layout from '../components/layout/Layout';
import { FileText, AlertTriangle, Shield, TrendingUp } from 'lucide-react';

const Archives = () => {
  const [cases, setCases] = useState([]);
  const [stats, setStats] = useState({ aucun_risque: 0, signale: 0, anomalie: 0 });
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchArchives();
  }, [activeCategory]);

  const fetchArchives = async () => {
    try {
      setLoading(true);
      const params = activeCategory ? { category: activeCategory } : {};
      const response = await casesAPI.getArchives(params);
      setCases(response.data.cases);
      setStats(response.data.stats);
    } catch (error) {
      console.error('Erreur récupération archives:', error);
    } finally {
      setLoading(false);
    }
  };

  const getCategoryBadge = (riskScore) => {
    if (riskScore < 20) {
      return (
        <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-xs font-bold">
          AUCUN RISQUE
        </span>
      );
    } else if (riskScore < 75) {
      return (
        <span className="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full text-xs font-bold">
          SIGNALE
        </span>
      );
    } else {
      return (
        <span className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-xs font-bold">
          ANOMALIE
        </span>
      );
    }
  };

  return (
    <Layout>
      <div className="space-y-6">
        {/* En-tête */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Archives</h1>
          <p className="text-gray-600 mt-1">
            Dossiers approuvés et archivés
          </p>
        </div>

        {/* Statistiques */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div
            onClick={() => setActiveCategory(null)}
            className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
              activeCategory === null
                ? 'border-blue-500 bg-blue-50'
                : 'border-gray-200 hover:border-blue-300'
            }`}
          >
            <div className="flex items-center space-x-3 mb-2">
              <FileText size={24} className="text-blue-600" />
              <div className="text-2xl font-bold text-gray-900">
                {stats.aucun_risque + stats.signale + stats.anomalie}
              </div>
            </div>
            <div className="text-sm text-gray-600">Total archives</div>
          </div>

          <div
            onClick={() => setActiveCategory('AUCUN_RISQUE')}
            className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
              activeCategory === 'AUCUN_RISQUE'
                ? 'border-green-500 bg-green-50'
                : 'border-gray-200 hover:border-green-300'
            }`}
          >
            <div className="flex items-center space-x-3 mb-2">
              <TrendingUp size={24} className="text-green-600" />
              <div className="text-2xl font-bold text-green-600">
                {stats.aucun_risque}
              </div>
            </div>
            <div className="text-sm text-gray-600">Aucun risque</div>
          </div>

          <div
            onClick={() => setActiveCategory('SIGNALE')}
            className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
              activeCategory === 'SIGNALE'
                ? 'border-yellow-500 bg-yellow-50'
                : 'border-gray-200 hover:border-yellow-300'
            }`}
          >
            <div className="flex items-center space-x-3 mb-2">
              <AlertTriangle size={24} className="text-yellow-600" />
              <div className="text-2xl font-bold text-yellow-600">
                {stats.signale}
              </div>
            </div>
            <div className="text-sm text-gray-600">Signalés</div>
          </div>

          <div
            onClick={() => setActiveCategory('ANOMALIE')}
            className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
              activeCategory === 'ANOMALIE'
                ? 'border-red-500 bg-red-50'
                : 'border-gray-200 hover:border-red-300'
            }`}
          >
            <div className="flex items-center space-x-3 mb-2">
              <Shield size={24} className="text-red-600" />
              <div className="text-2xl font-bold text-red-600">
                {stats.anomalie}
              </div>
            </div>
            <div className="text-sm text-gray-600">Anomalies</div>
          </div>
        </div>

        {/* Filtre actif */}
        {activeCategory && (
          <div className="flex items-center space-x-2 p-3 bg-blue-50 rounded-lg border border-blue-200">
            <span className="text-sm text-gray-600">Filtre actif:</span>
            <span className={`px-3 py-1 rounded-full text-xs font-bold ${
              activeCategory === 'AUCUN_RISQUE' ? 'bg-green-100 text-green-800' :
              activeCategory === 'SIGNALE' ? 'bg-yellow-100 text-yellow-800' :
              'bg-red-100 text-red-800'
            }`}>
              {activeCategory === 'AUCUN_RISQUE' ? 'Aucun risque' :
               activeCategory === 'SIGNALE' ? 'Signalé' :
               'Anomalie'}
            </span>
            <button
              onClick={() => setActiveCategory(null)}
              className="text-xs text-blue-600 hover:text-blue-800 ml-auto"
            >
              Réinitialiser
            </button>
          </div>
        )}

        {/* Liste des dossiers */}
        {loading ? (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
            <p className="text-gray-600 mt-4">Chargement des archives...</p>
          </div>
        ) : cases.length === 0 ? (
          <div className="text-center py-12 bg-gray-50 rounded-lg">
            <FileText size={48} className="mx-auto text-gray-400 mb-4" />
            <p className="text-gray-600">Aucun dossier archivé</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {cases.map(caseItem => (
              <div
                key={caseItem.id}
                onClick={() => navigate(`/cases/${caseItem.id}`)}
                className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-lg transition-shadow cursor-pointer"
              >
                <div className="flex items-start justify-between mb-3">
                  <h3 className="text-lg font-bold text-gray-900">
                    {caseItem.case_number}
                  </h3>
                  {getCategoryBadge(caseItem.risk_score || 0)}
                </div>

                <div className="space-y-2 text-sm">
                  <p className="text-gray-600">
                    <strong>Importateur:</strong> {caseItem.importer_name || 'N/A'}
                  </p>
                  <p className="text-gray-600">
                    <strong>Score de risque:</strong> {caseItem.risk_score || 0}/100
                  </p>
                  <p className="text-gray-600">
                    <strong>Archivé le:</strong>{' '}
                    {new Date(caseItem.updated_at).toLocaleDateString('fr-FR')}
                  </p>
                </div>

                <div className="mt-4 pt-3 border-t border-gray-200">
                  <span className="text-xs text-gray-500">
                    Cliquez pour voir les détails
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </Layout>
  );
};

export default Archives;
