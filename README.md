#  PortNet HARPON

**Système Intelligent d'Analyse de Risque Douanier**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61dafb.svg)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

##  Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Technologies](#-technologies)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [API Documentation](#-api-documentation)
- [Captures d'écran](#-captures-décran)
- [Contribuer](#-contribuer)
- [Licence](#-licence)

---

##  À propos

**PortNet HARPON** est une application web full-stack d'analyse intelligente de risque douanier. Elle utilise l'Intelligence Artificielle et le traitement du langage naturel (NLP) pour analyser automatiquement les documents douaniers et calculer un score de risque.

### Problématique

Les autorités douanières traitent quotidiennement des milliers de documents. L'analyse manuelle est :
-  **Chronophage** : Plusieurs heures par dossier
-  **Sujette aux erreurs** : Fatigue humaine
-  **Difficile à standardiser** : Critères variables

### Solution

PortNet HARPON automatise l'analyse avec :
-  **IA d'analyse de documents** : Extraction automatique de données
-  **Scoring de risque** : Calcul basé sur 4 critères objectifs
-  **Visualisation** : Graphiques et tableaux de bord
-  **Rapports PDF** : Génération automatique de rapports professionnels

---

##  Fonctionnalités

### Authentification & Sécurité
- Authentification JWT sécurisée
- Gestion des rôles (Admin, Analyste, Viewer)
- Sessions persistantes
- Hashage des mots de passe (bcrypt)

### Dashboard Interactif
- Statistiques temps réel
- Graphiques interactifs (Chart.js)
  - Répartition par statut
  - Distribution des risques
  - Évolution temporelle
- Indicateurs clés de performance (KPI)

### Gestion des Dossiers
- Création, lecture, mise à jour, suppression (CRUD)
- Statuts multiples : OPEN, IN_REVIEW, FLAGGED, CLEARED, CLOSED
- Niveaux de priorité : LOW, MEDIUM, HIGH, URGENT
- Assignation à des analystes
- Filtrage et recherche avancés

### Analyse Intelligente de Documents
- **Upload multi-formats** : PDF, images (PNG, JPG)
- **Extraction de texte** : Double méthode (PyPDF2 + pdfplumber)
- **Extraction de données structurées** :
  - Numéros de conteneurs
  - Montants et devises
  - Dates
  - Codes HS (tarification douanière)
  - Poids et mesures
  - Pays d'origine/destination
  - Emails et téléphones

### Intelligence Artificielle
- **Traitement du langage naturel** (spaCy)
- **Calcul du score de risque** (0-100) basé sur :
  1. Pays à risque (30 points)
  2. Montants suspects (25 points)
  3. Mots-clés suspects (35 points)
  4. Complétude des données (10 points)
- **Détection de facteurs de risque**
- **Recommandations automatiques**

### Système de Notes
- Notes collaboratives par dossier
- Auteur et horodatage
- Suppression par l'auteur
- Historique complet

### Visualisation & Reporting
- Graphiques interactifs (barres, circulaires, linéaires)
- Export PDF professionnel
  - En-tête avec logo
  - Score de risque encadré et coloré
  - Tableaux des documents
  - Facteurs de risque détaillés
  - Recommandations
  - Pagination automatique

### Notifications
- Toasts modernes (react-toastify)
- Feedback en temps réel
- Types : succès, erreur, info, warning

---

## Technologies

### Backend
| Technologie | Version | Utilisation |
|------------|---------|-------------|
| Python | 3.11+ | Langage principal |
| FastAPI | 0.110+ | Framework web moderne |
| PostgreSQL | 15+ | Base de données relationnelle |
| SQLAlchemy | 2.0+ | ORM Python |
| Alembic | 1.13+ | Migrations de base de données |
| PyJWT | 2.8+ | Authentification JWT |
| Passlib | 1.7+ | Hashage de mots de passe |
| spaCy | 3.7+ | NLP et analyse de texte |
| PyPDF2 | 3.0+ | Extraction PDF |
| pdfplumber | 0.11+ | Extraction PDF avancée |
| python-multipart | 0.0.6+ | Upload de fichiers |

### Frontend
| Technologie | Version | Utilisation |
|------------|---------|-------------|
| React | 18.2+ | Framework UI |
| Vite | 5.0+ | Build tool rapide |
| Tailwind CSS | 3.4+ | Framework CSS utility-first |
| Axios | 1.6+ | Client HTTP |
| React Router | 6.21+ | Routing |
| Chart.js | 4.4+ | Graphiques interactifs |
| react-chartjs-2 | 5.2+ | Wrapper React pour Chart.js |
| jsPDF | 2.5+ | Génération de PDF |
| jsPDF-AutoTable | 3.8+ | Tableaux PDF |
| react-toastify | 10.0+ | Notifications toast |
| Lucide React | 0.300+ | Icônes modernes |

---

##  Architecture

```
PortNet-HARPON/
├── backend/                 # API FastAPI
│   ├── app/
│   │   ├── api/            # Routes API
│   │   │   └── v1/
│   │   │       ├── endpoints/  # Endpoints REST
│   │   │       │   ├── auth.py
│   │   │       │   ├── cases.py
│   │   │       │   ├── documents.py
│   │   │       │   ├── notes.py
│   │   │       │   └── analysis.py
│   │   │       └── api.py      # Router principal
│   │   ├── core/           # Configuration
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/         # Modèles SQLAlchemy
│   │   │   ├── user.py
│   │   │   ├── case.py
│   │   │   ├── document.py
│   │   │   └── note.py
│   │   ├── schemas/        # Schémas Pydantic
│   │   ├── services/       # Services IA
│   │   │   ├── document_analyzer.py
│   │   │   ├── pdf_extractor.py
│   │   │   ├── data_extractor.py
│   │   │   └── risk_analyzer.py
│   │   └── main.py         # Point d'entrée
│   ├── uploads/            # Fichiers uploadés
│   ├── alembic/            # Migrations DB
│   └── requirements.txt    # Dépendances Python
│
├── frontend/               # Application React
│   ├── src/
│   │   ├── api/           # Client API
│   │   │   └── apiClient.js
│   │   ├── components/    # Composants réutilisables
│   │   │   ├── charts/
│   │   │   ├── Layout.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   ├── pages/         # Pages principales
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Cases.jsx
│   │   │   ├── CaseDetail.jsx
│   │   │   └── NewCase.jsx
│   │   ├── services/      # Services frontend
│   │   │   └── pdfGenerator.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   └── package.json       # Dépendances Node.js
│
└── README.md              # Ce fichier
```

### Flux de données

```
┌─────────────┐
│  Frontend   │
│   (React)   │
└──────┬──────┘
       │ HTTP/REST
       ▼
┌─────────────┐
│   FastAPI   │
│   Backend   │
└──────┬──────┘
       │
       ├─────► PostgreSQL (données structurées)
       │
       ├─────► Uploads/ (fichiers)
       │
       └─────► Services IA (analyse)
               │
               ├─► PDFExtractor
               ├─► DataExtractor
               ├─► RiskAnalyzer
               └─► DocumentAnalyzer
```

---

##  Installation

### Prérequis

- **Python** 3.11 ou supérieur
- **Node.js** 18 ou supérieur
- **PostgreSQL** 15 ou supérieur
- **Git**

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/PortNet-HARPON.git
cd PortNet-HARPON
```

### 2. Configuration de la base de données

```sql
-- Créer la base de données PostgreSQL
CREATE DATABASE portnet_harpon;
CREATE USER portnet_user WITH PASSWORD 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE portnet_harpon TO portnet_user;
```

### 3. Installation du Backend

```bash
cd backend

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Télécharger le modèle spaCy français
python -m spacy download fr_core_news_sm

# Créer le fichier .env
cp .env.example .env
# Éditer .env avec vos informations
```

Fichier `.env` à créer :

```env
# Base de données
DATABASE_URL=postgresql://portnet_user:votre_mot_de_passe@localhost/portnet_harpon

# Sécurité
SECRET_KEY=votre-cle-secrete-ultra-longue-et-aleatoire-changez-moi
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=True
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

```bash
# Initialiser la base de données
alembic upgrade head

# Lancer le serveur
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

 Le backend est accessible sur : **http://127.0.0.1:8001**  
 Documentation API : **http://127.0.0.1:8001/docs**

### 4. Installation du Frontend

Ouvrez un nouveau terminal :

```bash
cd frontend

# Installer les dépendances
npm install

# Lancer le serveur de développement
npm run dev
```

 Le frontend est accessible sur : **http://localhost:5173**

---

##  Utilisation

### Première connexion

Identifiants par défaut :
- **Username** : `admin`
- **Password** : `admin123`

 **Important** : Changez le mot de passe admin après la première connexion !

### Workflow typique

1. Se connecter avec vos identifiants
2. Créer un nouveau dossier depuis le Dashboard
3. Uploader un document PDF (facture, connaissement, etc.)
4. Attendre l'analyse IA (quelques secondes)
5. Consulter le score de risque et les facteurs détectés
6. Ajouter des notes pour collaboration
7. Exporter le rapport en PDF si nécessaire
8. Changer le statut selon l'avancement

### Exemples de documents à tester

Pour tester l'IA, créez un PDF avec ce contenu :

```
FACTURE COMMERCIALE

Exportateur : ABC Trading Co.
Pays d'origine : CHINE
Destination : Maroc

Montant total : 150,000 USD

Conteneur : ABCD1234567
Code HS : 8471.30.00

Description : Ordinateurs portables
Poids net : 2500 KG
```

**Résultat attendu** :
- Score de risque : ~55/100 (MOYEN)
- Facteurs :
  -  Pays à risque détecté : CHINE
  -  Montant élevé : 150000 USD

---

##  API Documentation

### Authentification

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}

Response:
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "user": { ... }
}
```

### Dossiers

```http
# Lister tous les dossiers
GET /api/v1/cases/
Authorization: Bearer {token}

# Créer un dossier
POST /api/v1/cases/
Authorization: Bearer {token}
Content-Type: application/json

{
  "case_number": "CASE-2026-001",
  "importer": "Société XYZ",
  "origin_country": "Chine"
}

# Détails d'un dossier
GET /api/v1/cases/{case_id}
Authorization: Bearer {token}
```

### Documents

```http
# Uploader un document
POST /api/v1/cases/{case_id}/documents
Authorization: Bearer {token}
Content-Type: multipart/form-data

file: [fichier PDF]

Response:
{
  "id": 1,
  "filename": "facture.pdf",
  "status": "ANALYZED",
  "risk_score": 55,
  "risk_level": "MOYEN",
  "risk_factors": ["Pays à risque : CHINE", "Montant élevé : 150000 USD"]
}
```

 **Documentation complète** : http://127.0.0.1:8001/docs

---

##  Captures d'écran

### Dashboard
![Dashboard](docs/screenshots/dashboard.png)  
*Vue d'ensemble avec statistiques et graphiques*

### Liste des dossiers
![Cases List](docs/screenshots/cases-list.png)  
*Gestion et filtrage des dossiers*

### Détail d'un dossier
![Case Detail](docs/screenshots/case-detail.png)  
*Analyse complète avec score de risque*

### Analyse IA
![AI Analysis](docs/screenshots/ai-analysis.png)  
*Résultats de l'analyse automatique*

---

##  Contribuer

Les contributions sont les bienvenues ! Voici comment participer :

1. Fork le projet
2. Créer une branche : `git checkout -b feature/nouvelle-fonctionnalite`
3. Commit vos changements : `git commit -m 'Ajout nouvelle fonctionnalité'`
4. Push : `git push origin feature/nouvelle-fonctionnalite`
5. Ouvrir une Pull Request

### Guidelines

- **Code Python** : suivre PEP 8
- **Code JavaScript** : ESLint + Prettier
- **Tests** : ajouter des tests pour les nouvelles fonctionnalités
- **Documentation** : mettre à jour le README si nécessaire

---

##  Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

##  Auteurs

- **Votre Nom** - *Développeur principal* - [GitHub](https://github.com/votre-username)

---

##  Remerciements

- [FastAPI](https://fastapi.tiangolo.com/) - Framework backend moderne
- [React](https://react.dev/) - Bibliothèque UI
- [spaCy](https://spacy.io/) - NLP open-source
- [Tailwind CSS](https://tailwindcss.com/) - Framework CSS

---

##  Support

Pour toute question ou problème :
- **Issues** : [GitHub Issues](https://github.com/votre-username/PortNet-HARPON/issues)
- **Email** : votre.email@exemple.com

---

*Fait avec ❤️ pour faciliter le travail des autorités douanières*
