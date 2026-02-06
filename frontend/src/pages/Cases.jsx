import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
<<<<<<< HEAD
import { casesAPI, documentsAPI } from '../api/apiClient';
import { useAuth } from '../hooks/useAuth';
import { toast } from 'react-toastify';
import { generateCaseReport } from '../services/pdfGenerator';
import Layout from '../components/layout/Layout';
import CaseList from '../components/cases/CaseList';
import CreateCaseForm from '../components/cases/CreateCaseForm';
import { Plus, AlertCircle, FileDown } from 'lucide-react';
=======
import { casesAPI } from '../api/apiClient';
import { useAuth } from '../hooks/useAuth';
import Layout from '../components/layout/Layout';
import CaseList from '../components/cases/CaseList';
import CreateCaseForm from '../components/cases/CreateCaseForm';
import { Plus, AlertCircle } from 'lucide-react';
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
import { ROLES } from '../utils/constants';

const Cases = () => {
  const [cases, setCases] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [createLoading, setCreateLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const { user } = useAuth();
  const navigate = useNavigate();

  // Permissions: Admin et Analyst peuvent créer
  const canCreate = user?.role === ROLES.ADMIN || user?.role === ROLES.ANALYST;

  useEffect(() => {
    fetchCases();
  }, []);

  const fetchCases = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await casesAPI.getAll();
      setCases(response.data.cases || []);
    } catch (error) {
      console.error('Erreur lors du chargement des dossiers:', error);
      setError('Impossible de charger les dossiers. Veuillez réessayer.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateCase = async (formData) => {
    setCreateLoading(true);
    
    console.log('🔵 DÉBUT DE CRÉATION');
    console.log('🔵 FormData à envoyer:', formData);
    
    try {
      const response = await casesAPI.create(formData);
      
      console.log('✅ SUCCÈS - Réponse complète:', response);
      console.log('✅ Data:', response.data);
      
      // Ajouter à la liste
      setCases(prev => [response.data, ...prev]);
      
      // Fermer le modal
      setShowCreateForm(false);
      
<<<<<<< HEAD
      toast.success(`Dossier ${response.data.case_number} créé avec succès !`);
=======
      alert(`✅ Dossier ${response.data.case_number} créé avec succès !`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      
      // Recharger pour être sûr
      fetchCases();
      
    } catch (error) {
      console.error('❌ ERREUR COMPLÈTE:', error);
      console.error('❌ Response:', error.response);
      console.error('❌ Data:', error.response?.data);
      console.error('❌ Status:', error.response?.status);
      
      let errorMessage = 'Erreur inconnue';
      
      if (error.response) {
        if (error.response.data?.detail) {
          errorMessage = error.response.data.detail;
        } else if (error.response.data?.message) {
          errorMessage = error.response.data.message;
        } else {
          errorMessage = `Erreur ${error.response.status}: ${error.response.statusText}`;
        }
      } else if (error.request) {
        errorMessage = 'Aucune réponse du serveur. Vérifiez que le backend est démarré sur http://127.0.0.1:8000';
      } else {
        errorMessage = error.message;
      }
      
<<<<<<< HEAD
      toast.error(errorMessage);
=======
      alert(`❌ ERREUR: ${errorMessage}`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    } finally {
      setCreateLoading(false);
    }
  };

  const handleCaseClick = (caseId) => {
    navigate(`/cases/${caseId}`);
  };

<<<<<<< HEAD
  const handleQuickExport = async (caseId, event) => {
    // Empêcher la navigation vers le détail du dossier
    if (event) {
      event.stopPropagation();
    }
    
    try {
      console.log('📄 Export rapide du dossier', caseId);
      
      toast.info('Chargement des données...');
      
      // Charger les détails du dossier
      const caseResponse = await casesAPI.getById(caseId);
      const caseData = caseResponse.data;
      
      // Charger les documents
      const docsResponse = await documentsAPI.getAll(caseId);
      const documents = docsResponse.data.documents || [];
      
      // Générer le PDF
      const filename = generateCaseReport(caseData, documents);
      
      toast.success(`PDF généré : ${filename}`);
    } catch (error) {
      console.error('❌ Erreur export:', error);
      toast.error('Erreur lors de l\'export PDF');
    }
  };

=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Dossiers</h1>
            <p className="text-gray-600 mt-1">Gestion des dossiers de fraude douanière</p>
          </div>

          {canCreate && (
            <button
              onClick={() => setShowCreateForm(true)}
              className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition duration-200 flex items-center space-x-2"
            >
              <Plus size={20} />
              <span>Nouveau dossier</span>
            </button>
          )}
        </div>

        {/* Error */}
        {error && (
          <div className="card bg-red-50 border border-red-200">
            <div className="flex items-start space-x-2">
              <AlertCircle className="text-red-600 mt-0.5" size={20} />
              <div>
                <p className="text-red-800 font-medium">Erreur</p>
                <p className="text-red-700 text-sm">{error}</p>
                <button
                  onClick={fetchCases}
                  className="mt-2 text-sm text-red-600 hover:text-red-800 font-medium underline"
                >
                  Réessayer
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Cases List */}
        <CaseList 
          cases={cases} 
          onCaseClick={handleCaseClick}
<<<<<<< HEAD
          onExportPDF={handleQuickExport}
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
          loading={loading}
        />

        {/* Create Form Modal */}
        {showCreateForm && (
          <CreateCaseForm
            onClose={() => setShowCreateForm(false)}
            onSubmit={handleCreateCase}
            loading={createLoading}
          />
        )}
      </div>
    </Layout>
  );
};

export default Cases;
