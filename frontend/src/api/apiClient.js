import axios from 'axios';

<<<<<<< HEAD
export const API_BASE_URL = 'http://127.0.0.1:8001';
=======
const API_BASE_URL = 'http://127.0.0.1:8001';
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

console.warn('🚀 API CLIENT LOADED - Backend:', API_BASE_URL);

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
});

api.interceptors.request.use(config => {
  console.log('📤 REQUEST:', config.method.toUpperCase(), API_BASE_URL + config.url);
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  response => {
    console.log('✅ RESPONSE:', response.status, response.config.url);
    return response;
  },
  error => {
    console.error('❌ ERROR:', error.message, error.response?.status);
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const authAPI = {
  login: (credentials) => api.post('/api/v1/auth/login', credentials),
  getCurrentUser: () => api.get('/api/v1/auth/me'),
};

export const casesAPI = {
  getAll: (params) => api.get('/api/v1/cases/', { params }),
  getById: (id) => api.get(`/api/v1/cases/${id}`),
  create: (data) => api.post('/api/v1/cases/', data),
<<<<<<< HEAD
  update: (id, data) => api.put(`/api/v1/cases/${id}`, data),
  delete: (id) => api.delete(`/api/v1/cases/${id}`),
  updateStatus: (id, status) => api.patch(`/api/v1/cases/${id}/status`, { status }),
  updatePriority: (id, priority) => api.patch(`/api/v1/cases/${id}/priority`, { priority }),
  getStats: () => api.get('/api/v1/cases/stats'),
  getRiskDistribution: () => api.get('/api/v1/cases/risk-distribution'),
  approveCase: (caseId) => api.post(`/api/v1/cases/${caseId}/approve`),
  getArchives: (params = {}) => api.get('/api/v1/cases/archives', { params }),
  usersAPI: {
    getMyProfile: () => api.get('/api/v1/users/me'),
    updateMyProfile: (data) => api.put('/api/v1/users/me', data),
    uploadAvatar: (file) => {
      const formData = new FormData();
      formData.append('file', file);
      return api.post('/api/v1/users/me/avatar', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
    },
  },
=======
  updateStatus: (id, status) => api.patch(`/api/v1/cases/${id}/status`, { status }),
  updatePriority: (id, priority) => api.patch(`/api/v1/cases/${id}/priority`, { priority }),
  getStats: () => api.get('/api/v1/cases/stats'),
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
};

export const documentsAPI = {
  upload: (caseId, file) => {
<<<<<<< HEAD
    console.log('📤 UPLOAD - Case ID:', caseId, '| Fichier:', file.name, '| Taille:', file.size);
    console.log('📤 UPLOAD - URL complète:', `${API_BASE_URL}/api/v1/cases/${caseId}/documents`);
    const formData = new FormData();
    formData.append('file', file);
    // Ne pas définir Content-Type manuellement - le navigateur le fait automatiquement avec le boundary
    return api.post(`/api/v1/cases/${caseId}/documents`, formData, {
=======
    const formData = new FormData();
    formData.append('file', file);
    return api.post(`/api/v1/cases/${caseId}/documents`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      timeout: 60000,
    });
  },
  getAll: (caseId) => api.get(`/api/v1/cases/${caseId}/documents`),
  getById: (id) => api.get(`/api/v1/documents/${id}`),
  analyze: (id) => api.post(`/api/v1/documents/${id}/analyze`),
  delete: (id) => api.delete(`/api/v1/documents/${id}`),
};

export const notesAPI = {
  create: (caseId, data) => api.post(`/api/v1/cases/${caseId}/notes`, data),
  getAll: (caseId) => api.get(`/api/v1/cases/${caseId}/notes`),
  delete: (id) => api.delete(`/api/v1/notes/${id}`),
};

export default api;
