import axios from 'axios';

// ========================================
// CONFIGURATION DE L'URL DU BACKEND
// ========================================
const BACKEND_URL = 'http://127.0.0.1:8001';

console.log('🌐 ========================================');
console.log('🌐 API CLIENT INITIALISÉ');
console.log('🌐 Backend URL:', BACKEND_URL);
console.log('🌐 ========================================');

const apiClient = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000,
});

// Intercepteur REQUEST
apiClient.interceptors.request.use(
  (config) => {
    console.log('📤 ========================================');
    console.log('📤 REQUÊTE ENVOYÉE');
    console.log('📤 Method:', config.method.toUpperCase());
    console.log('📤 URL complète:', config.baseURL + config.url);
    console.log('📤 Data:', config.data);
    console.log('📤 ========================================');
    
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
      console.log('🔑 Token ajouté');
    }
    return config;
  },
  (error) => {
    console.error('❌ ERREUR REQUEST INTERCEPTOR:', error);
    return Promise.reject(error);
  }
);

// Intercepteur RESPONSE
apiClient.interceptors.response.use(
  (response) => {
    console.log('✅ ========================================');
    console.log('✅ RÉPONSE REÇUE');
    console.log('✅ Status:', response.status);
    console.log('✅ Data:', response.data);
    console.log('✅ ========================================');
    return response;
  },
  (error) => {
    console.error('❌ ========================================');
    console.error('❌ ERREUR RÉPONSE');
    console.error('❌ Message:', error.message);
    console.error('❌ Code:', error.code);
    console.error('❌ Response:', error.response);
    console.error('❌ ========================================');
    
    if (error.response?.status === 401) {
      console.log('🔴 Token expiré - Redirection login');
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default apiClient;

// ========================================
// API AUTH
// ========================================
export const authAPI = {
  login: (credentials) => {
    console.log('🔐 ========================================');
    console.log('🔐 TENTATIVE DE LOGIN');
    console.log('🔐 Username:', credentials.username);
    console.log('🔐 URL:', BACKEND_URL + '/api/v1/auth/login');
    console.log('🔐 ========================================');
    return apiClient.post('/api/v1/auth/login', credentials);
  },
  getCurrentUser: () => apiClient.get('/api/v1/auth/me'),
};

// ========================================
// API CASES
// ========================================
export const casesAPI = {
  getAll: (params) => apiClient.get('/api/v1/cases/', { params }),
  getById: (id) => apiClient.get(`/api/v1/cases/${id}`),
  create: (caseData) => apiClient.post('/api/v1/cases/', caseData),
  updateStatus: (id, status) => apiClient.patch(`/api/v1/cases/${id}/status`, { status }),
  updatePriority: (id, priority) => apiClient.patch(`/api/v1/cases/${id}/priority`, { priority }),
  getStats: () => apiClient.get('/api/v1/cases/stats'),
};

// ========================================
// API DOCUMENTS
// ========================================
export const documentsAPI = {
  upload: (caseId, file) => {
    const formData = new FormData();
    formData.append('file', file);
    console.log('📤 Upload document - Case:', caseId, '- File:', file.name);
    return apiClient.post(`/api/v1/cases/${caseId}/documents`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      timeout: 60000,
    });
  },
  getAll: (caseId) => apiClient.get(`/api/v1/cases/${caseId}/documents`),
  getById: (documentId) => apiClient.get(`/api/v1/documents/${documentId}`),
  analyze: (documentId) => apiClient.post(`/api/v1/documents/${documentId}/analyze`),
  delete: (documentId) => apiClient.delete(`/api/v1/documents/${documentId}`),
};

// ========================================
// API NOTES
// ========================================
export const notesAPI = {
  create: (caseId, noteData) => apiClient.post(`/api/v1/cases/${caseId}/notes`, noteData),
  getAll: (caseId) => apiClient.get(`/api/v1/cases/${caseId}/notes`),
  delete: (noteId) => apiClient.delete(`/api/v1/notes/${noteId}`),
};
