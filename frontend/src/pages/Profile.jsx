import React, { useState, useEffect, useRef } from 'react';
import { casesAPI, API_BASE_URL } from '../api/apiClient';
import Layout from '../components/layout/Layout';
import { User as UserIcon, Upload, Trash2 } from 'lucide-react';

const Profile = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState(false);
  const [formData, setFormData] = useState({});
  const [uploadingAvatar, setUploadingAvatar] = useState(false);
  const fileInputRef = useRef(null);

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      const response = await casesAPI.usersAPI.getMyProfile();
      setProfile(response.data);
      setFormData(response.data);
    } catch (error) {
      console.error('Erreur récupération profil:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAvatarChange = async (event) => {
    const file = event.target.files?.[0];
    if (!file) return;

    try {
      setUploadingAvatar(true);
      const response = await casesAPI.usersAPI.uploadAvatar(file);
      console.log('Avatar uploadé:', response.data);
      await fetchProfile();
      alert('Photo de profil mise à jour avec succès');
    } catch (error) {
      console.error('Erreur upload avatar:', error);
      alert('Erreur lors du téléchargement de la photo');
    } finally {
      setUploadingAvatar(false);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    }
  };

  const handleRemoveAvatar = async () => {
    if (!window.confirm('Êtes-vous sûr de vouloir supprimer votre photo de profil ?')) {
      return;
    }

    try {
      setUploadingAvatar(true);
      const updatedData = { ...formData, avatar_url: null };
      await casesAPI.usersAPI.updateMyProfile(updatedData);
      await fetchProfile();
      alert('Photo de profil supprimée');
    } catch (error) {
      console.error('Erreur suppression avatar:', error);
      alert('Erreur lors de la suppression de la photo');
    } finally {
      setUploadingAvatar(false);
    }
  };

  const handleSave = async () => {
    try {
      setLoading(true);
      await casesAPI.usersAPI.updateMyProfile(formData);
      alert('Profil mis à jour avec succès');
      setEditing(false);
      await fetchProfile();
    } catch (error) {
      console.error('Erreur mise à jour:', error);
      alert('Erreur lors de la mise à jour');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  if (loading) {
    return (
      <Layout>
        <div className="flex items-center justify-center min-h-screen">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-custom-primary"></div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="space-y-6">
        {/* En-tête */}
        <div className="bg-gradient-to-r from-custom-primary to-primary-700 rounded-lg p-8 mb-6 text-white">
          <div className="flex items-center space-x-6">
            {/* Avatar Upload */}
            <div className="relative">
              <input
                ref={fileInputRef}
                type="file"
                accept="image/jpeg,image/png,image/gif,image/webp"
                onChange={handleAvatarChange}
                disabled={uploadingAvatar}
                className="hidden"
              />
              <div className="w-24 h-24 bg-white rounded-full flex items-center justify-center text-4xl font-bold text-custom-primary overflow-hidden group">
                {profile?.avatar_url ? (
                  <img 
                    src={`${API_BASE_URL}${profile.avatar_url}`}
                    alt="Avatar"
                    className="w-full h-full object-cover group-hover:opacity-75 transition-opacity"
                  />
                ) : (
                  <span>{profile?.first_name?.[0] || profile?.username?.[0] || '?'}</span>
                )}
              </div>
              <button
                onClick={() => fileInputRef.current?.click()}
                disabled={uploadingAvatar}
                className="absolute bottom-0 right-0 bg-white text-custom-primary rounded-full p-2 shadow-lg hover:bg-gray-100 transition-colors disabled:opacity-50"
                title="Télécharger une photo"
              >
                <Upload size={16} />
              </button>
            </div>

            <div className="flex-1">
              <h1 className="text-3xl font-bold mb-2">
                {profile?.first_name && profile?.last_name
                  ? `${profile.first_name} ${profile.last_name}`
                  : profile?.full_name || profile?.username}
              </h1>
              <p className="text-primary-100 text-lg">{profile?.position || 'Agent Douanier'}</p>
              <p className="text-primary-200 text-sm mt-1">
                {profile?.badge_number && `N° ${profile.badge_number} `}
                {profile?.department || 'PortNet HARPON'}
              </p>
            </div>
            <div className="flex space-x-2">
              <button
                onClick={() => editing ? handleSave() : setEditing(true)}
                className="px-6 py-3 bg-white text-custom-primary rounded-lg font-semibold hover:bg-primary-50 transition-colors"
              >
                {editing ? 'Enregistrer' : 'Modifier'}
              </button>
              {editing && (
                <button
                  onClick={() => {
                    setEditing(false);
                    setFormData(profile);
                  }}
                  className="px-6 py-3 bg-red-500 text-white rounded-lg font-semibold hover:bg-red-600 transition-colors"
                >
                  Annuler
                </button>
              )}
              {profile?.avatar_url && (
                <button
                  onClick={handleRemoveAvatar}
                  disabled={uploadingAvatar}
                  className="px-4 py-3 bg-red-500/20 text-red-300 rounded-lg hover:bg-red-500/30 transition-colors disabled:opacity-50"
                  title="Supprimer la photo"
                >
                  <Trash2 size={20} />
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Informations personnelles */}
        <div className="bg-white rounded-lg border border-gray-200 p-6 mb-6">
          <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center">
            <UserIcon size={24} className="mr-2 text-custom-primary" />
            Informations Personnelles
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Prénom */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Prénom
              </label>
              {editing ? (
                <input
                  type="text"
                  value={formData.first_name || ''}
                  onChange={(e) => handleChange('first_name', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="Entrez votre prénom"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.first_name || 'Non renseigné'}
                </p>
              )}
            </div>

            {/* Nom */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Nom
              </label>
              {editing ? (
                <input
                  type="text"
                  value={formData.last_name || ''}
                  onChange={(e) => handleChange('last_name', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="Entrez votre nom"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.last_name || 'Non renseigné'}
                </p>
              )}
            </div>

            {/* Date de naissance */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Date de naissance
              </label>
              {editing ? (
                <input
                  type="date"
                  value={formData.birth_date || ''}
                  onChange={(e) => handleChange('birth_date', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.birth_date
                    ? new Date(profile.birth_date).toLocaleDateString('fr-FR')
                    : 'Non renseignée'}
                </p>
              )}
            </div>

            {/* Téléphone */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Téléphone
              </label>
              {editing ? (
                <input
                  type="tel"
                  value={formData.phone || ''}
                  onChange={(e) => handleChange('phone', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="+212 6XX XXX XXX"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.phone || 'Non renseigné'}
                </p>
              )}
            </div>
          </div>
        </div>

        {/* Informations professionnelles */}
        <div className="bg-white rounded-lg border border-gray-200 p-6">
          <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center">
            <svg className="w-6 h-6 mr-2 text-custom-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 13.255A23.931 23.931 0 0112 15a23.931 23.931 0 01-9-1.745M12 9a3 3 0 100-6 3 3 0 000 6zm-16 8.568A21.965 21.965 0 0112 21c7.732 0 14.666-2.519 20-6.732M6 12h12" />
            </svg>
            Informations Professionnelles
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Poste */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Poste
              </label>
              {editing ? (
                <input
                  type="text"
                  value={formData.position || ''}
                  onChange={(e) => handleChange('position', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="Ex: Inspecteur Douanier"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.position || 'Non renseigné'}
                </p>
              )}
            </div>

            {/* N° d'immatriculation */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                N° d'immatriculation
              </label>
              {editing ? (
                <input
                  type="text"
                  value={formData.badge_number || ''}
                  onChange={(e) => handleChange('badge_number', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="Ex: ADM-2024-001"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.badge_number || 'Non renseigné'}
                </p>
              )}
            </div>

            {/* Email professionnel */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Email professionnel
              </label>
              {editing ? (
                <input
                  type="email"
                  value={formData.professional_email || ''}
                  onChange={(e) => handleChange('professional_email', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="prenom.nom@portnet.ma"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.professional_email || 'Non renseigné'}
                </p>
              )}
            </div>

            {/* Département */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Service / Département
              </label>
              {editing ? (
                <input
                  type="text"
                  value={formData.department || ''}
                  onChange={(e) => handleChange('department', e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-custom-primary"
                  placeholder="Ex: Contrôle Douanier"
                />
              ) : (
                <p className="text-gray-900 font-medium">
                  {profile?.department || 'Non renseigné'}
                </p>
              )}
            </div>

            {/* Rôle */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Rôle
              </label>
              <p className="text-gray-900 font-medium">
                {profile?.role === 'ADMIN' ? 'Administrateur' : profile?.role === 'ANALYST' ? 'Analyste' : 'Visualiseur'}
              </p>
            </div>

            {/* Compte créé le */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Compte créé le
              </label>
              <p className="text-gray-900 font-medium">
                {profile?.created_at
                  ? new Date(profile.created_at).toLocaleDateString('fr-FR')
                  : 'N/A'}
              </p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Profile;
