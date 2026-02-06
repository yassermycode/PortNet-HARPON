<<<<<<< HEAD
import { Calendar, AlertCircle, Target, FileDown } from 'lucide-react';
import { STATUS_LABELS, RISK_LEVEL_LABELS, ACTION_LABELS, STATUS_COLORS, RISK_LEVEL_COLORS, ACTION_COLORS } from '../../utils/constants';

const CaseCard = ({ caseData, onClick, onExportPDF }) => {
=======
import { Calendar, AlertCircle, Target } from 'lucide-react';
import { STATUS_LABELS, RISK_LEVEL_LABELS, ACTION_LABELS, STATUS_COLORS, RISK_LEVEL_COLORS, ACTION_COLORS } from '../../utils/constants';

const CaseCard = ({ caseData, onClick }) => {
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  return (
    <div
      onClick={onClick}
      className="card hover:shadow-xl transition cursor-pointer border-l-4 hover:border-l-custom-primary"
      style={{ borderLeftColor: caseData.risk_level === 'CRITICAL' ? 'rgb(220, 38, 38)' : 'transparent' }}
    >
      <div className="flex justify-between items-start mb-4">
        <div className="flex-1">
          <h3 className="text-lg font-bold text-gray-900 mb-1 hover:text-custom-primary transition">
            {caseData.reference_id || `CASE-${caseData.id}`}
          </h3>
          <p className="text-sm text-gray-600">
            Score global: <span className="font-semibold">{caseData.global_score || 0}/100</span>
          </p>
        </div>
        
        {/* Risk Level Badge */}
        {caseData.risk_level && (
          <span className={`px-3 py-1 rounded-full text-xs font-medium ${RISK_LEVEL_COLORS[caseData.risk_level]}`}>
            {RISK_LEVEL_LABELS[caseData.risk_level] || caseData.risk_level}
          </span>
        )}
      </div>

      {/* Status & Action */}
      <div className="flex items-center justify-between mb-3 gap-2">
        <span className={`px-3 py-1 rounded-full text-xs font-medium ${STATUS_COLORS[caseData.status]}`}>
          {STATUS_LABELS[caseData.status] || caseData.status}
        </span>
        
        {caseData.recommended_action && (
          <div className="flex items-center space-x-1">
            <Target size={14} className="text-gray-600" />
            <span className={`px-2 py-1 rounded text-xs font-medium ${ACTION_COLORS[caseData.recommended_action]}`}>
              {ACTION_LABELS[caseData.recommended_action] || caseData.recommended_action}
            </span>
          </div>
        )}
      </div>

      {/* Risk Score Bar */}
      {caseData.global_score !== undefined && (
        <div className="mb-3">
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className={`h-2 rounded-full transition-all ${
                caseData.global_score > 70 ? 'bg-red-600' :
                caseData.global_score > 40 ? 'bg-orange-600' : 'bg-green-600'
              }`}
              style={{ width: `${caseData.global_score}%` }}
            ></div>
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="flex items-center justify-between text-xs text-gray-500 pt-3 border-t border-gray-100">
        <div className="flex items-center space-x-1">
          <Calendar size={14} />
          <span>{formatDate(caseData.created_at)}</span>
        </div>
        
<<<<<<< HEAD
        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-1">
            <AlertCircle 
              size={14} 
              className={caseData.global_score > 70 ? 'text-red-600' : caseData.global_score > 40 ? 'text-orange-600' : 'text-green-600'}
            />
            <span>ID: {caseData.id}</span>
          </div>
          
          {onExportPDF && (
            <button
              onClick={(e) => {
                e.stopPropagation();
                onExportPDF(caseData.id, e);
              }}
              className="p-1.5 text-custom-primary hover:bg-primary-50 rounded-lg transition"
              title="Exporter en PDF"
            >
              <FileDown size={16} />
            </button>
          )}
=======
        <div className="flex items-center space-x-1">
          <AlertCircle 
            size={14} 
            className={caseData.global_score > 70 ? 'text-red-600' : caseData.global_score > 40 ? 'text-orange-600' : 'text-green-600'}
          />
          <span>ID: {caseData.id}</span>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        </div>
      </div>
    </div>
  );
};

export default CaseCard;
