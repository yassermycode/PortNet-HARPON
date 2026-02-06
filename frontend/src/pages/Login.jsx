import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { Lock, User, AlertCircle } from 'lucide-react';
<<<<<<< HEAD
import { toast } from 'react-toastify';
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    const result = await login(username, password);
    
    if (result.success) {
<<<<<<< HEAD
      toast.success('Connexion réussie !');
      navigate('/');
    } else {
      setError(result.error);
      toast.error(result.error || 'Erreur de connexion');
=======
      navigate('/');
    } else {
      setError(result.error);
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    }
    
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-600 to-primary-900 px-4">
<<<<<<< HEAD
      <div className="max-w-md w-full space-y-6">
        {/* Logo - Centré et au-dessus du formulaire */}
        <div className="text-center">
          <div className="flex justify-center mb-4">
            <img 
              src="/portnet-logo.png" 
              alt="PortNet Logo" 
              className="h-20 w-auto"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextSibling.style.display = 'flex';
              }}
            />
            <div className="hidden items-center justify-center w-20 h-20 bg-white rounded-2xl">
              <span className="text-primary-600 font-bold text-4xl">PN</span>
            </div>
          </div>
=======
      <div className="max-w-md w-full">
        {/* Logo */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-white rounded-2xl mb-4">
            <span className="text-primary-600 font-bold text-3xl">PH</span>
          </div>
          <h1 className="text-3xl font-bold text-white mb-2">PortNet-HARPON</h1>
          <p className="text-primary-200">Système de détection de fraude douanière</p>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        </div>

        {/* Formulaire */}
        <div className="card">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Connexion</h2>
          
          {error && (
            <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg flex items-start space-x-2">
              <AlertCircle className="text-red-600 mt-0.5" size={20} />
              <p className="text-red-800 text-sm">{error}</p>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            {/* Username */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Nom d'utilisateur
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <User className="text-gray-400" size={20} />
                </div>
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="input pl-10"
                  placeholder="admin"
                  required
                  autoFocus
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Mot de passe
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Lock className="text-gray-400" size={20} />
                </div>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="input pl-10"
                  placeholder="••••••••"
                  required
                />
              </div>
            </div>

            {/* Submit */}
            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Connexion...' : 'Se connecter'}
            </button>
          </form>
<<<<<<< HEAD
=======

          {/* Info */}
          <div className="mt-6 p-4 bg-blue-50 rounded-lg">
            <p className="text-sm text-blue-800 font-medium mb-2">🔐 Compte de démonstration :</p>
            <p className="text-sm text-blue-700">
              Username: <code className="bg-blue-100 px-2 py-0.5 rounded">admin</code><br />
              Password: <code className="bg-blue-100 px-2 py-0.5 rounded">admin123</code>
            </p>
          </div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        </div>
      </div>
    </div>
  );
};

export default Login;
