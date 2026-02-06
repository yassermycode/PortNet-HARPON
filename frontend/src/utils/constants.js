export const ROLES = {
  ADMIN: 'ADMIN',
  ANALYST: 'ANALYST',
  VIEWER: 'VIEWER',
};

// Statuts du backend
export const CASE_STATUS = {
  PENDING: 'PENDING',
  FLAGGED: 'FLAGGED',
  CLEAN: 'CLEAN',
  INSPECTED: 'INSPECTED',
};

// Niveaux de risque du backend (risk_level)
export const RISK_LEVEL = {
  LOW: 'LOW',
  MEDIUM: 'MEDIUM',
  HIGH: 'HIGH',
  CRITICAL: 'CRITICAL',
};

// Actions recommandées du backend
export const RECOMMENDED_ACTION = {
  RELEASE: 'RELEASE',
  INSPECT: 'INSPECT',
  SEIZE: 'SEIZE',
};

// Labels français pour les statuts
export const STATUS_LABELS = {
  PENDING: 'En attente',
  FLAGGED: 'Signalé',
  CLEAN: 'Clean',
  INSPECTED: 'Inspecté',
};

// Labels français pour les niveaux de risque
export const RISK_LEVEL_LABELS = {
  LOW: 'Faible',
  MEDIUM: 'Moyen',
  HIGH: 'Élevé',
  CRITICAL: 'Critique',
};

// Labels français pour les actions recommandées
export const ACTION_LABELS = {
  RELEASE: 'Libérer',
  INSPECT: 'Inspecter',
  SEIZE: 'Saisir',
};

// Couleurs pour les statuts
export const STATUS_COLORS = {
  PENDING: 'bg-yellow-100 text-yellow-800',
  FLAGGED: 'bg-red-100 text-red-800',
  CLEAN: 'bg-green-100 text-green-800',
  INSPECTED: 'bg-blue-100 text-blue-800',
};

// Couleurs pour les niveaux de risque
export const RISK_LEVEL_COLORS = {
  LOW: 'bg-gray-100 text-gray-800',
  MEDIUM: 'bg-blue-100 text-blue-800',
  HIGH: 'bg-orange-100 text-orange-800',
  CRITICAL: 'bg-red-100 text-red-800',
};

// Couleurs pour les actions recommandées
export const ACTION_COLORS = {
  RELEASE: 'bg-green-100 text-green-800',
  INSPECT: 'bg-orange-100 text-orange-800',
  SEIZE: 'bg-red-100 text-red-800',
};

// Alias pour compatibilité (anciens noms)
export const CASE_PRIORITY = RISK_LEVEL;
export const PRIORITY_LABELS = RISK_LEVEL_LABELS;
export const PRIORITY_COLORS = RISK_LEVEL_COLORS;
