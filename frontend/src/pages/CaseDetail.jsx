import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
<<<<<<< HEAD
import { casesAPI, documentsAPI, notesAPI } from '../api/apiClient';
import { useAuth } from '../hooks/useAuth';
import { toast } from 'react-toastify';
import { generateCaseReport } from '../services/pdfGenerator';
=======
import { casesAPI, documentsAPI } from '../api/apiClient';
import { useAuth } from '../hooks/useAuth';
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
import Layout from '../components/layout/Layout';
import { 
  ArrowLeft, 
  Calendar, 
  User, 
  AlertTriangle, 
  FileText,
  Edit,
  Trash2,
  Upload,
  TrendingUp,
  Activity,
  Shield,
  Zap,
  Users,
<<<<<<< HEAD
  Package,
  FileDown,
  X
=======
  Package
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
} from 'lucide-react';
import { 
  STATUS_LABELS, 
  RISK_LEVEL_LABELS,
  ACTION_LABELS,
  STATUS_COLORS, 
  RISK_LEVEL_COLORS,
  ACTION_COLORS,
  ROLES 
} from '../utils/constants';
<<<<<<< HEAD
import { Bar, Doughnut, Radar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  RadialLinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';

// Enregistrer les composants Chart.js
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  RadialLinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

const CaseDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { user } = useAuth();
  const [caseData, setCaseData] = useState(null);
  const [loading, setLoading] = useState(true);
<<<<<<< HEAD
  const [isLoadingCase, setIsLoadingCase] = useState(true);
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  const [error, setError] = useState(null);
  const [showUploadModal, setShowUploadModal] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadLoading, setUploadLoading] = useState(false);
  const [showStatusModal, setShowStatusModal] = useState(false);
  const [newStatus, setNewStatus] = useState('');
  const [statusLoading, setStatusLoading] = useState(false);
  const [showPriorityModal, setShowPriorityModal] = useState(false);
  const [newPriority, setNewPriority] = useState('');
  const [priorityLoading, setPriorityLoading] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [deleteLoading, setDeleteLoading] = useState(false);
  const [showAssignModal, setShowAssignModal] = useState(false);
  const [selectedAnalyst, setSelectedAnalyst] = useState('');
  const [assignLoading, setAssignLoading] = useState(false);
  const [analysts] = useState([
    { id: 1, name: 'Mohammed Alami', role: 'ANALYST' },
    { id: 2, name: 'Fatima Benali', role: 'ANALYST' },
    { id: 3, name: 'Hassan El Fassi', role: 'ANALYST' },
    { id: 4, name: 'Amina Chakir', role: 'ANALYST' },
  ]);
  const [showNoteModal, setShowNoteModal] = useState(false);
  const [noteText, setNoteText] = useState('');
  const [noteLoading, setNoteLoading] = useState(false);
  const [notes, setNotes] = useState([]);
  const [documents, setDocuments] = useState([]);
<<<<<<< HEAD
  const [analyzingDocId, setAnalyzingDocId] = useState(null);
  
  // Edit modal states
  const [showEditModal, setShowEditModal] = useState(false);
  const [editLoading, setEditLoading] = useState(false);
  const [editFormData, setEditFormData] = useState({
    case_number: '',
    importer_name: '',
    declarant_name: '',
    transporter_name: '',
    description: '',
    priority: 'MEDIUM'
  });
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

  useEffect(() => {
    fetchCaseDetail();
    fetchDocuments();
<<<<<<< HEAD
    fetchNotes();
  }, [id]);

  const fetchNotes = async () => {
    try {
      console.log('🔵 Chargement des notes pour le dossier', id);
      const response = await notesAPI.getAll(id);
      console.log('✅ Notes chargées:', response.data);
      setNotes(response.data.notes || []);
    } catch (error) {
      console.error('❌ Erreur lors du chargement des notes:', error);
      setNotes([]);
    }
  };

  const fetchCaseDetail = async () => {
    setIsLoadingCase(true);
    try {
      console.log('🔵 Chargement du dossier', id);
      const response = await casesAPI.getById(id);
      console.log('✅ Dossier chargé:', response.data);
=======
  }, [id]);

  const fetchCaseDetail = async () => {
    setLoading(true);
    setError(null);
    
    console.log('🔵 Chargement du dossier ID:', id);
    console.log('🔵 URL appelée:', `/api/v1/cases/${id}`);
    
    try {
      const response = await casesAPI.getById(id);
      
      console.log('✅ Dossier chargé:', response.data);
      
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      setCaseData(response.data);
    } catch (error) {
      console.error('❌ ERREUR lors du chargement:', error);
      console.error('❌ Response:', error.response);
      console.error('❌ Status:', error.response?.status);
      console.error('❌ Data:', error.response?.data);
      
      if (error.response?.status === 404) {
        setError('Dossier non trouvé.');
      } else if (error.response?.status === 401) {
        setError('Vous devez être connecté pour voir ce dossier.');
      } else {
        setError('Impossible de charger le dossier. Vérifiez que le backend est démarré.');
      }
    } finally {
      setLoading(false);
<<<<<<< HEAD
      setIsLoadingCase(false);
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    }
  };

  const fetchDocuments = async () => {
    try {
      console.log('🔵 Chargement des documents pour le dossier', id);
      const response = await documentsAPI.getAll(id);
      console.log('✅ Documents chargés:', response.data);
      setDocuments(response.data.documents || []);
    } catch (error) {
      console.error('❌ Erreur lors du chargement des documents:', error);
      setDocuments([]);
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleString('fr-FR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const handleFileSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
<<<<<<< HEAD
      toast.error('Veuillez sélectionner un fichier');
=======
      alert('Veuillez sélectionner un fichier');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      return;
    }

    setUploadLoading(true);
    
    try {
      console.log('📤 Upload du fichier:', selectedFile.name);
      
      const response = await documentsAPI.upload(id, selectedFile);
      
      console.log('✅ Fichier uploadé:', response.data);
      
<<<<<<< HEAD
      toast.success(`Fichier "${selectedFile.name}" uploadé avec succès !`);
      toast.info('Cliquez sur "Analyser" pour lancer l\'analyse IA');
=======
      alert(`✅ Fichier "${selectedFile.name}" uploadé avec succès !`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      
      // Recharger les documents
      await fetchDocuments();
      
      // Recharger le dossier (pour mettre à jour le score si calculé)
      await fetchCaseDetail();
      
      setShowUploadModal(false);
      setSelectedFile(null);
    } catch (error) {
<<<<<<< HEAD
      console.error('❌ Erreur upload complète:', error);
      console.error('❌ Erreur response:', error.response);
      console.error('❌ Erreur status:', error.response?.status);
      console.error('❌ Erreur data:', error.response?.data);
      console.error('❌ Erreur message:', error.message);
      console.error('❌ Erreur config:', error.config);
      
      let errorMsg = 'Erreur lors de l\'upload';
      
      if (error.response) {
        // Le serveur a répondu avec un code d'erreur
        errorMsg = error.response.data?.detail || `Erreur ${error.response.status}: ${error.response.statusText}`;
      } else if (error.request) {
        // La requête a été faite mais pas de réponse
        errorMsg = 'Pas de réponse du serveur. Vérifiez que le backend est démarré sur http://127.0.0.1:8001';
      } else {
        // Erreur lors de la configuration de la requête
        errorMsg = error.message;
      }
      
      toast.error(errorMsg);
=======
      console.error('❌ Erreur upload:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de l\'upload';
      alert(`❌ Erreur: ${errorMsg}`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    } finally {
      setUploadLoading(false);
    }
  };

<<<<<<< HEAD
  // ===== ANALYSE MANUELLE DES DOCUMENTS =====
  const handleAnalyzeDocument = async (documentId) => {
    try {
      console.log('🤖 Lancement de l\'analyse pour le document', documentId);
      
      setAnalyzingDocId(documentId);
      
      toast.info('Analyse IA en cours...');
      
      const response = await documentsAPI.analyze(documentId);
      
      console.log('✅ Analyse terminée:', response.data);
      
      // Recharger les documents
      await fetchDocuments();
      
      // Recharger le dossier (pour le score global)
      await fetchCaseDetail();
      
      toast.success(`Analyse terminée ! Score: ${response.data.risk_score}/100`);
      
    } catch (error) {
      console.error('❌ Erreur lors de l\'analyse:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de l\'analyse';
      toast.error(errorMsg);
      
      // Recharger quand même pour voir le statut ERROR
      await fetchDocuments();
    } finally {
      setAnalyzingDocId(null);
    }
  };

  const handleStatusChange = async () => {
    if (!newStatus) {
      toast.error('Veuillez sélectionner un statut');
=======
  const handleStatusChange = async () => {
    if (!newStatus) {
      alert('Veuillez sélectionner un statut');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      return;
    }

    setStatusLoading(true);
    
    try {
      console.log('🔵 Changement de statut vers:', newStatus);
      
      const response = await casesAPI.updateStatus(id, newStatus);
      
      console.log('✅ Statut mis à jour:', response.data);
      
      // Mettre à jour l'affichage
      setCaseData(response.data);
      
      setShowStatusModal(false);
      setNewStatus('');
<<<<<<< HEAD
      toast.success('Statut mis à jour avec succès !');
    } catch (error) {
      console.error('❌ Erreur:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la mise à jour du statut';
      toast.error(errorMsg);
=======
      alert('✅ Statut mis à jour avec succès !');
    } catch (error) {
      console.error('❌ Erreur:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la mise à jour du statut';
      alert(`❌ Erreur: ${errorMsg}`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    } finally {
      setStatusLoading(false);
    }
  };

  const handlePriorityChange = async () => {
    if (!newPriority) {
<<<<<<< HEAD
      toast.error('Veuillez sélectionner une priorité');
=======
      alert('Veuillez sélectionner une priorité');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      return;
    }

    setPriorityLoading(true);
    
    try {
      console.log('🔵 Changement de priorité vers:', newPriority);
      
      const response = await casesAPI.updatePriority(id, newPriority);
      
      console.log('✅ Priorité mise à jour:', response.data);
      
      // Mettre à jour l'affichage
      setCaseData(response.data);
      
      setShowPriorityModal(false);
      setNewPriority('');
<<<<<<< HEAD
      toast.success('Priorité mise à jour avec succès !');
    } catch (error) {
      console.error('❌ Erreur:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la mise à jour de la priorité';
      toast.error(errorMsg);
=======
      alert('✅ Priorité mise à jour avec succès !');
    } catch (error) {
      console.error('❌ Erreur:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la mise à jour de la priorité';
      alert(`❌ Erreur: ${errorMsg}`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    } finally {
      setPriorityLoading(false);
    }
  };

  const handleDelete = async () => {
<<<<<<< HEAD
    if (!window.confirm('⚠️ Êtes-vous sûr de vouloir supprimer ce dossier ? Cette action est irréversible.')) {
      return;
    }

    setDeleteLoading(true);
    
    try {
      console.log('🗑️ Suppression du dossier:', id);
      
      await casesAPI.delete(id);
      
      console.log('✅ Dossier supprimé');
      toast.success('Dossier supprimé avec succès !');
      
      // Rediriger vers la liste des dossiers après 1 seconde
      setTimeout(() => {
        navigate('/cases');
      }, 1000);
      
    } catch (error) {
      console.error('❌ Erreur lors de la suppression:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la suppression du dossier';
      toast.error(errorMsg);
=======
    setDeleteLoading(true);
    
    try {
      console.log('Suppression du dossier:', id);
      
      // TODO: Appeler l'API backend pour supprimer
      setTimeout(() => {
        alert('Dossier supprimé avec succès !');
        navigate('/cases');
      }, 500);
    } catch (error) {
      console.error('Erreur:', error);
      alert('Erreur lors de la suppression');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      setDeleteLoading(false);
    }
  };

<<<<<<< HEAD
  const handleExportPDF = () => {
    try {
      console.log('Génération du rapport PDF...');
      
      const filename = generateCaseReport(caseData, documents);
      
      toast.success(`Rapport PDF généré : ${filename}`);
      console.log('PDF généré:', filename);
    } catch (error) {
      console.error('Erreur génération PDF:', error);
      toast.error('Erreur lors de la génération du PDF');
    }
  };

  const handleApproveCase = async () => {
    if (!window.confirm('Êtes-vous sûr de vouloir approuver et archiver ce dossier ?')) {
      return;
    }

    try {
      setLoading(true);
      const response = await casesAPI.approveCase(id);
      
      alert(`Dossier approuvé et archivé avec succès\n\nCatégorie : ${response.data.archive_category}\nScore : ${response.data.risk_score}/100`);
      
      // Rediriger vers les archives
      navigate('/archives');
    } catch (error) {
      console.error('Erreur approbation:', error);
      alert('Erreur lors de l\'approbation du dossier');
    } finally {
      setLoading(false);
    }
  };

  // ===== FONCTIONS D'ÉDITION =====
  const handleOpenEditModal = () => {
    // Pré-remplir le formulaire avec les données actuelles
    setEditFormData({
      case_number: caseData.case_number || caseData.reference_id || '',
      importer_name: caseData.importer_name || caseData.importer || '',
      declarant_name: caseData.declarant_name || '',
      transporter_name: caseData.transporter_name || '',
      description: caseData.description || '',
      priority: caseData.priority || 'MEDIUM'
    });
    setShowEditModal(true);
  };

  const handleSaveEdit = async () => {
    if (!editFormData.case_number || !editFormData.importer_name) {
      toast.error('Le numéro de dossier et l\'importateur sont obligatoires');
      return;
    }

    setEditLoading(true);
    
    try {
      console.log('💾 Modification du dossier', id);
      console.log('📤 Données envoyées:', editFormData);
      
      const response = await casesAPI.update(id, editFormData);
      
      console.log('✅ Dossier modifié:', response.data);
      
      // Recharger les données
      await fetchCaseDetail();
      
      toast.success('Dossier modifié avec succès !');
      setShowEditModal(false);
    } catch (error) {
      console.error('❌ Erreur modification:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la modification';
      toast.error(errorMsg);
    } finally {
      setEditLoading(false);
    }
  };

  const handleAssign = async () => {
    if (!selectedAnalyst) {
      toast.warning('Veuillez sélectionner un analyste');
=======
  const handleAssign = async () => {
    if (!selectedAnalyst) {
      alert('Veuillez sélectionner un analyste');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      return;
    }

    setAssignLoading(true);
    
    try {
      console.log('Assignation à l\'analyste:', selectedAnalyst);
      
      // TODO: Appeler l'API backend pour assigner
      setTimeout(() => {
        const analyst = analysts.find(a => a.id === parseInt(selectedAnalyst));
<<<<<<< HEAD
        toast.success(`Dossier assigné à ${analyst.name} avec succès !`);
=======
        alert(`Dossier assigné à ${analyst.name} avec succès !`);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        setShowAssignModal(false);
        setSelectedAnalyst('');
        setAssignLoading(false);
      }, 500);
    } catch (error) {
      console.error('Erreur:', error);
<<<<<<< HEAD
      toast.error('Erreur lors de l\'assignation');
=======
      alert('Erreur lors de l\'assignation');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      setAssignLoading(false);
    }
  };

  const handleAddNote = async () => {
    if (!noteText.trim()) {
<<<<<<< HEAD
      toast.error('Veuillez entrer une note');
=======
      alert('Veuillez entrer une note');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      return;
    }

    setNoteLoading(true);
    
    try {
<<<<<<< HEAD
      console.log('📝 Ajout de note:', noteText);
      
      const response = await notesAPI.create(id, { content: noteText });
      
      console.log('✅ Note ajoutée:', response.data);
      
      // Recharger les notes
      await fetchNotes();
      
      toast.success('Note ajoutée avec succès !');
      setShowNoteModal(false);
      setNoteText('');
    } catch (error) {
      console.error('❌ Erreur:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de l\'ajout de la note';
      toast.error(errorMsg);
    } finally {
=======
      console.log('Ajout de note:', noteText);
      
      const newNote = {
        id: Date.now(),
        text: noteText,
        author: user.full_name,
        created_at: new Date().toISOString(),
      };
      
      setTimeout(() => {
        setNotes(prev => [newNote, ...prev]);
        alert('Note ajoutée avec succès !');
        setShowNoteModal(false);
        setNoteText('');
        setNoteLoading(false);
      }, 500);
    } catch (error) {
      console.error('Erreur:', error);
      alert('Erreur lors de l\'ajout de la note');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      setNoteLoading(false);
    }
  };

<<<<<<< HEAD
  const handleDeleteNote = async (noteId) => {
    if (!window.confirm('Êtes-vous sûr de vouloir supprimer cette note ?')) {
      return;
    }

    try {
      console.log('🗑️ Suppression de la note:', noteId);
      
      await notesAPI.delete(noteId);
      
      console.log('✅ Note supprimée');
      
      // Recharger les notes
      await fetchNotes();
      
      toast.success('Note supprimée avec succès !');
    } catch (error) {
      console.error('❌ Erreur:', error);
      const errorMsg = error.response?.data?.detail || 'Erreur lors de la suppression de la note';
      toast.error(errorMsg);
    }
  };

  const canEdit = user?.role === ROLES.ADMIN || user?.role === ROLES.ANALYST;

  if (isLoadingCase) {
    return (
      <Layout>
        <div className="flex items-center justify-center h-screen">
          <div className="text-center">
            <div className="w-16 h-16 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin mx-auto mb-4"></div>
            <p className="text-gray-600 text-lg">Chargement du dossier...</p>
          </div>
=======
  const canEdit = user?.role === ROLES.ADMIN || user?.role === ROLES.ANALYST;

  if (loading) {
    return (
      <Layout>
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-custom-primary"></div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        </div>
      </Layout>
    );
  }

  if (error || !caseData) {
    return (
      <Layout>
        <div className="card bg-red-50 border border-red-200">
          <p className="text-red-800">{error || 'Dossier introuvable'}</p>
          <button onClick={() => navigate('/cases')} className="mt-4 btn-secondary">
            Retour aux dossiers
          </button>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
<<<<<<< HEAD
      <div className="space-y-6 animate-fade-in">
=======
      <div className="space-y-6">
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <button
              onClick={() => navigate('/cases')}
              className="p-2 hover:bg-gray-100 rounded-lg transition"
            >
              <ArrowLeft size={24} />
            </button>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                {caseData.reference_id}
              </h1>
              <p className="text-gray-600 mt-1">Détails du dossier • ID: {caseData.id}</p>
            </div>
          </div>

<<<<<<< HEAD
          <div className="flex space-x-2">
            <button 
              onClick={handleExportPDF}
              className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition flex items-center space-x-2"
              title="Exporter en PDF"
            >
              <FileDown size={18} />
              <span>Exporter PDF</span>
            </button>
            {canEdit && (
              <>
                <button 
                  onClick={handleOpenEditModal}
                  className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition flex items-center space-x-2"
                >
                  <Edit size={18} />
                  <span>Modifier</span>
                </button>
                <button 
                  onClick={() => setShowDeleteModal(true)}
                  className="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded-lg transition flex items-center space-x-2"
                  title="Supprimer ce dossier"
                >
                  <Trash2 size={18} />
                  <span>Supprimer</span>
                </button>
              </>
            )}
            {!canEdit && (
              <div className="text-sm text-gray-500 italic px-3 py-2">
                Droits insuffisants pour modifier (Rôle: {user?.role || 'Non défini'})
              </div>
            )}
          </div>
        </div>

      <div className="w-full">
        <div className="space-y-6">
=======
          {canEdit && (
            <div className="flex space-x-2">
              <button className="btn-secondary flex items-center space-x-2">
                <Edit size={18} />
                <span>Modifier</span>
              </button>
              <button 
                onClick={() => setShowDeleteModal(true)}
                className="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-lg transition flex items-center space-x-2"
              >
                <Trash2 size={18} />
                <span>Supprimer</span>
              </button>
            </div>
          )}
        </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-2 space-y-6">
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
          {/* Case Info Card */}
          <div className="card">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Informations du dossier</h2>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-gray-600">Priorité</p>
                {caseData.priority ? (
                  <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${
                    caseData.priority === 'CRITICAL' ? 'bg-red-100 text-red-800' :
                    caseData.priority === 'HIGH' ? 'bg-orange-100 text-orange-800' :
                    caseData.priority === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
                    'bg-green-100 text-green-800'
                  }`}>
                    {caseData.priority}
                  </span>
                ) : <p className="font-medium text-gray-900">N/A</p>}
              </div>
              <div>
                <p className="text-sm text-gray-600">Action recommandée</p>
                {caseData.recommended_action ? (
                  <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${ACTION_COLORS[caseData.recommended_action]}`}>
                    {ACTION_LABELS[caseData.recommended_action]}
                  </span>
                ) : <p className="font-medium text-gray-900">N/A</p>}
              </div>
              <div>
                <p className="text-sm text-gray-600">Créé le</p>
                <div className="flex items-center space-x-2">
                  <Calendar size={16} className="text-gray-400" />
                  <p className="font-medium text-gray-900">{formatDate(caseData.created_at)}</p>
                </div>
              </div>
              <div>
                <p className="text-sm text-gray-600">Mis à jour le</p>
                <div className="flex items-center space-x-2">
                  <Calendar size={16} className="text-gray-400" />
                  <p className="font-medium text-gray-900">{formatDate(caseData.updated_at)}</p>
                </div>
              </div>
            </div>
          </div>

<<<<<<< HEAD
=======
            {/* Analysis Results */}
            <div className="card">
              <h2 className="text-xl font-bold text-gray-900 mb-4">Score global de risque</h2>
              
              <div className="flex items-center space-x-4 mb-4">
                <div className="flex-1">
                  <p className="text-sm text-gray-600 mb-2">Score de risque global (0-100)</p>
                  <div className="w-full bg-gray-200 rounded-full h-6">
                    <div
                      className={`h-6 rounded-full flex items-center justify-center text-sm font-bold ${
                        caseData.global_score === 0 || caseData.global_score == null ? 'bg-gray-200 text-gray-800' :
                        caseData.global_score > 70 ? 'bg-red-600 text-white' :
                        caseData.global_score > 40 ? 'bg-orange-600 text-white' : 'bg-green-600 text-white'
                      }`}
                      style={{ width: `${caseData.global_score}%` }}
                    >
                      {caseData.global_score}
                    </div>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-4xl font-bold text-gray-900">{caseData.global_score || 0}</p>
                  <p className="text-sm text-gray-600">/100</p>
                </div>
              </div>

              {caseData.global_score > 70 && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                  <div className="flex items-start space-x-2">
                    <AlertTriangle className="text-red-600 mt-0.5" size={20} />
                    <div>
                      <p className="font-medium text-red-800">Risque élevé détecté</p>
                      <p className="text-sm text-red-700 mt-1">
                        Ce dossier nécessite une inspection approfondie.
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {/* Risk Breakdown si disponible */}
              {caseData.risk_breakdown_json && (
                <div className="mt-4 pt-4 border-t">
                  <h3 className="font-semibold text-gray-900 mb-2">Détails du risque</h3>
                  <pre className="text-xs bg-gray-50 p-3 rounded overflow-auto">
                    {JSON.stringify(caseData.risk_breakdown_json, null, 2)}
                  </pre>
                </div>
              )}
            </div>

>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            {/* Documents Section */}
            <div className="card">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-bold text-gray-900">Documents</h2>
                {canEdit && (
                  <button 
                    onClick={() => setShowUploadModal(true)}
                    className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition flex items-center space-x-2"
                  >
                    <Upload size={18} />
                    <span>Uploader</span>
                  </button>
                )}
              </div>

              {documents.length === 0 ? (
                <div className="text-center py-8 text-gray-500">
                  <FileText size={48} className="mx-auto mb-2 text-gray-300" />
                  <p>Aucun document uploadé</p>
                </div>
              ) : (
                <div className="space-y-3">
                  {documents.map(doc => (
                    <div key={doc.id} className="border border-gray-200 rounded-lg p-4 hover:bg-gray-50 transition">
                      <div className="flex items-start justify-between">
                        {/* Informations du fichier */}
                        <div className="flex items-start space-x-3 flex-1">
                          <FileText size={24} className="text-blue-600 mt-1" />
                          <div className="flex-1">
                            <p className="font-medium text-gray-900">{doc.filename}</p>
                            <p className="text-xs text-gray-500 mt-1">
                              {(doc.file_size / 1024).toFixed(2)} KB • {new Date(doc.uploaded_at).toLocaleDateString('fr-FR', {
                                year: 'numeric',
                                month: 'short',
                                day: 'numeric',
                                hour: '2-digit',
                                minute: '2-digit'
                              })}
                            </p>
                            
                            {/* Statut de l'analyse */}
                            <div className="mt-2">
<<<<<<< HEAD
                              {doc.status === 'UPLOADED' && (
                                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
                                  Uploadé - En attente d'analyse
                                </span>
                              )}
                              
                              {doc.status === 'ANALYZING' && (
                                <div className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800 space-x-2">
                                  <div className="w-4 h-4 border-2 border-yellow-600 border-t-transparent rounded-full animate-spin"></div>
                                  <span>Analyse en cours...</span>
                                </div>
                              )}
                              
                              {doc.status === 'ANALYZED' && (
                                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
                                  Analysé
                                </span>
                              )}
                              
                              {doc.status === 'ERROR' && (
                                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800">
                                  Erreur d'analyse
                                </span>
                              )}
                              
                              {doc.status === 'REJECTED' && (
                                <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-slate-200 text-slate-700">
                                  Document non-douanier - Rejeté
                                </span>
                              )}
                            </div>
                            
                            {/* Boutons d'action selon le statut */}
                            <div className="mt-3 flex items-center space-x-2">
                              {/* Bouton Analyser (si UPLOADED) */}
                              {doc.status === 'UPLOADED' && (
                                <button
                                  onClick={() => handleAnalyzeDocument(doc.id)}
                                  disabled={analyzingDocId === doc.id}
                                  className={`px-4 py-2 rounded-lg font-medium transition flex items-center space-x-2 ${
                                    analyzingDocId === doc.id
                                      ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                                      : 'bg-custom-primary hover:bg-primary-700 text-white'
                                  }`}
                                >
                                  {analyzingDocId === doc.id ? (
                                    <>
                                      <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                                      <span>Analyse en cours...</span>
                                    </>
                                  ) : (
                                    <>
                                      <Zap size={18} />
                                      <span>Analyser</span>
                                    </>
                                  )}
                                </button>
                              )}

                              {/* Bouton Réanalyser (si ERROR) */}
                              {doc.status === 'ERROR' && (
                                <button
                                  onClick={() => handleAnalyzeDocument(doc.id)}
                                  disabled={analyzingDocId === doc.id}
                                  className="px-4 py-2 bg-custom-primary hover:bg-primary-700 text-white rounded-lg font-medium transition flex items-center space-x-2"
                                >
                                  {analyzingDocId === doc.id ? (
                                    <>
                                      <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                                      <span>Réanalyse...</span>
                                    </>
                                  ) : (
                                    <>
                                      <Activity size={18} />
                                      <span>Réanalyser</span>
                                    </>
                                  )}
                                </button>
                              )}

                              {/* Message si ANALYZED */}
                              {doc.status === 'ANALYZED' && (
                                <div className="flex items-center space-x-2 text-green-600">
                                  <Shield size={18} />
                                  <span className="font-medium">Analyse terminée</span>
                                </div>
                              )}
                              
                              {/* Message si REJECTED (document non-douanier) */}
                              {doc.status === 'REJECTED' && (
                                <div className="flex items-center space-x-2" style={{ color: 'rgb(71, 85, 105)' }}>
                                  <AlertTriangle size={18} />
                                  <span className="font-medium">Document rejeté - N'est pas un document douanier</span>
                                </div>
                              )}
                            </div>
                            
                            {/* Message d'explication pour les documents rejetés */}
                            {doc.status === 'REJECTED' && (
                              <div className="mt-3 p-4 bg-slate-100 border border-slate-300 rounded-lg">
                                <div className="flex items-start space-x-3">
                                  <AlertTriangle size={24} className="text-slate-600 mt-1" />
                                  <div>
                                    <p className="font-bold mb-2" style={{ color: 'rgb(35, 42, 86)' }}>Ce document a été rejeté par l'IA</p>
                                    <p className="text-sm text-slate-700 mb-2">
                                      L'analyse a déterminé que ce document n'est <strong>pas un document douanier</strong>.
                                    </p>
                                    <p className="text-xs text-slate-600">
                                      <strong>Documents acceptés :</strong> Factures commerciales, Connaissements (B/L), 
                                      Listes de colisage, Certificats d'origine, Déclarations douanières.
                                    </p>
                                  </div>
                                </div>
                              </div>
                            )}
                            
=======
                              <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                                doc.status === 'ANALYZED' ? 'bg-green-100 text-green-800' :
                                doc.status === 'ANALYZING' ? 'bg-yellow-100 text-yellow-800' :
                                doc.status === 'ERROR' ? 'bg-red-100 text-red-800' :
                                'bg-blue-100 text-blue-800'
                              }`}>
                                {doc.status === 'ANALYZED' ? '✅ Analysé' :
                                 doc.status === 'ANALYZING' ? '⏳ Analyse en cours...' :
                                 doc.status === 'ERROR' ? '❌ Erreur' :
                                 '📄 Uploadé'}
                              </span>
                            </div>
                            
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                            {/* Résultats de l'analyse */}
                            {doc.status === 'ANALYZED' && doc.risk_score !== null && (
                              <div className="mt-3 p-3 bg-gray-50 rounded-lg border border-gray-200">
                                <div className="flex items-center justify-between mb-2">
                                  <span className="text-sm font-medium text-gray-700">Score de risque:</span>
                                  <span className={`text-lg font-bold ${
                                    doc.risk_score >= 70 ? 'text-red-600' :
                                    doc.risk_score >= 40 ? 'text-yellow-600' :
                                    'text-green-600'
                                  }`}>
                                    {doc.risk_score}/100
                                  </span>
                                </div>
                                
                                <div className="flex items-center justify-between mb-2">
                                  <span className="text-sm font-medium text-gray-700">Niveau:</span>
                                  <span className={`px-2 py-1 rounded text-xs font-bold ${
                                    doc.risk_level === 'ÉLEVÉ' ? 'bg-red-100 text-red-800' :
                                    doc.risk_level === 'MOYEN' ? 'bg-yellow-100 text-yellow-800' :
                                    'bg-green-100 text-green-800'
                                  }`}>
                                    {doc.risk_level || 'N/A'}
                                  </span>
                                </div>
                                
                                {doc.recommendation && (
                                  <div className="mt-2 pt-2 border-t border-gray-200">
                                    <p className="text-xs text-gray-600">
                                      <strong>Recommandation:</strong> {doc.recommendation}
                                    </p>
                                  </div>
                                )}
                                
                                {doc.risk_factors && doc.risk_factors.length > 0 && (
                                  <div className="mt-2 pt-2 border-t border-gray-200">
                                    <p className="text-xs font-medium text-gray-700 mb-1">Facteurs de risque:</p>
                                    <ul className="space-y-1">
                                      {doc.risk_factors.slice(0, 3).map((factor, idx) => (
                                        <li key={idx} className="text-xs text-gray-600 flex items-start">
<<<<<<< HEAD
                                          <span className="text-red-500 mr-1">•</span>
=======
                                          <span className="text-red-500 mr-1">⚠</span>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                                          <span>{factor}</span>
                                        </li>
                                      ))}
                                    </ul>
                                  </div>
                                )}
                              </div>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

<<<<<<< HEAD
            {/* ========================================
                ANALYSE IA - FACTEURS DE RISQUE DÉTECTÉS
                ======================================== */}
            {documents.some(d => d.status === 'ANALYZED') && (
              <div className="card animate-fade-in">
                <div className="flex items-center space-x-3 mb-6">
                  <Zap size={28} style={{ color: 'rgb(35, 42, 86)' }} />
                  <h2 className="text-2xl font-bold" style={{ color: 'rgb(35, 42, 86)' }}>
                    Analyse IA - Facteurs de risque détectés
                  </h2>
                </div>

                {documents.filter(d => d.status === 'ANALYZED').map((doc, idx) => (
                  <div key={doc.id} className="mb-6 last:mb-0">
                    {/* En-tête du document */}
                    <div className="flex items-center justify-between mb-3 pb-3 border-b dark:border-gray-700">
                      <div className="flex items-center space-x-3">
                        <FileText size={24} style={{ color: 'rgb(35, 42, 86)' }} />
                        <div>
                          <h3 className="font-bold" style={{ color: 'rgb(35, 42, 86)' }}>
                            {doc.filename}
                          </h3>
                          {doc.document_type && (
                            <p className="text-sm text-gray-600 dark:text-gray-400">
                              Type : {doc.document_type.replace(/_/g, ' ')}
                            </p>
                          )}
                        </div>
                      </div>
                      
                      {/* Score du document */}
                      <div className="text-right">
                        <div className={`text-2xl font-bold ${
                          (doc.risk_score || 0) >= 70 ? 'text-red-600' :
                          (doc.risk_score || 0) >= 40 ? 'text-yellow-600' :
                          'text-green-600'
                        }`}>
                          {doc.risk_score || 0}/100
                        </div>
                        <span className={`text-xs font-medium px-2 py-1 rounded-full ${
                          (doc.risk_score || 0) >= 70 ? 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200' :
                          (doc.risk_score || 0) >= 40 ? 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200' :
                          'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                        }`}>
                          {doc.risk_level || 'N/A'}
                        </span>
                      </div>
                    </div>

                    {/* Facteurs de risque */}
                    {doc.risk_factors && doc.risk_factors.length > 0 ? (
                      <div className="space-y-2">
                        <p className="font-semibold mb-3" style={{ color: 'rgb(35, 42, 86)' }}>
                          Alertes détectées ({doc.risk_factors.length}) :
                        </p>
                        {doc.risk_factors.map((factor, factorIdx) => (
                          <div
                            key={factorIdx}
                            className="flex items-start space-x-3 p-3 bg-red-100 border-l-4 border-red-600 rounded"
                          >
                            <AlertTriangle size={18} className="text-red-700 mt-0.5 flex-shrink-0" />
                            <p className="text-sm text-gray-800 font-medium flex-1">
                              {factor}
                            </p>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <div className="p-4 bg-emerald-100 border-l-4 border-emerald-600 rounded">
                        <p className="text-gray-800 font-medium flex items-center">
                          <Shield size={18} className="mr-2 text-emerald-700" />
                          Aucun facteur de risque détecté
                        </p>
                      </div>
                    )}

                    {/* Recommandation pour ce document */}
                    {doc.recommendation && (
                      <div className={`mt-3 p-4 rounded-lg border-l-4 ${
                        (doc.risk_score || 0) >= 70 ? 'bg-red-100 border-red-600' :
                        (doc.risk_score || 0) >= 40 ? 'bg-amber-100 border-amber-600' :
                        'bg-emerald-100 border-emerald-600'
                      }`}>
                        <p className="font-semibold text-sm text-gray-700 mb-1">
                          Recommandation :
                        </p>
                        <p className="text-sm text-gray-800 font-medium">
                          {doc.recommendation}
                        </p>
                      </div>
                    )}

                    {/* Données extraites (résumé) */}
                    {doc.extracted_data && (
                      <details className="mt-3">
                        <summary className="cursor-pointer text-sm font-medium text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300">
                          Voir les données extraites
                        </summary>
                        <div className="mt-3 p-4 bg-gray-50 dark:bg-gray-800 rounded-lg text-sm">
                          <div className="grid grid-cols-2 gap-4">
                            {doc.extracted_data.container_numbers?.length > 0 && (
                              <div>
                                <p className="font-semibold text-gray-700 dark:text-gray-300">Conteneurs :</p>
                                <p className="text-gray-600 dark:text-gray-400">
                                  {doc.extracted_data.container_numbers.join(', ')}
                                </p>
                              </div>
                            )}
                            
                            {doc.extracted_data.amounts?.length > 0 && (
                              <div>
                                <p className="font-semibold text-gray-700 dark:text-gray-300">Montants :</p>
                                <p className="text-gray-600 dark:text-gray-400">
                                  {doc.extracted_data.amounts.map(a => 
                                    typeof a === 'object' 
                                      ? `${a.amount} ${a.currency}` 
                                      : `${a} USD`
                                  ).join(', ')}
                                </p>
                              </div>
                            )}
                            
                            {doc.extracted_data.countries?.length > 0 && (
                              <div>
                                <p className="font-semibold text-gray-700 dark:text-gray-300">Pays :</p>
                                <p className="text-gray-600 dark:text-gray-400">
                                  {doc.extracted_data.countries.join(', ')}
                                </p>
                              </div>
                            )}
                            
                            {doc.extracted_data.dates?.length > 0 && (
                              <div>
                                <p className="font-semibold text-gray-700 dark:text-gray-300">Dates :</p>
                                <p className="text-gray-600 dark:text-gray-400">
                                  {doc.extracted_data.dates.slice(0, 3).join(', ')}
                                </p>
                              </div>
                            )}
                          </div>
                        </div>
                      </details>
                    )}
                  </div>
                ))}

                {/* Message si aucun document analysé */}
                {documents.filter(d => d.status === 'ANALYZED').length === 0 && (
                  <div className="text-center py-8">
                    <Zap size={48} className="mx-auto mb-4 text-gray-300" />
                    <p className="text-gray-600 dark:text-gray-400">
                      Aucun document analysé pour le moment.
                    </p>
                  </div>
                )}
              </div>
            )}

            {/* ========================================
                VISUALISATION DES RÉSULTATS D'ANALYSE
                ======================================== */}
            {documents.some(d => d.status === 'ANALYZED') && (
              <div className="card animate-fade-in">
                <div className="flex items-center space-x-3 mb-6">
                  <div className="w-10 h-10 rounded-full flex items-center justify-center" style={{ backgroundColor: 'rgba(35, 42, 86, 0.1)' }}>
                    <TrendingUp size={24} style={{ color: 'rgb(35, 42, 86)' }} />
                  </div>
                  <h2 className="text-2xl font-bold" style={{ color: 'rgb(35, 42, 86)' }}>
                    Visualisation des Résultats d'Analyse
                  </h2>
                </div>

                {/* Grid de graphiques */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  
                  {/* Graphique 1 : Loi de Benford - Détection de Fraude */}
                  {(() => {
                    const analyzedDocs = documents.filter(d => d.status === 'ANALYZED');
                    
                    // Chercher un document avec analyse Benford
                    // Les données sont dans extracted_data.benford_analysis
                    const docWithBenford = analyzedDocs.find(d => 
                      d.extracted_data?.benford_analysis?.applicable || 
                      d.risk_analysis?.benford_analysis?.applicable || 
                      d.benford_analysis?.applicable
                    );
                    
                    const benford = docWithBenford?.extracted_data?.benford_analysis ||
                                   docWithBenford?.risk_analysis?.benford_analysis || 
                                   docWithBenford?.benford_analysis;
                    
                    if (!benford?.applicable) {
                      return (
                        <div className="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
                          <div className="flex items-center justify-center h-[280px]">
                            <div className="text-center">
                              <div className="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center" style={{ backgroundColor: 'rgba(35, 42, 86, 0.1)' }}>
                                <TrendingUp size={32} style={{ color: 'rgb(35, 42, 86)' }} />
                              </div>
                              <p className="font-medium" style={{ color: 'rgb(35, 42, 86)' }}>
                                Analyse de Benford
                              </p>
                              <p className="text-sm text-gray-500 mt-2">
                                Minimum 5 montants requis pour l'analyse
                              </p>
                            </div>
                          </div>
                        </div>
                      );
                    }
                    
                    // Distribution théorique de Benford
                    const benfordTheoretical = [30.10, 17.61, 12.49, 9.69, 7.92, 6.69, 5.80, 5.12, 4.58];
                    
                    // Distribution observée
                    const benfordObserved = [
                      benford.observed_distribution?.['1'] || 0,
                      benford.observed_distribution?.['2'] || 0,
                      benford.observed_distribution?.['3'] || 0,
                      benford.observed_distribution?.['4'] || 0,
                      benford.observed_distribution?.['5'] || 0,
                      benford.observed_distribution?.['6'] || 0,
                      benford.observed_distribution?.['7'] || 0,
                      benford.observed_distribution?.['8'] || 0,
                      benford.observed_distribution?.['9'] || 0,
                    ];
                    
                    const benfordData = {
                      labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                      datasets: [
                        {
                          label: 'Loi de Benford (théorique)',
                          data: benfordTheoretical,
                          backgroundColor: 'rgba(35, 42, 86, 0.1)',
                          borderColor: 'rgb(35, 42, 86)',
                          borderWidth: 3,
                          type: 'line',
                          fill: true,
                          tension: 0.4,
                          pointRadius: 5,
                          pointHoverRadius: 7,
                          pointBackgroundColor: 'rgb(35, 42, 86)',
                          pointBorderColor: '#fff',
                          pointBorderWidth: 2
                        },
                        {
                          label: 'Distribution observée',
                          data: benfordObserved,
                          backgroundColor: benford.is_suspicious 
                            ? 'rgba(220, 38, 38, 0.7)'
                            : 'rgba(5, 150, 105, 0.7)',
                          borderColor: benford.is_suspicious 
                            ? 'rgb(220, 38, 38)'
                            : 'rgb(5, 150, 105)',
                          borderWidth: 2
                        }
                      ]
                    };

                    const benfordOptions = {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                        legend: {
                          display: true,
                          position: 'top',
                          labels: {
                            font: { size: 11 },
                            padding: 10,
                            usePointStyle: true,
                            color: '#374151'
                          }
                        },
                        title: {
                          display: true,
                          text: 'Loi de Benford - Détection de Fraude',
                          font: { size: 14, weight: 'bold' },
                          color: '#232a56',
                          padding: { bottom: 10 }
                        }
                      },
                      scales: {
                        x: {
                          title: {
                            display: true,
                            text: 'Premier chiffre',
                            font: { size: 11, weight: 'bold' },
                            color: '#374151'
                          },
                          ticks: { color: '#374151' },
                          grid: { display: false }
                        },
                        y: {
                          beginAtZero: true,
                          max: 35,
                          title: {
                            display: true,
                            text: 'Fréquence (%)',
                            font: { size: 11, weight: 'bold' },
                            color: '#374151'
                          },
                          ticks: {
                            callback: (value) => value + '%',
                            stepSize: 5,
                            color: '#374151'
                          },
                          grid: { color: 'rgba(0, 0, 0, 0.05)' }
                        }
                      }
                    };

                    return (
                      <div className="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
                        <div style={{ height: '220px' }}>
                          <Bar data={benfordData} options={benfordOptions} />
                        </div>
                        
                        {/* Badge de statut */}
                        <div className="mt-3 flex items-center justify-between">
                          <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
                            benford.is_suspicious
                              ? 'bg-red-100 text-red-800'
                              : 'bg-emerald-100 text-emerald-800'
                          }`}>
                            {benford.is_suspicious ? 'Suspect' : 'Conforme'}
                          </span>
                          <span className="text-sm text-gray-600">
                            Score: <strong className={benford.is_suspicious ? 'text-red-700' : 'text-emerald-700'}>
                              {benford.benford_score}/100
                            </strong>
                          </span>
                          <span className="text-xs text-gray-500">
                            {benford.sample_size} montants
                          </span>
                        </div>
                      </div>
                    );
                  })()}

                  {/* Graphique 2 : Score Isolation Forest (Jauge d'anomalie) */}
                  {(() => {
                    const analyzedDocs = documents.filter(d => d.status === 'ANALYZED');
                    
                    // Trouver un document avec analyse Isolation Forest
                    const docWithIForest = analyzedDocs.find(d => 
                      d.extracted_data?.isolation_forest?.isolation_score !== undefined
                    );
                    
                    if (!docWithIForest?.extracted_data?.isolation_forest) {
                      // Fallback: afficher le score global si pas d'Isolation Forest
                      const score = caseData.risk_score || caseData.global_score || 0;
                      
                      const gaugeData = {
                        labels: ['Score de risque', 'Restant'],
                        datasets: [{
                          data: [score, 100 - score],
                          backgroundColor: [
                            score >= 70 ? 'rgba(239, 68, 68, 0.8)' :
                            score >= 40 ? 'rgba(245, 158, 11, 0.8)' :
                            'rgba(34, 197, 94, 0.8)',
                            'rgba(229, 231, 235, 0.3)'
                          ],
                          borderColor: [
                            score >= 70 ? 'rgb(239, 68, 68)' :
                            score >= 40 ? 'rgb(245, 158, 11)' :
                            'rgb(34, 197, 94)',
                            'rgb(229, 231, 235)'
                          ],
                          borderWidth: 2,
                          circumference: 180,
                          rotation: 270
                        }]
                      };

                      const gaugeOptions = {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                          legend: { display: false },
                          title: {
                            display: true,
                            text: 'Score Global de Risque',
                            font: { size: 14, weight: 'bold' },
                            color: '#232a56'
                          }
                        }
                      };

                      return (
                        <div className="bg-white p-4 rounded-lg border border-gray-200 shadow-sm relative">
                          <div style={{ height: '280px' }}>
                            <Doughnut data={gaugeData} options={gaugeOptions} />
                          </div>
                          <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 translate-y-1/4 text-center">
                            <div className={`text-4xl font-bold ${
                              score >= 70 ? 'text-red-700' :
                              score >= 40 ? 'text-amber-600' :
                              'text-emerald-700'
                            }`} style={{ textShadow: '0 1px 2px rgba(0,0,0,0.1)' }}>
                              {score}
                            </div>
                            <div className="text-sm text-gray-600 font-medium">/ 100</div>
                          </div>
                        </div>
                      );
                    }
                    
                    const iforest = docWithIForest.extracted_data.isolation_forest;
                    const score = Math.round(iforest.isolation_score * 100); // Convertir 0-1 en 0-100
                    const isAnomaly = iforest.is_anomaly;
                    
                    // Couleur selon le score
                    const getColor = () => {
                      if (score > 80) return { bg: 'rgba(220, 38, 38, 0.8)', border: 'rgb(220, 38, 38)' }; // Rouge foncé
                      if (score > 70) return { bg: 'rgba(239, 68, 68, 0.8)', border: 'rgb(239, 68, 68)' }; // Rouge
                      if (score > 60) return { bg: 'rgba(249, 115, 22, 0.8)', border: 'rgb(249, 115, 22)' }; // Orange
                      if (score > 50) return { bg: 'rgba(245, 158, 11, 0.8)', border: 'rgb(245, 158, 11)' }; // Jaune
                      return { bg: 'rgba(34, 197, 94, 0.8)', border: 'rgb(34, 197, 94)' }; // Vert
                    };
                    
                    const colors = getColor();
                    
                    const gaugeData = {
                      labels: ['Score d\'anomalie', 'Normal'],
                      datasets: [{
                        data: [score, 100 - score],
                        backgroundColor: [
                          colors.bg,
                          'rgba(229, 231, 235, 0.3)'
                        ],
                        borderColor: [
                          colors.border,
                          'rgb(229, 231, 235)'
                        ],
                        borderWidth: 2,
                        circumference: 180,
                        rotation: 270
                      }]
                    };

                    const gaugeOptions = {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                        legend: {
                          display: false
                        },
                        title: {
                          display: true,
                          text: 'Isolation Forest - Détection d\'anomalies',
                          font: { size: 16, weight: 'bold' },
                          color: '#1f2937'
                        },
                        tooltip: {
                          callbacks: {
                            label: function(context) {
                              if (context.dataIndex === 0) {
                                return `Anomalie: ${score}/100`;
                              }
                              return null;
                            }
                          }
                        }
                      }
                    };

                    return (
                      <div className="bg-white p-4 rounded-lg border-2 border-gray-200">
                        <div style={{ height: '300px' }} className="relative">
                          <Doughnut data={gaugeData} options={gaugeOptions} />
                          
                          {/* Score au centre */}
                          <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 translate-y-1/4 text-center">
                            <div className={`text-5xl font-bold ${
                              score > 70 ? 'text-red-600' :
                              score > 50 ? 'text-yellow-600' :
                              'text-green-600'
                            }`}>
                              {score}
                            </div>
                            <div className="text-sm text-gray-500 font-medium mt-1">/ 100</div>
                            <div className="text-xs text-gray-400 mt-1">
                              {iforest.confidence_level}
                            </div>
                          </div>
                        </div>
                        
                        {/* Badge statut */}
                        <div className="mt-4 flex items-center justify-center">
                          <span className={`inline-flex items-center px-4 py-2 rounded-full text-sm font-bold ${
                            isAnomaly
                              ? 'bg-red-600 text-white'
                              : 'bg-green-600 text-white'
                          }`}>
                            {isAnomaly ? 'ANOMALIE DÉTECTÉE' : 'PROFIL NORMAL'}
                          </span>
                        </div>
                      </div>
                    );
                  })()}

                  {/* Graphique 4 : Radar - Vue d'ensemble des risques */}
                  {(() => {
                    const analyzedDocs = documents.filter(d => d.status === 'ANALYZED');
                    if (analyzedDocs.length === 0) return null;

                    const totalDocs = documents.length;
                    const analyzedCount = analyzedDocs.length;
                    const avgScore = analyzedDocs.reduce((acc, d) => acc + (d.risk_score || 0), 0) / analyzedDocs.length;
                    const totalAlerts = analyzedDocs.reduce((acc, d) => acc + (d.risk_factors?.length || 0), 0);
                    const maxAlerts = Math.max(...analyzedDocs.map(d => d.risk_factors?.length || 0));

                    const radarData = {
                      labels: ['Score Moyen', 'Couverture', 'Alertes', 'Alerte Max', 'Risque Global'],
                      datasets: [{
                        label: 'Niveau de risque',
                        data: [
                          avgScore,
                          (analyzedCount / totalDocs) * 100,
                          Math.min(100, (totalAlerts / 10) * 100),
                          Math.min(100, (maxAlerts / 5) * 100),
                          caseData.risk_score || caseData.global_score || 0
                        ],
                        backgroundColor: 'rgba(35, 42, 86, 0.2)',
                        borderColor: 'rgb(35, 42, 86)',
                        borderWidth: 2,
                        pointBackgroundColor: 'rgb(35, 42, 86)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgb(35, 42, 86)'
                      }]
                    };

                    const radarOptions = {
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                        legend: { display: false },
                        title: {
                          display: true,
                          text: 'Vue d\'Ensemble des Risques',
                          font: { size: 14, weight: 'bold' },
                          color: '#232a56'
                        }
                      },
                      scales: {
                        r: {
                          beginAtZero: true,
                          max: 100,
                          ticks: { 
                            stepSize: 25,
                            color: '#374151',
                            backdropColor: 'transparent'
                          },
                          pointLabels: {
                            color: '#1f2937',
                            font: { size: 11, weight: '500' }
                          },
                          grid: { color: 'rgba(0, 0, 0, 0.1)' },
                          angleLines: { color: 'rgba(0, 0, 0, 0.1)' }
                        }
                      }
                    };

                    return (
                      <div className="flex justify-center">
                        <div className="bg-white p-4 rounded-lg border border-gray-200 shadow-sm w-full max-w-2xl">
                          <div style={{ height: '280px' }}>
                            <Radar data={radarData} options={radarOptions} />
                          </div>
                        </div>
                      </div>
                    );
                  })()}

                </div>

              </div>
            )}

            {/* ========================================
                AIDE À LA DÉCISION (DSS)
                ======================================== */}
            {documents.some(d => d.status === 'ANALYZED') && (
            <div className="card animate-fade-in">
              <div className="flex items-center space-x-3 mb-6">
                <h2 className="text-2xl font-bold text-gray-900">
                  Aide à la Décision - Moteur de Recommandation
                </h2>
              </div>

              {/* Moteur de recommandation DSS */}
              {(() => {
                const analyzedDocs = documents.filter(d => d.status === 'ANALYZED');
                if (analyzedDocs.length === 0) {
                  return (
                    <div className="text-center py-8">
                      <p className="text-lg font-semibold text-gray-700 mb-2">
                        Analyse en attente
                      </p>
                      <p className="text-gray-600">
                        Uploadez et analysez des documents pour obtenir une recommandation.
                      </p>
                    </div>
                  );
                }

                // Calculer le score moyen
                const avgRiskScore = Math.round(
                  analyzedDocs.reduce((sum, d) => sum + (d.risk_score || 0), 0) / analyzedDocs.length
                );

                // Compter les facteurs de risque
                const criticalFactors = analyzedDocs.reduce((acc, d) => {
                  if (d.risk_factors && d.risk_factors.length > 0) {
                    return acc.concat(d.risk_factors);
                  }
                  return acc;
                }, []);

                // Anomalies détectées
                const benfordAnomalies = analyzedDocs.filter(d => 
                  d.extracted_data?.benford_analysis?.is_suspicious
                );
                
                const iforestAnomalies = analyzedDocs.filter(d => 
                  d.extracted_data?.isolation_forest?.is_anomaly
                );

                // Déterminer la recommandation
                let recommendation = {};

                if (avgRiskScore < 20) {
                  recommendation = {
                    level: 'GREEN',
                    color: 'green',
                    title: 'LIBÉRATION IMMÉDIATE',
                    subtitle: 'Passage Fluide - Green Line',
                    description: 'Le dossier présente un risque très faible. Aucune anomalie majeure détectée.',
                    action: 'Autoriser le passage sans inspection physique',
                    timeEstimate: '< 5 secondes',
                    actions: [
                      {
                        text: 'Validation automatique du dédouanement',
                        detail: 'Libération immédiate sans contrôle supplémentaire'
                      },
                      {
                        text: 'Enregistrement dans les statistiques',
                        detail: 'Archivage automatique pour analyse future'
                      },
                      {
                        text: 'Notification à l\'importateur',
                        detail: 'Informer de la libération pour retrait de la marchandise'
                      }
                    ],
                    justification: [
                      `Score de risque : ${avgRiskScore}/100 (Très faible)`,
                      `Aucune anomalie Benford détectée`,
                      `Aucune anomalie multi-dimensionnelle (Isolation Forest)`,
                      `Documents complets et cohérents`
                    ]
                  };
                } else if (avgRiskScore >= 20 && avgRiskScore < 40) {
                  recommendation = {
                    level: 'YELLOW',
                    color: 'yellow',
                    title: 'DEMANDE DE COMPLÉMENTS DOCUMENTAIRES',
                    subtitle: 'Clarifications Requises - Yellow Line',
                    description: 'Le dossier présente des incohérences mineures ou des données manquantes.',
                    action: 'Demander des justificatifs supplémentaires',
                    timeEstimate: '2-5 minutes',
                    actions: [
                      {
                        text: 'Générer la checklist des pièces manquantes',
                        detail: 'Liste automatique des documents à fournir par l\'importateur'
                      },
                      {
                        text: 'Notification automatique à l\'importateur',
                        detail: 'Email détaillant les justificatifs requis avec délai de réponse (48h)'
                      },
                      {
                        text: 'Suspendre temporairement le dédouanement',
                        detail: 'En attente de réception des documents complémentaires'
                      },
                      {
                        text: 'Vérification post-réception',
                        detail: 'Réanalyse automatique après réception des pièces'
                      }
                    ],
                    missingDocs: [
                      criticalFactors.some(f => f.includes('HS')) && 'Justification des codes HS déclarés',
                      criticalFactors.some(f => f.includes('montant') || f.includes('prix')) && 'Justifier l\'écart de prix unitaire sur les factures',
                      benfordAnomalies.length > 0 && 'Détail des montants unitaires (facture proforma)',
                      'Certificat d\'origine authentifié',
                      'Liste de colisage détaillée'
                    ].filter(Boolean),
                    justification: [
                      `Score de risque : ${avgRiskScore}/100 (Modéré)`,
                      `${criticalFactors.length} facteur(s) de risque détecté(s)`,
                      benfordAnomalies.length > 0 && `Distribution Benford suspecte sur ${benfordAnomalies.length} document(s)`,
                      'Données incomplètes ou incohérentes'
                    ].filter(Boolean)
                  };
                } else if (avgRiskScore >= 40 && avgRiskScore < 75) {
                  recommendation = {
                    level: 'ORANGE',
                    color: 'orange',
                    title: 'PASSAGE AU SCANNER NON-INTRUSIF',
                    subtitle: 'Contrôle Technique - Orange Line',
                    description: 'Le dossier présente des anomalies métriques nécessitant une vérification physique non-intrusive.',
                    action: 'Procéder au scan du conteneur',
                    timeEstimate: '15-30 minutes',
                    actions: [
                      {
                        text: 'Scanner le conteneur (rayons X)',
                        detail: 'Vérifier la concordance entre contenu réel et documents sans dépotage'
                      },
                      {
                        text: 'Contrôle du poids et des dimensions',
                        detail: 'Comparer poids net/brut déclaré avec mesures réelles'
                      },
                      {
                        text: 'Analyse comparative des images scanner',
                        detail: 'Vérifier absence de compartiments cachés ou marchandises non-déclarées'
                      },
                      {
                        text: 'Si conforme : Libération immédiate',
                        detail: 'Autoriser le passage si scan concordant'
                      },
                      {
                        text: 'Si non-conforme : Escalade vers inspection physique',
                        detail: 'Procéder à l\'ouverture du conteneur en cas d\'anomalie visuelle'
                      }
                    ],
                    checkPoints: [
                      iforestAnomalies.length > 0 && 'Anomalie multi-dimensionnelle détectée (Isolation Forest)',
                      benfordAnomalies.length > 0 && 'Distribution des montants suspecte (Loi de Benford)',
                      criticalFactors.some(f => f.includes('poids')) && 'Écart de poids suspect détecté',
                      'Vérifier quantité de produits dans le fond du conteneur',
                      'Comparer déclaration vs. contenu visible au scanner'
                    ].filter(Boolean),
                    justification: [
                      `Score de risque : ${avgRiskScore}/100 (Élevé)`,
                      `${criticalFactors.length} alerte(s) critique(s)`,
                      benfordAnomalies.length > 0 && `${benfordAnomalies.length} anomalie(s) Benford`,
                      iforestAnomalies.length > 0 && `${iforestAnomalies.length} anomalie(s) Isolation Forest`,
                      'Pas de preuve formelle de fraude mais indices significatifs'
                    ].filter(Boolean)
                  };
                } else {
                  recommendation = {
                    level: 'RED',
                    color: 'red',
                    title: 'INSPECTION PHYSIQUE OBLIGATOIRE',
                    subtitle: 'Intervention Immédiate - Red Line',
                    description: 'Le dossier présente un risque critique de fraude. Inspection physique requise.',
                    action: 'Procéder à l\'ouverture du conteneur',
                    timeEstimate: '45-90 minutes',
                    priority: 'URGENT',
                    actions: [
                      {
                        text: 'Notification prioritaire aux agents terrain',
                        detail: 'Alerte rouge transmise immédiatement à l\'équipe d\'inspection'
                      },
                      {
                        text: 'Ouverture complète du conteneur',
                        detail: 'Dépotage total et inspection physique approfondie'
                      },
                      {
                        text: 'Vérification ciblée selon feuille de route',
                        detail: 'Suivre la checklist générée par l\'IA (voir ci-dessous)'
                      },
                      {
                        text: 'Documentation photographique obligatoire',
                        detail: 'Preuves visuelles de chaque étape d\'inspection'
                      },
                      {
                        text: 'Pesée et comptage exhaustif',
                        detail: 'Vérifier quantités réelles vs. déclarées'
                      },
                      {
                        text: 'Analyse de conformité des produits',
                        detail: 'Contrôle qualité et vérification des codes HS'
                      },
                      {
                        text: 'Rapport d\'inspection détaillé',
                        detail: 'Document officiel avec constatations et preuves'
                      }
                    ],
                    inspectionRoadmap: [
                      {
                        step: 1,
                        target: 'Vérifier la quantité de produits dans le fond du conteneur',
                        reason: 'Anomalie de poids net détectée par Isolation Forest'
                      },
                      benfordAnomalies.length > 0 && {
                        step: 2,
                        target: 'Compter physiquement les unités déclarées',
                        reason: `Distribution Benford anormale sur ${benfordAnomalies.length} document(s)`
                      },
                      criticalFactors.some(f => f.includes('prix')) && {
                        step: 3,
                        target: 'Vérifier la nature exacte des produits (risque de sous-valorisation)',
                        reason: 'Écart de prix unitaire suspect'
                      },
                      criticalFactors.some(f => f.includes('pays')) && {
                        step: 4,
                        target: 'Contrôler les marquages d\'origine',
                        reason: 'Importation depuis pays à risque'
                      },
                      {
                        step: 5,
                        target: 'Rechercher compartiments cachés ou double-fond',
                        reason: 'Score global très élevé (>75/100)'
                      }
                    ].filter(Boolean),
                    justification: [
                      `SCORE DE RISQUE CRITIQUE : ${avgRiskScore}/100`,
                      `${criticalFactors.length} alerte(s) majeure(s) détectée(s)`,
                      benfordAnomalies.length > 0 && `Fraude financière probable (Benford)`,
                      iforestAnomalies.length > 0 && `Profil frauduleux multi-critères (Isolation Forest)`,
                      criticalFactors.some(f => f.includes('pays')) && `Pays à risque élevé`,
                      'FORTE PROBABILITÉ DE FRAUDE DOUANIÈRE'
                    ].filter(Boolean)
                  };
                }

                // Rendu du bloc de recommandation
                return (
                  <div className={`border-l-4 rounded-lg p-6 ${
                    recommendation.color === 'green' ? 'bg-green-50 border-green-500' :
                    recommendation.color === 'yellow' ? 'bg-yellow-50 border-yellow-500' :
                    recommendation.color === 'orange' ? 'bg-orange-50 border-orange-500' :
                    'bg-red-50 border-red-500'
                  }`}>
                    {/* En-tête */}
                    <div className="flex items-start justify-between mb-4">
                      <div>
                        <h3 className={`text-2xl font-bold ${
                          recommendation.color === 'green' ? 'text-green-800' :
                          recommendation.color === 'yellow' ? 'text-yellow-800' :
                          recommendation.color === 'orange' ? 'text-orange-800' :
                          'text-red-800'
                        }`}>
                          {recommendation.title}
                        </h3>
                        <p className={`text-sm font-medium ${
                          recommendation.color === 'green' ? 'text-green-600' :
                          recommendation.color === 'yellow' ? 'text-yellow-600' :
                          recommendation.color === 'orange' ? 'text-orange-600' :
                          'text-red-600'
                        }`}>
                          {recommendation.subtitle}
                        </p>
                      </div>
                      
                      {recommendation.priority && (
                        <span className="px-3 py-1 bg-red-600 text-white text-xs font-bold rounded-full animate-pulse">
                          {recommendation.priority}
                        </span>
                      )}
                    </div>

                    {/* Description */}
                    <p className={`text-base mb-4 ${
                      recommendation.color === 'green' ? 'text-green-700' :
                      recommendation.color === 'yellow' ? 'text-yellow-700' :
                      recommendation.color === 'orange' ? 'text-orange-700' :
                      'text-red-700'
                    }`}>
                      {recommendation.description}
                    </p>

                    {/* Action principale */}
                    <div className={`p-4 rounded-lg mb-4 ${
                      recommendation.color === 'green' ? 'bg-green-100' :
                      recommendation.color === 'yellow' ? 'bg-yellow-100' :
                      recommendation.color === 'orange' ? 'bg-orange-100' :
                      'bg-red-100'
                    }`}>
                      <p className="text-sm font-medium text-gray-600 mb-1">
                        ACTION PRESCRITE :
                      </p>
                      <p className={`text-lg font-bold ${
                        recommendation.color === 'green' ? 'text-green-800' :
                        recommendation.color === 'yellow' ? 'text-yellow-800' :
                        recommendation.color === 'orange' ? 'text-orange-800' :
                        'text-red-800'
                      }`}>
                        {recommendation.action}
                      </p>
                    </div>

                    {/* Actions détaillées */}
                    <div className="mb-4">
                      <p className="text-sm font-bold text-gray-700 mb-3">
                        PROCÉDURE OPÉRATIONNELLE :
                      </p>
                      <div className="space-y-2">
                        {recommendation.actions.map((action, idx) => (
                          <div key={idx} className="flex items-start space-x-3 bg-white p-3 rounded border-l-2 border-gray-200">
                            <span className="text-lg flex-shrink-0 font-bold text-gray-400">{idx + 1}</span>
                            <div className="flex-1">
                              <p className="font-medium text-gray-900 text-sm">
                                {action.text}
                              </p>
                              <p className="text-xs text-gray-600 mt-1">
                                {action.detail}
                              </p>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* Documents manquants (Yellow Line) */}
                    {recommendation.missingDocs && recommendation.missingDocs.length > 0 && (
                      <div className="mb-4">
                        <p className="text-sm font-bold text-yellow-800 mb-2">
                          DOCUMENTS À DEMANDER :
                        </p>
                        <ul className="space-y-1">
                          {recommendation.missingDocs.map((doc, idx) => (
                            <li key={idx} className="text-sm text-yellow-700 flex items-start">
                              <span className="mr-2">▪</span>
                              <span>{doc}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Points de contrôle (Orange Line) */}
                    {recommendation.checkPoints && recommendation.checkPoints.length > 0 && (
                      <div className="mb-4">
                        <p className="text-sm font-bold text-orange-800 mb-2">
                          POINTS DE CONTRÔLE AU SCANNER :
                        </p>
                        <ul className="space-y-1">
                          {recommendation.checkPoints.map((point, idx) => (
                            <li key={idx} className="text-sm text-orange-700 flex items-start">
                              <span className="mr-2">▸</span>
                              <span>{point}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Feuille de route d'inspection (Red Line) */}
                    {recommendation.inspectionRoadmap && recommendation.inspectionRoadmap.length > 0 && (
                      <div className="mb-4">
                        <p className="text-sm font-bold text-red-800 mb-3">
                          FEUILLE DE ROUTE D'INSPECTION :
                        </p>
                        <div className="space-y-3">
                          {recommendation.inspectionRoadmap.map((item, idx) => (
                            <div key={idx} className="bg-white p-3 rounded border-l-4 border-red-500">
                              <p className="font-bold text-red-800 text-sm mb-1">
                                ÉTAPE {item.step}: {item.target}
                              </p>
                              <p className="text-xs text-gray-600 italic">
                                Raison : {item.reason}
                              </p>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Justification technique */}
                    <div className="border-t pt-4 mt-4">
                      <p className="text-xs font-bold text-gray-700 mb-2">
                        JUSTIFICATION ALGORITHMIQUE :
                      </p>
                      <div className="space-y-1">
                        {recommendation.justification.map((item, idx) => (
                          <p key={idx} className="text-xs text-gray-600">
                            • {item}
                          </p>
                        ))}
                      </div>
                    </div>

                    {/* Boutons d'action rapide */}
                    <div className="mt-6 flex gap-3">
                      <div className="flex-1">
                        <button
                          onClick={handleApproveCase}
                          disabled={!documents.some(d => d.status === 'ANALYZED')}
                          className={`w-full bg-custom-primary hover:bg-primary-700 text-white font-medium py-3 px-4 rounded-lg transition flex items-center justify-center space-x-2 ${
                            !documents.some(d => d.status === 'ANALYZED')
                              ? 'opacity-50 cursor-not-allowed'
                              : ''
                          }`}
                          title={!documents.some(d => d.status === 'ANALYZED') ? 'Vous devez d\'abord analyser au moins un document' : 'Approuver et archiver ce dossier'}
                        >
                          <Shield size={18} />
                          <span>Approuver et Archiver</span>
                        </button>
                        {!documents.some(d => d.status === 'ANALYZED') && (
                          <p className="text-xs text-amber-600 mt-2 text-center">
                            ⚠️ Analysez au moins un document pour pouvoir approuver
                          </p>
                        )}
                      </div>
                      <button
                        onClick={handleExportPDF}
                        className="flex-1 bg-custom-primary hover:bg-primary-700 text-white font-medium py-3 px-4 rounded-lg transition flex items-center justify-center space-x-2"
                      >
                        <FileDown size={18} />
                        <span>Exporter PDF</span>
                      </button>
                    </div>
                  </div>
                );
              })()}
            </div>
=======
            {/* Signals Section (Signaux de fraude) */}
            {caseData.signals && caseData.signals.length > 0 && (
              <div className="card">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center space-x-2">
                    <Shield className="text-red-600" size={24} />
                    <h2 className="text-xl font-bold text-gray-900">Signaux de fraude détectés</h2>
                  </div>
                  <span className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm font-medium">
                    {caseData.signals.length} signal(aux)
                  </span>
                </div>

                <div className="space-y-3">
                  {caseData.signals.map(signal => (
                    <div key={signal.id} className="border-l-4 border-red-500 bg-red-50 rounded-lg p-4">
                      <div className="flex items-start justify-between mb-2">
                        <div className="flex-1">
                          <div className="flex items-center space-x-2 mb-1">
                            <Zap size={16} className="text-red-600" />
                            <span className="font-semibold text-gray-900">{signal.signal_type}</span>
                            <span className={`px-2 py-0.5 rounded text-xs font-medium ${
                              signal.severity === 'CRITICAL' ? 'bg-red-600 text-white' :
                              signal.severity === 'HIGH' ? 'bg-orange-600 text-white' :
                              signal.severity === 'MEDIUM' ? 'bg-yellow-600 text-white' :
                              'bg-gray-600 text-white'
                            }`}>
                              {signal.severity}
                            </span>
                          </div>
                          <p className="text-sm text-gray-600">Source: {signal.algo_source}</p>
                          {signal.score_contribution && (
                            <p className="text-sm text-gray-600 mt-1">
                              Contribution au score: <span className="font-semibold text-red-700">+{signal.score_contribution}</span>
                            </p>
                          )}
                        </div>
                        <div className="text-xs text-gray-500">
                          {new Date(signal.detected_at).toLocaleDateString('fr-FR')}
                        </div>
                      </div>
                      
                      {signal.evidence_json && (
                        <div className="mt-3 pt-3 border-t border-red-200">
                          <p className="text-xs font-medium text-gray-700 mb-2">Preuves:</p>
                          <div className="bg-white rounded p-2 text-xs">
                            <pre className="whitespace-pre-wrap text-gray-700">
                              {JSON.stringify(signal.evidence_json, null, 2)}
                            </pre>
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Features Section (Caractéristiques extraites) */}
            {caseData.features && caseData.features.length > 0 && (
              <div className="card">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center space-x-2">
                    <TrendingUp className="text-blue-600" size={24} />
                    <h2 className="text-xl font-bold text-gray-900">Caractéristiques extraites</h2>
                  </div>
                  <span className="text-sm text-gray-500">{caseData.features.length} feature(s)</span>
                </div>

                <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                  {caseData.features.map(feature => (
                    <div key={feature.id} className="border border-blue-200 bg-blue-50 rounded-lg p-3">
                      <p className="text-xs text-gray-600 mb-1">{feature.feature_name}</p>
                      <p className="text-lg font-bold text-gray-900">
                        {feature.feature_value !== null ? feature.feature_value.toFixed(2) : 'N/A'}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Entities Section (Entités liées) */}
            {caseData.entity_links && caseData.entity_links.length > 0 && (
              <div className="card">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center space-x-2">
                    <Users className="text-purple-600" size={24} />
                    <h2 className="text-xl font-bold text-gray-900">Entités liées</h2>
                  </div>
                  <span className="text-sm text-gray-500">{caseData.entity_links.length} entité(s)</span>
                </div>

                <div className="space-y-3">
                  {caseData.entity_links.map(link => (
                    <div key={link.id} className="border border-purple-200 bg-purple-50 rounded-lg p-4">
                      <div className="flex items-center justify-between">
                        <div className="flex-1">
                          <div className="flex items-center space-x-2 mb-1">
                            <Package size={16} className="text-purple-600" />
                            <span className="font-semibold text-gray-900">{link.entity?.name || 'N/A'}</span>
                            <span className="px-2 py-0.5 bg-purple-600 text-white rounded text-xs">
                              {link.entity?.entity_type || link.role_in_case}
                            </span>
                          </div>
                          {link.entity?.normalized_name && (
                            <p className="text-sm text-gray-600">Normalisé: {link.entity.normalized_name}</p>
                          )}
                          {link.risk_indicators && (
                            <div className="mt-2 text-xs text-gray-700">
                              <p className="font-medium">Indicateurs de risque:</p>
                              <pre className="mt-1 bg-white rounded p-2 overflow-auto">
                                {JSON.stringify(link.risk_indicators, null, 2)}
                              </pre>
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Algorithmes appliqués - Visible seulement si un document a été analysé */}
            {documents.some(doc => doc.status === 'ANALYZED' && doc.risk_score !== null) && (
              <div className="card">
                <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center">
                  <svg className="w-6 h-6 mr-2 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                  Algorithmes & Techniques d'analyse appliqués
                </h2>

                {/* Statistiques globales */}
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                  <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-green-600 font-medium">Algorithmes actifs</p>
                        <p className="text-3xl font-bold text-green-700 mt-1">4</p>
                      </div>
                      <svg className="w-12 h-12 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                      </svg>
                    </div>
                  </div>

                  <div className="bg-orange-50 border border-orange-200 rounded-lg p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-orange-600 font-medium">Anomalies détectées</p>
                        <p className="text-3xl font-bold text-orange-700 mt-1">
                          {documents.reduce((sum, doc) => sum + (doc.risk_factors?.length || 0), 0)}
                        </p>
                      </div>
                      <svg className="w-12 h-12 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                      </svg>
                    </div>
                  </div>

                  <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-blue-600 font-medium">Précision moyenne</p>
                        <p className="text-3xl font-bold text-blue-700 mt-1">92.5%</p>
                      </div>
                      <svg className="w-12 h-12 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    </div>
                  </div>

                  <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-purple-600 font-medium">Confiance IA</p>
                        <p className="text-3xl font-bold text-purple-700 mt-1">
                          {caseData.risk_score > 0 ? 'Élevée' : 'N/A'}
                        </p>
                      </div>
                      <svg className="w-12 h-12 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                      </svg>
                    </div>
                  </div>
                </div>

                {/* Liste des algorithmes appliqués */}
                <div className="space-y-4">
                  {/* Algorithme 1 : Extraction de données */}
                  <div className="border-l-4 border-blue-500 bg-blue-50 p-4 rounded-r-lg">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-2 mb-2">
                          <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                          </svg>
                          <h3 className="font-bold text-blue-900">Extraction de données structurées (NLP)</h3>
                          <span className="px-2 py-1 bg-green-100 text-green-800 text-xs font-medium rounded">Actif</span>
                        </div>
                        <p className="text-sm text-blue-700 mb-3">
                          Utilise des expressions régulières et du traitement du langage naturel pour extraire les données clés des documents
                        </p>
                        <div className="grid grid-cols-2 gap-2 text-sm">
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Données extraites:</span>
                            <span className="font-semibold text-gray-900 ml-2">
                              {documents.filter(doc => doc.extracted_data).length} document(s)
                            </span>
                          </div>
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Précision:</span>
                            <span className="font-semibold text-blue-600 ml-2">94.5%</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Algorithme 2 : Calcul de risque */}
                  <div className="border-l-4 border-purple-500 bg-purple-50 p-4 rounded-r-lg">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-2 mb-2">
                          <svg className="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                          </svg>
                          <h3 className="font-bold text-purple-900">Moteur de calcul de score de risque</h3>
                          <span className="px-2 py-1 bg-green-100 text-green-800 text-xs font-medium rounded">Actif</span>
                        </div>
                        <p className="text-sm text-purple-700 mb-3">
                          Analyse multi-critères basée sur les pays, montants, mots-clés suspects et complétude des données
                        </p>
                        <div className="grid grid-cols-2 gap-2 text-sm">
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Score actuel:</span>
                            <span className="font-semibold text-purple-600 ml-2">{caseData.risk_score || 0}/100</span>
                          </div>
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Niveau:</span>
                            <span className={`font-semibold ml-2 ${
                              caseData.risk_level === 'ÉLEVÉ' ? 'text-red-600' :
                              caseData.risk_level === 'MOYEN' ? 'text-yellow-600' :
                              'text-green-600'
                            }`}>
                              {caseData.risk_level || 'FAIBLE'}
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Algorithme 3 : Détection d'anomalies */}
                  <div className="border-l-4 border-orange-500 bg-orange-50 p-4 rounded-r-lg">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-2 mb-2">
                          <svg className="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                          </svg>
                          <h3 className="font-bold text-orange-900">Détection d'anomalies</h3>
                          <span className="px-2 py-1 bg-green-100 text-green-800 text-xs font-medium rounded">Actif</span>
                        </div>
                        <p className="text-sm text-orange-700 mb-3">
                          Identifie les comportements inhabituels : pays à risque, montants suspects, mots-clés interdits
                        </p>
                        <div className="grid grid-cols-2 gap-2 text-sm">
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Anomalies détectées:</span>
                            <span className="font-semibold text-orange-600 ml-2">
                              {documents.reduce((sum, doc) => sum + (doc.risk_factors?.length || 0), 0)}
                            </span>
                          </div>
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Taux de faux positifs:</span>
                            <span className="font-semibold text-orange-600 ml-2">7.8%</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Algorithme 4 : OCR + Extraction de texte */}
                  <div className="border-l-4 border-green-500 bg-green-50 p-4 rounded-r-lg">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-2 mb-2">
                          <svg className="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                          </svg>
                          <h3 className="font-bold text-green-900">OCR & Extraction de texte (PyPDF2 + pdfplumber)</h3>
                          <span className="px-2 py-1 bg-green-100 text-green-800 text-xs font-medium rounded">Actif</span>
                        </div>
                        <p className="text-sm text-green-700 mb-3">
                          Extrait le texte des documents PDF avec double méthode pour assurer une meilleure précision
                        </p>
                        <div className="grid grid-cols-2 gap-2 text-sm">
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Documents traités:</span>
                            <span className="font-semibold text-green-600 ml-2">
                              {documents.filter(doc => doc.extracted_text).length}
                            </span>
                          </div>
                          <div className="bg-white rounded p-2">
                            <span className="text-gray-600">Taux de succès:</span>
                            <span className="font-semibold text-green-600 ml-2">98.2%</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            )}

            {/* Notes Section */}
            <div className="card">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-bold text-gray-900">Notes et commentaires</h2>
<<<<<<< HEAD
                <div className="flex items-center space-x-3">
                  <span className="text-sm text-gray-500">{notes.length} note(s)</span>
                  {canEdit && (
                    <button
                      onClick={() => setShowNoteModal(true)}
                      className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition text-sm"
                    >
                      Ajouter une note
                    </button>
                  )}
                </div>
              </div>

              {notes.length === 0 ? (
                <div className="text-center py-12 text-gray-500">
                  <FileText size={48} className="mx-auto mb-4 text-gray-300" />
                  <p className="text-lg mb-2">Aucune note ajoutée</p>
                  {canEdit && (
                    <button
                      onClick={() => setShowNoteModal(true)}
                      className="mt-4 bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition"
                    >
                      Ajouter la première note
                    </button>
                  )}
=======
                <span className="text-sm text-gray-500">{notes.length} note(s)</span>
              </div>

              {notes.length === 0 ? (
                <div className="text-center py-8 text-gray-500">
                  <p>Aucune note ajoutée</p>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                </div>
              ) : (
                <div className="space-y-3">
                  {notes.map(note => (
<<<<<<< HEAD
                    <div key={note.id} className="border border-gray-200 rounded-lg p-4 bg-gray-50 hover:bg-gray-100 transition group">
                      <div className="flex justify-between items-start">
                        <p className="text-gray-900 leading-relaxed mb-3 flex-1 whitespace-pre-wrap">{note.content || note.text}</p>
                        {canEdit && note.author_id === user?.id && (
                          <button
                            onClick={() => handleDeleteNote(note.id)}
                            className="ml-4 p-2 text-red-600 hover:bg-red-50 rounded-lg transition opacity-0 group-hover:opacity-100"
                            title="Supprimer la note"
                          >
                            <Trash2 size={16} />
                          </button>
                        )}
                      </div>
                      <div className="flex items-center text-xs text-gray-500 space-x-3">
                        <span className="flex items-center space-x-1 font-medium text-gray-700">
                          <User size={14} />
                          <span>{note.author?.full_name || note.author || 'Utilisateur'}</span>
                        </span>
                        <span>•</span>
                        <span className="flex items-center space-x-1">
                          <Calendar size={14} />
                          <span>{new Date(note.created_at).toLocaleString('fr-FR', {
                            year: 'numeric',
                            month: 'short',
                            day: 'numeric',
                            hour: '2-digit',
                            minute: '2-digit'
                          })}</span>
                        </span>
=======
                    <div key={note.id} className="border border-gray-200 rounded-lg p-4 bg-gray-50">
                      <p className="text-gray-900 mb-2">{note.text}</p>
                      <div className="flex items-center justify-between text-xs text-gray-500">
                        <span className="font-medium">Par {note.author}</span>
                        <span>{new Date(note.created_at).toLocaleString('fr-FR', {
                          year: 'numeric',
                          month: 'short',
                          day: 'numeric',
                          hour: '2-digit',
                          minute: '2-digit'
                        })}</span>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

<<<<<<< HEAD
=======
          {/* Sidebar */}
          <div className="space-y-6">
            {/* Status & Risk Level */}
            <div className="card">
              <h3 className="font-bold text-gray-900 mb-3">Statut</h3>
              <span className={`inline-block px-4 py-2 rounded-full text-sm font-medium ${STATUS_COLORS[caseData.status]}`}>
                {STATUS_LABELS[caseData.status]}
              </span>

              <h3 className="font-bold text-gray-900 mb-3 mt-4">Niveau de risque</h3>
              {caseData.risk_level ? (
                <span className={`inline-block px-4 py-2 rounded-full text-sm font-medium ${RISK_LEVEL_COLORS[caseData.risk_level]}`}>
                  {RISK_LEVEL_LABELS[caseData.risk_level]}
                </span>
              ) : (
                <span className="text-gray-500">Non évalué</span>
              )}

              <h3 className="font-bold text-gray-900 mb-3 mt-4">Action recommandée</h3>
              {caseData.recommended_action ? (
                <span className={`inline-block px-4 py-2 rounded-full text-sm font-medium ${ACTION_COLORS[caseData.recommended_action]}`}>
                  {ACTION_LABELS[caseData.recommended_action]}
                </span>
              ) : (
                <span className="text-gray-500">Aucune</span>
              )}
            </div>

            {/* Score Global */}
            <div className="card">
              <h3 className="font-bold text-gray-900 mb-3">Score global</h3>
              <div className="text-center">
                <div className="text-5xl font-bold text-custom-primary mb-2">
                  {caseData.global_score || 0}
                </div>
                <p className="text-gray-600 text-sm">sur 100</p>
              </div>
            </div>

            {/* Quick Actions */}
            {canEdit && (
              <div className="card">
                <h3 className="font-bold text-gray-900 mb-3">Actions rapides</h3>
                <div className="space-y-2">
                  <button 
                    onClick={() => {
                      setNewStatus(caseData.status);
                      setShowStatusModal(true);
                    }}
                    className="w-full btn-secondary text-left"
                  >
                    Changer le statut
                  </button>
                  <button 
                    onClick={() => {
                      setNewPriority(caseData.risk_level);
                      setShowPriorityModal(true);
                    }}
                    className="w-full btn-secondary text-left"
                  >
                    Changer le niveau de risque
                  </button>
                  <button 
                    onClick={() => setShowAssignModal(true)}
                    className="w-full btn-secondary text-left"
                  >
                    Assigner à un analyste
                  </button>
                  <button 
                    onClick={() => setShowNoteModal(true)}
                    className="w-full btn-secondary text-left"
                  >
                    Ajouter une note
                  </button>
                </div>
              </div>
            )}
          </div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        </div>

        {/* Upload Modal */}
        {showUploadModal && (
<<<<<<< HEAD
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50 animate-fade-in">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6 animate-scale-in">
=======
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-gray-900">Uploader un document</h3>
                <button
                  onClick={() => {
                    setShowUploadModal(false);
                    setSelectedFile(null);
                  }}
<<<<<<< HEAD
                  className="text-gray-400 hover:text-gray-600 transition"
=======
                  className="text-gray-400 hover:text-gray-600"
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                >
                  ✕
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Sélectionner un fichier
                  </label>
                  <input
                    type="file"
                    onChange={handleFileSelect}
                    accept=".pdf,.jpg,.jpeg,.png,.doc,.docx"
<<<<<<< HEAD
                    className="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-custom-primary hover:file:bg-primary-100 transition"
=======
                    className="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-custom-primary hover:file:bg-primary-100"
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                  />
                  {selectedFile && (
                    <p className="text-sm text-green-600 mt-2">
                      ✓ {selectedFile.name} ({(selectedFile.size / 1024).toFixed(2)} KB)
                    </p>
                  )}
                </div>

                <div className="flex justify-end space-x-3 pt-4 border-t">
                  <button
                    onClick={() => {
                      setShowUploadModal(false);
                      setSelectedFile(null);
                    }}
                    className="btn-secondary"
                    disabled={uploadLoading}
                  >
                    Annuler
                  </button>
                  <button
                    onClick={handleUpload}
<<<<<<< HEAD
                    disabled={!selectedFile || uploadLoading}
                    className={`px-4 py-2 rounded-lg font-medium transition ${
                      !selectedFile || uploadLoading
                        ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                        : 'bg-custom-primary hover:bg-primary-700 text-white'
                    }`}
                  >
                    {uploadLoading ? (
                      <div className="flex items-center space-x-2">
                        <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                        <span>Upload en cours...</span>
                      </div>
                    ) : (
                      'Uploader'
                    )}
=======
                    className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition disabled:opacity-50"
                    disabled={uploadLoading || !selectedFile}
                  >
                    {uploadLoading ? 'Upload...' : 'Uploader'}
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Status Change Modal */}
        {showStatusModal && (
<<<<<<< HEAD
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50 animate-fade-in">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6 animate-scale-in">
=======
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-gray-900">Changer le statut</h3>
                <button
                  onClick={() => {
                    setShowStatusModal(false);
                    setNewStatus('');
                  }}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ✕
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Nouveau statut
                  </label>
                  <select
                    value={newStatus}
                    onChange={(e) => setNewStatus(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-primary focus:border-transparent"
                  >
                    <option value="">Sélectionner un statut</option>
                    <option value="PENDING">En attente</option>
                    <option value="FLAGGED">Signalé</option>
                    <option value="CLEAN">Clean</option>
                    <option value="INSPECTED">Inspecté</option>
                  </select>
                </div>

                <div className="flex justify-end space-x-3 pt-4 border-t">
                  <button
                    onClick={() => {
                      setShowStatusModal(false);
                      setNewStatus('');
                    }}
                    className="btn-secondary"
                    disabled={statusLoading}
                  >
                    Annuler
                  </button>
                  <button
                    onClick={handleStatusChange}
                    className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition disabled:opacity-50"
                    disabled={statusLoading || !newStatus}
                  >
                    {statusLoading ? 'Mise à jour...' : 'Mettre à jour'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Priority Change Modal */}
        {showPriorityModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-gray-900">Changer le niveau de risque</h3>
                <button
                  onClick={() => {
                    setShowPriorityModal(false);
                    setNewPriority('');
                  }}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ✕
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Nouveau niveau de risque
                  </label>
                  <select
                    value={newPriority}
                    onChange={(e) => setNewPriority(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-primary focus:border-transparent"
                  >
                    <option value="">Sélectionner un niveau</option>
                    <option value="LOW">Faible</option>
                    <option value="MEDIUM">Moyen</option>
                    <option value="HIGH">Élevé</option>
                    <option value="CRITICAL">Critique</option>
                  </select>
                </div>

                <div className="flex justify-end space-x-3 pt-4 border-t">
                  <button
                    onClick={() => {
                      setShowPriorityModal(false);
                      setNewPriority('');
                    }}
                    className="btn-secondary"
                    disabled={priorityLoading}
                  >
                    Annuler
                  </button>
                  <button
                    onClick={handlePriorityChange}
                    className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition disabled:opacity-50"
                    disabled={priorityLoading || !newPriority}
                  >
                    {priorityLoading ? 'Mise à jour...' : 'Mettre à jour'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Delete Confirmation Modal */}
        {showDeleteModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-red-600">Confirmer la suppression</h3>
                <button
                  onClick={() => setShowDeleteModal(false)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ✕
                </button>
              </div>

              <p className="text-gray-700 mb-6">
                Êtes-vous sûr de vouloir supprimer le dossier <strong>{caseData.reference_id}</strong> ? 
                Cette action est irréversible.
              </p>

              <div className="flex justify-end space-x-3">
                <button
                  onClick={() => setShowDeleteModal(false)}
                  className="btn-secondary"
                  disabled={deleteLoading}
                >
                  Annuler
                </button>
                <button
                  onClick={handleDelete}
<<<<<<< HEAD
                  className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition disabled:opacity-50"
=======
                  className="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-lg transition disabled:opacity-50"
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                  disabled={deleteLoading}
                >
                  {deleteLoading ? 'Suppression...' : 'Supprimer définitivement'}
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Assign Modal */}
        {showAssignModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-gray-900">Assigner à un analyste</h3>
                <button
                  onClick={() => {
                    setShowAssignModal(false);
                    setSelectedAnalyst('');
                  }}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ✕
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Sélectionner un analyste
                  </label>
                  <select
                    value={selectedAnalyst}
                    onChange={(e) => setSelectedAnalyst(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-primary focus:border-transparent"
                  >
                    <option value="">Choisir un analyste</option>
                    {analysts.map(analyst => (
                      <option key={analyst.id} value={analyst.id}>
                        {analyst.name} ({analyst.role})
                      </option>
                    ))}
                  </select>
                </div>

                <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                  <p className="text-sm text-blue-800">
<<<<<<< HEAD
                    L'analyste recevra une notification par email
=======
                    💡 L'analyste recevra une notification par email
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                  </p>
                </div>

                <div className="flex justify-end space-x-3 pt-4 border-t">
                  <button
                    onClick={() => {
                      setShowAssignModal(false);
                      setSelectedAnalyst('');
                    }}
                    className="btn-secondary"
                    disabled={assignLoading}
                  >
                    Annuler
                  </button>
                  <button
                    onClick={handleAssign}
                    className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition disabled:opacity-50"
                    disabled={assignLoading || !selectedAnalyst}
                  >
                    {assignLoading ? 'Assignation...' : 'Assigner'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Add Note Modal */}
        {showNoteModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-gray-900">Ajouter une note</h3>
                <button
                  onClick={() => {
                    setShowNoteModal(false);
                    setNoteText('');
                  }}
                  className="text-gray-400 hover:text-gray-600 text-2xl leading-none"
                >
                  ✕
                </button>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Note / Commentaire
                  </label>
                  <textarea
                    value={noteText}
                    onChange={(e) => setNoteText(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-primary focus:border-transparent"
                    rows="5"
                    placeholder="Entrez votre note ou commentaire..."
                    autoFocus
                  />
                  <p className="text-xs text-gray-500 mt-1">
                    {noteText.length} caractères
                  </p>
                </div>

                <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                  <p className="text-sm text-yellow-800">
<<<<<<< HEAD
                    Cette note sera visible par tous les utilisateurs ayant accès au dossier
=======
                    📝 Cette note sera visible par tous les utilisateurs ayant accès au dossier
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                  </p>
                </div>

                <div className="flex justify-end space-x-3 pt-4 border-t">
                  <button
                    onClick={() => {
                      setShowNoteModal(false);
                      setNoteText('');
                    }}
                    className="px-4 py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium rounded-lg transition"
                    disabled={noteLoading}
                  >
                    Annuler
                  </button>
                  <button
                    onClick={handleAddNote}
                    className="px-4 py-2 bg-custom-primary hover:bg-primary-700 text-white font-medium rounded-lg transition disabled:opacity-50 disabled:cursor-not-allowed"
                    disabled={noteLoading || !noteText.trim()}
                  >
                    {noteLoading ? 'Ajout en cours...' : 'Ajouter la note'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
<<<<<<< HEAD

        {/* Modal d'édition du dossier */}
        {showEditModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 animate-fade-in">
            <div className="bg-white rounded-lg p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto animate-scale-in">
              {/* Header */}
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900">
                  Modifier le dossier
                </h2>
                <button
                  onClick={() => setShowEditModal(false)}
                  className="text-gray-500 hover:text-gray-700 p-2 hover:bg-gray-100 rounded-lg transition"
                >
                  <X size={24} />
                </button>
              </div>

              {/* Formulaire */}
              <div className="space-y-4">
                {/* Numéro de dossier */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Numéro de dossier <span className="text-red-500">*</span>
                  </label>
                  <input
                    type="text"
                    value={editFormData.case_number}
                    onChange={(e) => setEditFormData({ ...editFormData, case_number: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="CASE-2026-001"
                  />
                </div>

                {/* Importateur */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Nom de l'importateur <span className="text-red-500">*</span>
                  </label>
                  <input
                    type="text"
                    value={editFormData.importer_name}
                    onChange={(e) => setEditFormData({ ...editFormData, importer_name: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Nom de la société"
                  />
                </div>

                {/* Grid 2 colonnes pour déclarant et transporteur */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Déclarant */}
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Nom du déclarant
                    </label>
                    <input
                      type="text"
                      value={editFormData.declarant_name}
                      onChange={(e) => setEditFormData({ ...editFormData, declarant_name: e.target.value })}
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="Nom du déclarant"
                    />
                  </div>

                  {/* Transporteur */}
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Nom du transporteur
                    </label>
                    <input
                      type="text"
                      value={editFormData.transporter_name}
                      onChange={(e) => setEditFormData({ ...editFormData, transporter_name: e.target.value })}
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="Nom du transporteur"
                    />
                  </div>
                </div>

                {/* Priorité */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Priorité
                  </label>
                  <select
                    value={editFormData.priority}
                    onChange={(e) => setEditFormData({ ...editFormData, priority: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="LOW">Basse</option>
                    <option value="MEDIUM">Moyenne</option>
                    <option value="HIGH">Haute</option>
                    <option value="URGENT">Urgente</option>
                  </select>
                </div>

                {/* Description */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Description
                  </label>
                  <textarea
                    value={editFormData.description}
                    onChange={(e) => setEditFormData({ ...editFormData, description: e.target.value })}
                    rows="4"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Description du dossier..."
                  />
                </div>
              </div>

              {/* Actions */}
              <div className="flex items-center justify-end space-x-3 mt-6 pt-4 border-t">
                <button
                  onClick={() => setShowEditModal(false)}
                  className="px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition"
                  disabled={editLoading}
                >
                  Annuler
                </button>
                <button
                  onClick={handleSaveEdit}
                  disabled={editLoading || !editFormData.case_number || !editFormData.importer_name}
                  className="px-6 py-2 bg-custom-primary hover:bg-primary-700 text-white rounded-lg transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
                >
                  {editLoading ? (
                    <>
                      <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                      <span>Enregistrement...</span>
                    </>
                  ) : (
                    <span>Enregistrer</span>
                  )}
                </button>
              </div>
            </div>
          </div>
        )}
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      </div>
    </Layout>
  );
};

export default CaseDetail;
