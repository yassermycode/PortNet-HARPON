import { useState } from 'react';
import { X } from 'lucide-react';
import { CASE_PRIORITY } from '../../utils/constants';

const CreateCaseForm = ({ onClose, onSubmit, loading }) => {
  const [formData, setFormData] = useState({
    case_number: '',
    importer_name: '',
    declarant_name: '',
    transporter_name: '',
    priority: 'MEDIUM',
    description: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b bg-custom-primary">
          <h2 className="text-2xl font-bold text-white">Créer un nouveau dossier</h2>
          <button
            onClick={onClose}
            className="text-white hover:bg-white hover:bg-opacity-20 p-2 rounded-lg transition"
          >
            <X size={24} />
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          {/* Case Number */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Numéro de dossier <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="case_number"
              value={formData.case_number}
              onChange={handleChange}
              className="input focus:ring-custom-primary focus:border-custom-primary"
              placeholder="CASE-2024-001"
              required
            />
          </div>

          {/* Importer Name */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nom de l'importateur <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="importer_name"
              value={formData.importer_name}
              onChange={handleChange}
              className="input focus:ring-custom-primary focus:border-custom-primary"
              placeholder="ABC Import"
              required
            />
          </div>

          {/* Declarant Name */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nom du déclarant
            </label>
            <input
              type="text"
              name="declarant_name"
              value={formData.declarant_name}
              onChange={handleChange}
              className="input focus:ring-custom-primary focus:border-custom-primary"
              placeholder="XYZ Customs Broker"
            />
          </div>

          {/* Transporter Name */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nom du transporteur
            </label>
            <input
              type="text"
              name="transporter_name"
              value={formData.transporter_name}
              onChange={handleChange}
              className="input focus:ring-custom-primary focus:border-custom-primary"
              placeholder="Fast Logistics"
            />
          </div>

          {/* Priority */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Priorité <span className="text-red-500">*</span>
            </label>
            <select
              name="priority"
              value={formData.priority}
              onChange={handleChange}
              className="input focus:ring-custom-primary focus:border-custom-primary"
              required
            >
              {Object.values(CASE_PRIORITY).map(priority => (
                <option key={priority} value={priority}>{priority}</option>
              ))}
            </select>
          </div>

          {/* Description */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              name="description"
              value={formData.description}
              onChange={handleChange}
              className="input focus:ring-custom-primary focus:border-custom-primary"
              rows="4"
              placeholder="Détails du dossier..."
            />
          </div>

          {/* Actions */}
          <div className="flex justify-end space-x-3 pt-4 border-t">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium rounded-lg transition"
              disabled={loading}
            >
              Annuler
            </button>
            <button
              type="submit"
              className="bg-custom-primary hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition duration-200 disabled:opacity-50"
              disabled={loading}
            >
              {loading ? 'Création...' : 'Créer le dossier'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateCaseForm;
