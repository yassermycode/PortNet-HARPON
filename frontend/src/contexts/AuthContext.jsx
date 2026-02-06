import { createContext, useState, useEffect } from 'react';
import { authAPI } from '../api/apiClient';

export const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Vérifier si l'utilisateur est connecté au chargement
  useEffect(() => {
    const initAuth = async () => {
      const token = localStorage.getItem('token');
      const storedUser = localStorage.getItem('user');
      
      if (token && storedUser) {
        try {
          // Vérifier que le token est valide
          const response = await authAPI.getCurrentUser();
          setUser(response.data);
        } catch (error) {
          // Token invalide
          localStorage.removeItem('token');
          localStorage.removeItem('user');
          setUser(null);
        }
      }
      setLoading(false);
    };

    initAuth();
  }, []);

  const login = async (username, password) => {
    try {
      console.log('🔐 ========================================');
      console.log('🔐 AUTHCONTEXT LOGIN APPELÉ');
      console.log('🔐 Username:', username);
      console.log('🔐 ========================================');
      
      const response = await authAPI.login({ username, password });
      const { access_token } = response.data;
      
      console.log('✅ Token reçu:', access_token);
      
      // Sauvegarder le token
      localStorage.setItem('token', access_token);
      
      // Récupérer les infos utilisateur
      const userResponse = await authAPI.getCurrentUser();
      const userData = userResponse.data;
      
      console.log('✅ User data:', userData);
      
      localStorage.setItem('user', JSON.stringify(userData));
      setUser(userData);
      
      return { success: true };
    } catch (error) {
      console.error('❌ Login error:', error);
      console.error('❌ Response:', error.response);
      return { 
        success: false, 
        error: error.response?.data?.detail || 'Échec de la connexion' 
      };
    }
  };

  const logout = () => {
<<<<<<< HEAD
    localStorage.removeItem('token');
=======
    localStorage.removeItem('access_token');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    localStorage.removeItem('user');
    setUser(null);
  };

  const value = {
    user,
    login,
    logout,
    loading,
    isAuthenticated: !!user,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
