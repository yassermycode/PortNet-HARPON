import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../hooks/useAuth';
import { LogOut, User, LayoutDashboard, FolderOpen } from 'lucide-react';

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="bg-primary-600 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          {/* Logo et navigation */}
          <div className="flex items-center space-x-8">
<<<<<<< HEAD
            <Link to="/" className="flex items-center">
              <img 
                src="/portnet-logo.png" 
                alt="PortNet Logo" 
                className="h-10 w-auto"
                onError={(e) => {
                  e.target.style.display = 'none';
                  e.target.nextSibling.style.display = 'flex';
                }}
              />
              <div className="hidden w-8 h-8 bg-white rounded-lg items-center justify-center">
                <span className="text-primary-600 font-bold text-lg">PN</span>
              </div>
=======
            <Link to="/" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center">
                <span className="text-primary-600 font-bold text-xl">PH</span>
              </div>
              <span className="font-bold text-xl">PortNet-HARPON</span>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            </Link>

            {user && (
              <div className="hidden md:flex space-x-4">
                <Link
                  to="/"
                  className="flex items-center space-x-1 px-3 py-2 rounded-md hover:bg-primary-700 transition"
                >
                  <LayoutDashboard size={20} />
                  <span>Dashboard</span>
                </Link>
                <Link
                  to="/cases"
                  className="flex items-center space-x-1 px-3 py-2 rounded-md hover:bg-primary-700 transition"
                >
                  <FolderOpen size={20} />
                  <span>Dossiers</span>
                </Link>
<<<<<<< HEAD
                <Link
                  to="/archives"
                  className="flex items-center space-x-1 px-3 py-2 rounded-md hover:bg-primary-700 transition"
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4" />
                  </svg>
                  <span>Archives</span>
                </Link>
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
              </div>
            )}
          </div>

          {/* User menu */}
          {user && (
            <div className="flex items-center space-x-4">
<<<<<<< HEAD
              <Link
                to="/profile"
                className="flex items-center space-x-2 px-3 py-2 rounded-md hover:bg-primary-700 transition"
              >
                <User size={20} />
                <div className="text-sm text-left">
                  <p className="font-medium">{user.first_name && user.last_name ? `${user.first_name} ${user.last_name}` : user.full_name || 'Administrateur'}</p>
                  <p className="text-primary-200 text-xs">{user.position || 'ADMIN'}</p>
                </div>
              </Link>
=======
              <div className="flex items-center space-x-2">
                <User size={20} />
                <div className="text-sm">
                  <p className="font-medium">{user.full_name}</p>
                  <p className="text-primary-200 text-xs">{user.role}</p>
                </div>
              </div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
              <button
                onClick={handleLogout}
                className="flex items-center space-x-1 px-3 py-2 rounded-md hover:bg-primary-700 transition"
              >
                <LogOut size={20} />
                <span>Déconnexion</span>
              </button>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
