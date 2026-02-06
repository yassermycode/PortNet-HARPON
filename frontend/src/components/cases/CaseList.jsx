<<<<<<< HEAD
import { useState, useEffect } from 'react';
import CaseCard from './CaseCard';
import { Search, Filter, ChevronUp, ChevronDown, ChevronsUpDown } from 'lucide-react';
import { CASE_STATUS, RISK_LEVEL, STATUS_LABELS, RISK_LEVEL_LABELS } from '../../utils/constants';

const CaseList = ({ cases, onCaseClick, onExportPDF, loading }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('ALL');
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(9);
  
  // Sorting state
  const [sortField, setSortField] = useState('created_at');
  const [sortDirection, setSortDirection] = useState('desc');

  // Reset to page 1 when filters change
  useEffect(() => {
    setCurrentPage(1);
  }, [searchTerm, statusFilter]);
=======
import { useState } from 'react';
import CaseCard from './CaseCard';
import { Search, Filter } from 'lucide-react';
import { CASE_STATUS, RISK_LEVEL, STATUS_LABELS, RISK_LEVEL_LABELS } from '../../utils/constants';

const CaseList = ({ cases, onCaseClick, loading }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('ALL');
  const [riskFilter, setRiskFilter] = useState('ALL');
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

  const filteredCases = cases.filter(caseItem => {
    const matchesSearch = 
      !searchTerm ||
      caseItem.reference_id?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      caseItem.id?.toString().includes(searchTerm);
    
    const matchesStatus = statusFilter === 'ALL' || caseItem.status === statusFilter;
<<<<<<< HEAD
    
    return matchesSearch && matchesStatus;
  });

  // Sorting function
  const handleSort = (field) => {
    if (sortField === field) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortDirection('asc');
    }
    setCurrentPage(1);
  };

  const sortedCases = [...filteredCases].sort((a, b) => {
    let aValue = a[sortField];
    let bValue = b[sortField];

    if (aValue === null || aValue === undefined) return 1;
    if (bValue === null || bValue === undefined) return -1;

    if (sortField === 'global_score' || sortField === 'risk_score') {
      aValue = Number(aValue) || 0;
      bValue = Number(bValue) || 0;
    }

    if (sortField === 'created_at' || sortField === 'updated_at') {
      aValue = new Date(aValue);
      bValue = new Date(bValue);
    }

    if (typeof aValue === 'string') {
      aValue = aValue.toLowerCase();
      bValue = bValue.toLowerCase();
    }

    if (aValue < bValue) return sortDirection === 'asc' ? -1 : 1;
    if (aValue > bValue) return sortDirection === 'asc' ? 1 : -1;
    return 0;
  });

  // Pagination calculation
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentCases = sortedCases.slice(indexOfFirstItem, indexOfLastItem);
  const totalPages = Math.ceil(sortedCases.length / itemsPerPage);

  // Sort field labels
  const getSortFieldLabel = (field) => {
    const labels = {
      reference_id: 'Référence',
      status: 'Statut',
      risk_level: 'Niveau de risque',
      global_score: 'Score global',
      created_at: 'Date de création',
      updated_at: 'Dernière mise à jour'
    };
    return labels[field] || field;
  };

  // Sortable button component
  const SortButton = ({ field, children }) => {
    const isActive = sortField === field;
    return (
      <button
        onClick={() => handleSort(field)}
        className={`px-3 py-1.5 rounded-lg text-xs font-medium transition flex items-center space-x-1 ${
          isActive 
            ? 'bg-custom-primary text-white' 
            : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
        }`}
      >
        <span>{children}</span>
        {isActive && sortDirection === 'asc' ? (
          <ChevronUp size={14} />
        ) : isActive && sortDirection === 'desc' ? (
          <ChevronDown size={14} />
        ) : (
          <ChevronsUpDown size={14} className="opacity-50" />
        )}
      </button>
    );
  };

=======
    const matchesRisk = riskFilter === 'ALL' || caseItem.risk_level === riskFilter;
    
    return matchesSearch && matchesStatus && matchesRisk;
  });

>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-custom-primary"></div>
      </div>
    );
  }

  return (
<<<<<<< HEAD
    <div className="space-y-6 animate-fade-in">
      {/* Filters */}
      <div className="card">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
=======
    <div className="space-y-6">
      {/* Filters */}
      <div className="card">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
          {/* Search */}
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <Search className="text-gray-400" size={20} />
            </div>
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="input pl-10 focus:ring-custom-primary focus:border-custom-primary"
              placeholder="Rechercher..."
            />
          </div>

          {/* Status Filter */}
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <Filter className="text-gray-400" size={20} />
            </div>
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className={`input pl-10 focus:ring-custom-primary focus:border-custom-primary ${statusFilter !== 'ALL' ? 'text-custom-primary font-medium' : ''}`}
            >
              <option value="ALL">Tous les statuts</option>
              {Object.entries(STATUS_LABELS).map(([key, label]) => (
                <option key={key} value={key}>{label}</option>
              ))}
            </select>
          </div>

<<<<<<< HEAD

        </div>

        {/* Sorting Options */}
        <div className="flex flex-wrap items-center gap-2 pt-4 border-t">
          <span className="text-sm text-gray-500">Trier par :</span>
          <SortButton field="created_at">Date</SortButton>
          <SortButton field="status">Statut</SortButton>
          <SortButton field="global_score">Score</SortButton>
          <SortButton field="risk_level">Risque</SortButton>
        </div>
      </div>

      {/* Results Count & Sorting Info */}
      <div className="flex items-center justify-between">
        <p className="text-sm text-gray-600">
          <span className="font-semibold text-custom-primary">
            {sortedCases.length}
          </span> dossier(s) trouvé(s)
          {totalPages > 1 && (
            <span className="ml-2 text-gray-400">
              • Page {currentPage} sur {totalPages}
            </span>
          )}
        </p>
        <p className="text-sm text-gray-500">
          Tri : <span className="font-medium">{getSortFieldLabel(sortField)}</span>
          {' '}({sortDirection === 'asc' ? '↑ Croissant' : '↓ Décroissant'})
=======
          {/* Risk Level Filter */}
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <Filter className="text-gray-400" size={20} />
            </div>
            <select
              value={riskFilter}
              onChange={(e) => setRiskFilter(e.target.value)}
              className={`input pl-10 focus:ring-custom-primary focus:border-custom-primary ${riskFilter !== 'ALL' ? 'text-custom-primary font-medium' : ''}`}
            >
              <option value="ALL">Tous les niveaux de risque</option>
              {Object.entries(RISK_LEVEL_LABELS).map(([key, label]) => (
                <option key={key} value={key}>{label}</option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Results Count */}
      <div className="flex items-center justify-between">
        <p className="text-sm text-gray-600">
          <span className="font-semibold text-custom-primary">
            {filteredCases.length}
          </span> dossier(s) trouvé(s)
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        </p>
      </div>

      {/* Cases Grid */}
<<<<<<< HEAD
      {sortedCases.length === 0 ? (
=======
      {filteredCases.length === 0 ? (
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
        <div className="card text-center py-12">
          <p className="text-gray-500">Aucun dossier trouvé</p>
        </div>
      ) : (
<<<<<<< HEAD
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {currentCases.map((caseItem) => (
              <CaseCard
                key={caseItem.id}
                caseData={caseItem}
                onClick={() => onCaseClick(caseItem.id)}
                onExportPDF={onExportPDF}
              />
            ))}
          </div>

          {/* Pagination */}
          {totalPages > 1 && (
            <div className="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4">
              {/* Info */}
              <div className="text-sm text-gray-700">
                Affichage de <span className="font-medium">{indexOfFirstItem + 1}</span> à{' '}
                <span className="font-medium">
                  {Math.min(indexOfLastItem, sortedCases.length)}
                </span>{' '}
                sur <span className="font-medium">{sortedCases.length}</span> dossiers
              </div>

              {/* Pagination Buttons */}
              <div className="flex items-center space-x-2">
                {/* Previous Button */}
                <button
                  onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
                  disabled={currentPage === 1}
                  className={`px-3 py-2 rounded-lg font-medium transition ${
                    currentPage === 1
                      ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                      : 'bg-white border border-gray-300 text-gray-700 hover:bg-gray-50'
                  }`}
                >
                  ← Précédent
                </button>

                {/* Page Numbers */}
                <div className="flex items-center space-x-1">
                  {[...Array(totalPages)].map((_, index) => {
                    const pageNumber = index + 1;
                    
                    if (
                      pageNumber === 1 ||
                      pageNumber === totalPages ||
                      (pageNumber >= currentPage - 1 && pageNumber <= currentPage + 1)
                    ) {
                      return (
                        <button
                          key={pageNumber}
                          onClick={() => setCurrentPage(pageNumber)}
                          className={`w-10 h-10 rounded-lg font-medium transition ${
                            currentPage === pageNumber
                              ? 'bg-custom-primary text-white'
                              : 'bg-white border border-gray-300 text-gray-700 hover:bg-gray-50'
                          }`}
                        >
                          {pageNumber}
                        </button>
                      );
                    } else if (
                      pageNumber === currentPage - 2 ||
                      pageNumber === currentPage + 2
                    ) {
                      return <span key={pageNumber} className="text-gray-400 px-1">...</span>;
                    }
                    return null;
                  })}
                </div>

                {/* Next Button */}
                <button
                  onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
                  disabled={currentPage === totalPages}
                  className={`px-3 py-2 rounded-lg font-medium transition ${
                    currentPage === totalPages
                      ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                      : 'bg-white border border-gray-300 text-gray-700 hover:bg-gray-50'
                  }`}
                >
                  Suivant →
                </button>
              </div>
            </div>
          )}
        </>
=======
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCases.map((caseItem) => (
            <CaseCard
              key={caseItem.id}
              caseData={caseItem}
              onClick={() => onCaseClick(caseItem.id)}
            />
          ))}
        </div>
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
      )}
    </div>
  );
};

export default CaseList;
