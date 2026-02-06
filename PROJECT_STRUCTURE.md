# PortNet-HARPON Project Structure

## Overview
PortNet-HARPON is a full-stack web application for document analysis and port security risk assessment. The project combines a FastAPI backend with a React frontend for intelligent document processing and case management.

---

## Root Directory Structure

```
PortNet-HARPON/
├── .git/                          # Git repository metadata
├── .gitignore                      # Git ignore rules
├── .venv/                          # Python virtual environment (ignored)
├── venv/                           # Alternative Python virtual environment
├── backend/                        # FastAPI backend application
├── frontend/                       # React frontend application
├── docker-compose.yml              # Docker composition file
├── README.md                        # Project documentation
├── storage/                        # Document storage directory
└── PROJECT_STRUCTURE.md            # This file
```

---

## Backend Structure

### Path: `backend/`

```
backend/
├── app/                            # Main application package
│   ├── __init__.py
│   ├── main.py                     # FastAPI entry point
│   ├── api/                        # API routes and versioning
│   │   ├── __init__.py
│   │   ├── deps.py                 # Authentication dependencies & JWT validation
│   │   └── v1/                     # API v1 endpoints
│   │       ├── __init__.py
│   │       ├── api.py              # API router configuration
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── users.py        # User management endpoints
│   │           ├── auth.py         # Authentication endpoints (login, token)
│   │           ├── cases.py        # Case management endpoints (CRUD)
│   │           ├── documents.py    # Document upload & analysis endpoints
│   │           └── notes.py        # Note creation & management endpoints (NEW)
│   ├── core/                       # Core configuration & settings
│   │   ├── __init__.py
│   │   └── config.py               # Environment config, API_V1_STR, secrets
│   ├── db/                         # Database layer
│   │   ├── __init__.py
│   │   ├── base.py                 # SQLAlchemy base & model registration
│   │   ├── session.py              # Database session factory
│   │   ├── crud/                   # CRUD operations per model
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # User CRUD operations
│   │   │   ├── case.py             # Case CRUD operations
│   │   │   ├── document.py         # Document CRUD operations
│   │   │   └── note.py             # Note CRUD operations (NEW)
│   │   └── models/                 # SQLAlchemy ORM models
│   │       ├── __init__.py
│   │       ├── user.py             # User model (with hashed passwords, roles)
│   │       ├── case.py             # Case model (with risk fields)
│   │       ├── document.py         # Document model (with analysis results)
│   │       ├── note.py             # Note model (NEW - case/doc annotations)
│   │       ├── entity.py           # Entity model
│   │       ├── case_entity_link.py # CaseEntity relationship
│   │       ├── feature.py          # Feature model
│   │       ├── signal.py           # Signal model
│   │       ├── document_similarity.py # Document similarity tracking
│   │       └── audit_log.py        # Audit logging
│   ├── schemas/                    # Pydantic validation schemas
│   │   ├── __init__.py
│   │   ├── user.py                 # User schema (input/output)
│   │   ├── case.py                 # Case schema (input/output)
│   │   ├── document.py             # Document schema (input/output with analysis)
│   │   └── note.py                 # Note schema (NEW)
│   └── services/                   # Business logic services
│       ├── __init__.py
│       ├── pdf_extractor.py        # PDF text extraction (PyPDF2, pdfplumber)
│       ├── data_extractor.py       # Structured data extraction (NLP, spaCy)
│       ├── risk_analyzer.py        # Risk scoring & analysis
│       └── document_analyzer.py    # Orchestrator (chains extraction → analysis)
├── alembic/                        # Database migrations (Alembic setup)
│   ├── env.py
│   ├── script.py.mako
│   └── versions/                   # Migration files
├── scripts/                        # Utility scripts
│   └── init_db.py                  # Database initialization
├── tests/                          # Test suite
│   ├── test_auth.py
│   ├── test_documents.py
│   └── test_cases.py
├── alembic.ini                     # Alembic configuration
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker image definition
├── docker-compose.yml              # Docker compose services
├── .env                            # Environment variables (local)
├── .env.example                    # Environment template
├── README.md                        # Backend documentation
├── create_test_pdf.py              # Test PDF generator script
├── reset_db.py                     # Database reset utility
├── test_seed_check.py              # Seed data validation
├── test_tables.py                  # Table structure verification
├── data/                           # Data directory (database, exports)
├── logs/                           # Application logs
├── uploaded_files/                 # Uploaded document storage
├── uploads/                        # Alternative upload directory
├── test_documents/                 # Test PDF files
├── htmlcov/                        # Coverage reports
└── .pytest_cache/                  # Pytest cache
```

### Backend Key Dependencies
- **FastAPI**: Web framework
- **SQLAlchemy**: ORM for database
- **Pydantic**: Data validation
- **PyJWT + python-jose**: JWT authentication
- **PyPDF2, pdfplumber**: PDF text extraction
- **spaCy**: French NLP model (fr_core_news_sm)
- **pytesseract, Pillow, OpenCV**: OCR and image processing
- **python-Levenshtein**: String similarity
- **PostgreSQL**: Database (via SQLAlchemy)

### Database Models
1. **User** - Authentication & authorization
2. **Case** - Case container with risk scoring
3. **Document** - Uploaded files with analysis results
4. **Note** - User annotations on cases/documents (NEW)
5. **Entity** - Extracted entities from documents
6. **CaseEntityLink** - Relationship between cases and entities
7. **Feature** - ML features extracted
8. **Signal** - Risk signals detected
9. **DocumentSimilarity** - Document comparison tracking
10. **AuditLog** - Audit trail

---

## Frontend Structure

### Path: `frontend/`

```
frontend/
├── node_modules/                   # NPM dependencies (large, contains Vite, React, etc.)
├── src/                            # Source code
│   ├── api/
│   │   ├── apiClient.js            # Axios HTTP client (NEW - single source of truth)
│   │   │                            # Hardcoded to http://127.0.0.1:8001
│   │   │                            # Exports: authAPI, casesAPI, documentsAPI, notesAPI
│   │   └── client.old.js            # Deprecated client (backup)
│   ├── components/
│   │   ├── cases/
│   │   │   ├── CaseCard.jsx         # Individual case display
│   │   │   ├── CaseList.jsx         # List of cases
│   │   │   └── CreateCaseForm.jsx   # Case creation form
│   │   ├── dashboard/
│   │   │   └── StatsCard.jsx        # Statistics display card
│   │   └── layout/
│   │       ├── Layout.jsx           # Main layout wrapper
│   │       └── Navbar.jsx           # Navigation bar (Algorithms link removed)
│   ├── contexts/
│   │   └── AuthContext.jsx          # Auth state management (token key: 'token')
│   ├── hooks/
│   │   └── useAuth.js               # Custom hook for auth context
│   ├── pages/
│   │   ├── Analytics.jsx            # Analytics page (not in navigation)
│   │   ├── CaseDetail.jsx           # Case detail with documents & analysis
│   │   │                            # NEW: Large Algorithms section (300+ lines)
│   │   │                            # Shows: algorithm stats, detailed algo cards
│   │   ├── Cases.jsx                # Cases list page
│   │   ├── Dashboard.jsx            # Dashboard/home page
│   │   ├── Login.jsx                # Login page
│   │   └── NotFound.jsx             # 404 page
│   ├── utils/
│   │   └── constants.js             # App constants
│   ├── App.jsx                      # Main app component with routes
│   ├── main.jsx                     # Entry point
│   └── index.css                    # Global styles (Tailwind)
├── public/                          # Static assets (if any)
├── index.html                       # HTML entry point
├── vite.config.js                   # Vite configuration
├── tailwind.config.js               # Tailwind CSS configuration
├── package.json                     # NPM dependencies & scripts
├── package-lock.json                # Dependency lock file
└── .env                             # Frontend environment (if needed)
```

### Frontend Key Dependencies
- **React**: UI library
- **React Router**: Client-side routing
- **Axios**: HTTP client
- **Tailwind CSS**: Utility-first CSS framework
- **lucide-react**: Icon library
- **Vite**: Build tool & dev server

### Frontend Components Hierarchy
```
App.jsx
├── Login (public route)
├── Layout (private routes wrapper)
│   ├── Navbar
│   └── [Page Component]
│       ├── Dashboard
│       ├── Cases
│       │   └── CaseCard (multiple)
│       ├── CaseDetail
│       │   ├── DocumentList
│       │   └── Algorithms Section (NEW)
│       └── Analytics
```

### Frontend Authentication Flow
1. User logs in on Login page
2. Credentials sent to `POST /api/v1/auth/login`
3. JWT token received, stored in localStorage as `'token'` key
4. AuthContext manages token state
5. API calls include `Authorization: Bearer {token}` header
6. Protected routes check for valid token in AuthContext

---

## Key Features & Implementation

### 1. Document Analysis Pipeline
- **Upload**: `POST /api/v1/documents/upload`
- **Flow**: PDF → Text Extraction → Data Extraction → Risk Analysis
- **Services**:
  - `pdf_extractor.py`: Extracts raw text from PDFs
  - `data_extractor.py`: Performs NLP extraction (entities, relationships)
  - `risk_analyzer.py`: Calculates risk scores and flags
  - `document_analyzer.py`: Orchestrates the pipeline
- **Storage**: Results stored in Document model fields:
  - `extracted_text`: Raw PDF text
  - `extracted_data`: Structured JSON data
  - `risk_score`: Numerical score (0-100)
  - `risk_level`: Level (low, medium, high, critical)
  - `risk_factors`: List of identified risk factors
  - `recommendation`: Action recommendation
  - `analyzed_at`: Timestamp

### 2. Manual Re-Analysis
- **Endpoint**: `POST /api/v1/documents/{document_id}/analyze`
- **Purpose**: Trigger analysis on already-uploaded documents
- **Response**: Updated analysis results

### 3. Note System
- **Model**: `Note` with case_id, document_id, content, created_by
- **Endpoints**:
  - `POST /api/v1/notes/` - Create note
  - `GET /api/v1/notes/` - List notes (filter by case/doc)
  - `DELETE /api/v1/notes/{note_id}` - Delete note
- **Frontend**: Notes can be added/viewed in case detail

### 4. Authentication
- **Type**: JWT (JSON Web Token) with OAuth2PasswordBearer
- **Endpoints**:
  - `POST /api/v1/auth/login` - Login (username/password)
  - `POST /api/v1/auth/token/refresh` - Refresh token
- **Storage**: Token in localStorage with key `'token'`
- **Default User**: admin / admin123

### 5. Case Management
- **Endpoints**:
  - `GET /api/v1/cases/` - List all cases
  - `POST /api/v1/cases/` - Create case
  - `GET /api/v1/cases/{case_id}` - Get case detail
  - `PUT /api/v1/cases/{case_id}` - Update case
  - `DELETE /api/v1/cases/{case_id}` - Delete case
- **Fields**: title, description, status, priority, risk_score, risk_level

### 6. Algorithms Display Section
- **Location**: CaseDetail page, shown after Documents section
- **Displays**:
  - Global statistics: active algorithms, anomalies, precision, confidence
  - Detailed algorithm cards:
    1. **NLP Extraction** - Entity recognition, relationship extraction
    2. **Risk Scoring** - Pattern matching, threshold analysis
    3. **Anomaly Detection** - Deviation detection, outlier identification
    4. **OCR/Text Extraction** - Image text recognition, character accuracy
- **Logic**: Only shown when documents have been analyzed
- **Data**: Populated from document analysis results

---

## Configuration & Credentials

### Backend Environment (`.env`)
```
DATABASE_URL=postgresql://user:password@localhost/portnet
SECRET_KEY=<your-secret-key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
API_V1_STR=/api/v1
```

### Frontend API Configuration
- **Base URL**: `http://127.0.0.1:8001`
- **API Version**: `/api/v1`
- **Authentication Header**: `Authorization: Bearer {token}`

### Default Credentials
- **Username**: admin
- **Password**: admin123

---

## Database Schema

### User Table
```sql
id (PK)
username (UNIQUE)
email
hashed_password
full_name
is_active
role
created_at
updated_at
```

### Case Table
```sql
id (PK)
title
description
status
priority
risk_score
risk_level
created_at
updated_at
owner_id (FK → User)
```

### Document Table
```sql
id (PK)
case_id (FK → Case)
filename
file_path
file_size
extracted_text
extracted_data (JSON)
risk_score
risk_level
risk_factors (JSON)
recommendation
analyzed_at
uploaded_at
uploaded_by (FK → User)
```

### Note Table
```sql
id (PK)
case_id (FK → Case)
document_id (FK → Document, nullable)
content
created_by (FK → User)
created_at
updated_at
```

---

## API Endpoints Summary

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/token/refresh` - Refresh JWT token

### Users
- `GET /api/v1/users/me` - Get current user
- `POST /api/v1/users/` - Create user (admin only)
- `GET /api/v1/users/{user_id}` - Get user details

### Cases
- `GET /api/v1/cases/` - List all cases (paginated)
- `POST /api/v1/cases/` - Create new case
- `GET /api/v1/cases/{case_id}` - Get case details with documents
- `PUT /api/v1/cases/{case_id}` - Update case
- `DELETE /api/v1/cases/{case_id}` - Delete case

### Documents
- `GET /api/v1/documents/{document_id}` - Get document details
- `POST /api/v1/documents/upload` - Upload document (triggers auto-analysis)
- `POST /api/v1/documents/{document_id}/analyze` - Manual re-analysis
- `DELETE /api/v1/documents/{document_id}` - Delete document

### Notes
- `GET /api/v1/notes/` - List notes (filter by case_id or document_id)
- `POST /api/v1/notes/` - Create note
- `DELETE /api/v1/notes/{note_id}` - Delete note

---

## Running the Application

### Backend (FastAPI + uvicorn)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8001
```

### Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev  # Dev server on http://localhost:5173
npm run build  # Production build
```

### Database (PostgreSQL)
```bash
# Using Docker
docker-compose up -d

# Or local PostgreSQL instance
# Ensure DATABASE_URL points to correct connection string
# Run migrations: alembic upgrade head
```

---

## Testing

### Backend Tests
```bash
cd backend
pytest tests/
pytest tests/test_auth.py -v
pytest tests/test_documents.py -v
pytest tests/test_cases.py -v
```

### Test Scripts
```bash
python create_test_pdf.py  # Generate test PDF
python reset_db.py  # Reset database
python test_seed_check.py  # Verify seed data
python test_tables.py  # Verify table structure
```

---

## File Size & Performance Notes

### Large Directories
- **`frontend/node_modules/`** - ~500MB+ (contains Vite, React, dependencies)
- **`venv/`** - ~500MB+ (Python virtual environment)

### Git Ignored Items (`.gitignore`)
- node_modules/
- venv/
- .env (local)
- uploaded_files/
- htmlcov/
- .pytest_cache/
- __pycache__/

---

## Recent Changes (Session Summary)

### Phase 1: Backend Services & Integration
- Created document analysis services (PDF extraction, data extraction, risk analysis)
- Integrated automatic analysis into upload endpoint
- Updated Document model with analysis result fields

### Phase 2: Frontend API Refactoring
- Fixed API client configuration (hardcoded to 8001)
- Resolved token management inconsistency (standardized on `'token'` key)
- Updated all frontend files to use new unified `apiClient.js`

### Phase 3: Features Added
- Manual re-analyze endpoint: `POST /documents/{id}/analyze`
- Complete Note system with CRUD operations
- Large Algorithms display section in CaseDetail page
- Removed Analytics link from navigation

### Phase 4: Current Status
- ✅ Backend running on port 8001 (all endpoints operational)
- ✅ Frontend dev server on port 5173
- ✅ Document analysis pipeline functional
- ✅ Authentication system working
- ✅ Note system implemented
- ✅ Algorithms transparency display added

---

## Next Steps & Improvements

1. **Optional**: Install spaCy French model for enhanced NLP
   ```bash
   python -m spacy download fr_core_news_sm
   ```

2. **Optional**: Implement background processing with Celery/RQ for large uploads

3. **Optional**: Add Alembic migrations for proper database versioning

4. **Production**: Configure proper environment variables, SSL/TLS, rate limiting

5. **Testing**: Add comprehensive test coverage for new features

---

## Support & Debugging

### Common Issues
- **API 404 errors**: Ensure backend is running on 8001
- **Authentication failures**: Check token in localStorage (`'token'` key)
- **CORS errors**: Backend should have CORS middleware configured
- **Database connection**: Verify DATABASE_URL in .env matches your PostgreSQL setup

### Logging
- Backend logs: Check `backend/logs/` directory
- Frontend logs: Check browser console (F12)
- API request logs: Check with verbose axios logging in `apiClient.js`

---

**Last Updated**: Current session  
**Project Version**: Full-stack with document analysis  
**Status**: Production-ready for basic usage
