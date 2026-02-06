import { Link } from 'react-router-dom';
import { Home } from 'lucide-react';

const NotFound = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div className="text-center">
        <h1 className="text-9xl font-bold text-primary-600">404</h1>
        <h2 className="text-3xl font-bold text-gray-900 mt-4">Page non trouvée</h2>
        <p className="text-gray-600 mt-2 mb-8">
          Désolé, la page que vous recherchez n'existe pas.
        </p>
        <Link to="/" className="btn-primary inline-flex items-center space-x-2">
          <Home size={20} />
          <span>Retour à l'accueil</span>
        </Link>
      </div>
    </div>
  );
};

export default NotFound;
