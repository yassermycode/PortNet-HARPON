from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
<<<<<<< HEAD
import json
import numpy as np
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
from datetime import datetime

from app.db.session import get_db
from app.db.models.case import Case
from app.db.models.document import Document
from app.api.deps import get_current_user
from app.db.models.user import User
from app.services.document_analyzer import DocumentAnalyzer

router = APIRouter()

<<<<<<< HEAD

def convert_to_json_serializable(obj):
    """Convertit récursivement les types numpy et Python en types JSON-sérialisables"""
    if isinstance(obj, dict):
        return {k: convert_to_json_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json_serializable(item) for item in obj]
    elif isinstance(obj, (np.bool_, np.integer)):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, bool):
        return bool(obj)
    else:
        return obj


# Dossier pour stocker les fichiers
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

=======
# Dossier pour stocker les fichiers
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
@router.post("/cases/{case_id}/documents")
async def upload_document(
    case_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Upload un document et lance l'analyse IA automatiquement"""
    
    print(f"\n{'='*60}")
    print(f"📤 UPLOAD DE DOCUMENT POUR LE DOSSIER {case_id}")
    print(f"{'='*60}\n")
    print(f"🔵 Fichier: {file.filename}")
    print(f"🔵 Type: {file.content_type}")
    
    # Vérifier que le dossier existe
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    # Créer le dossier pour ce case
    case_upload_dir = os.path.join(UPLOAD_DIR, str(case_id))
    os.makedirs(case_upload_dir, exist_ok=True)
    
    # Générer un nom de fichier unique
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(case_upload_dir, filename)
    
    # Sauvegarder le fichier
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"✅ Fichier sauvegardé: {file_path}")
    except Exception as e:
        print(f"❌ Erreur upload: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'upload: {str(e)}")
    
    # Créer l'entrée dans la base de données
    document = Document(
        case_id=case_id,
        filename=file.filename,
        file_path=file_path,
        file_type=file.content_type,
        file_size=os.path.getsize(file_path),
        uploaded_by=current_user.id,
<<<<<<< HEAD
        status="UPLOADED"  # Statut initial - en attente d'analyse manuelle
=======
        status="ANALYZING"
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    )
    
    db.add(document)
    db.commit()
    db.refresh(document)
    
    print(f"✅ Document créé en DB: ID={document.id}")
    
<<<<<<< HEAD
    # NE PAS ANALYSER AUTOMATIQUEMENT
    # L'utilisateur déclenchera l'analyse manuellement via le bouton "Analyser"
    print(f"\n✅ DOCUMENT UPLOADÉ AVEC SUCCÈS")
    print(f"   Statut: UPLOADED (en attente d'analyse manuelle)")
    print(f"   L'utilisateur peut maintenant lancer l'analyse via le bouton 'Analyser'\n")
=======
    # ANALYSER LE DOCUMENT SI C'EST UN PDF
    if file.content_type == "application/pdf" or file.filename.lower().endswith('.pdf'):
        try:
            print(f"\n🤖 LANCEMENT DE L'ANALYSE IA...")
            
            # Analyser le document
            analysis_result = DocumentAnalyzer.analyze_document(file_path)
            
            if analysis_result["analysis_status"] == "SUCCESS":
                # Mettre à jour le document avec les résultats
                document.status = "ANALYZED"
                document.extracted_text = analysis_result["extracted_text"]
                document.extracted_data = analysis_result["extracted_data"]
                document.risk_score = analysis_result["risk_analysis"]["risk_score"]
                document.risk_level = analysis_result["risk_analysis"]["risk_level"]
                document.risk_factors = analysis_result["risk_analysis"]["risk_factors"]
                document.recommendation = analysis_result["risk_analysis"]["recommendation"]
                document.analyzed_at = datetime.now()
                
                # Mettre à jour le score du dossier (prendre le max des documents)
                case.risk_score = max(case.risk_score or 0, document.risk_score)
                case.risk_level = document.risk_level
                
                db.commit()
                db.refresh(document)
                db.refresh(case)
                
                print(f"\n✅ ANALYSE TERMINÉE ET SAUVEGARDÉE")
                print(f"   Score du document: {document.risk_score}/100")
                print(f"   Score du dossier mis à jour: {case.risk_score}/100")
                
            else:
                document.status = "ERROR"
                db.commit()
                print(f"\n❌ ERREUR D'ANALYSE: {analysis_result.get('error')}")
                
        except Exception as e:
            print(f"\n❌ ERREUR LORS DE L'ANALYSE: {str(e)}")
            document.status = "ERROR"
            db.commit()
    else:
        print(f"\n⚠️  Type de fichier non PDF - analyse ignorée")
        document.status = "UPLOADED"
        db.commit()
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    
    return {
        "id": document.id,
        "filename": document.filename,
        "file_type": document.file_type,
        "file_size": document.file_size,
        "uploaded_at": document.created_at,
        "status": document.status,
        "risk_score": document.risk_score,
        "risk_level": document.risk_level,
        "risk_factors": document.risk_factors,
        "recommendation": document.recommendation,
<<<<<<< HEAD
        "message": "Document uploadé avec succès. Cliquez sur 'Analyser' pour lancer l'analyse IA."
=======
        "message": "Document uploadé et analysé avec succès" if document.status == "ANALYZED" else "Document uploadé"
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    }


@router.get("/cases/{case_id}/documents")
async def get_case_documents(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer tous les documents d'un dossier avec leurs analyses"""
    
    print(f"🔵 Récupération des documents du dossier {case_id}")
    
    documents = db.query(Document).filter(Document.case_id == case_id).all()
    
    print(f"✅ {len(documents)} document(s) trouvé(s)")
    
    return {
        "case_id": case_id,
        "total": len(documents),
        "documents": [
            {
                "id": doc.id,
                "filename": doc.filename,
                "file_type": doc.file_type,
                "file_size": doc.file_size,
                "uploaded_at": doc.created_at,
                "status": doc.status,
                "risk_score": doc.risk_score,
                "risk_level": doc.risk_level,
                "risk_factors": doc.risk_factors,
                "recommendation": doc.recommendation,
<<<<<<< HEAD
                "extracted_data": doc.extracted_data,  # Inclut benford_analysis
                "document_type": doc.document_type,
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            }
            for doc in documents
        ]
    }


@router.get("/documents/{document_id}")
async def get_document_details(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les détails complets d'un document"""
    
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document non trouvé")
    
    return {
        "id": document.id,
        "filename": document.filename,
        "file_type": document.file_type,
        "file_size": document.file_size,
        "status": document.status,
        "extracted_text": document.extracted_text,
        "extracted_data": document.extracted_data,
        "risk_score": document.risk_score,
        "risk_level": document.risk_level,
        "risk_factors": document.risk_factors,
        "recommendation": document.recommendation,
        "uploaded_at": document.created_at,
        "analyzed_at": document.analyzed_at,
    }


@router.delete("/documents/{document_id}")
async def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Supprimer un document"""
    
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document non trouvé")
    
    # Supprimer le fichier physique
    try:
        if os.path.exists(document.file_path):
            os.remove(document.file_path)
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier: {e}")
    
    # Supprimer de la base de données
    db.delete(document)
    db.commit()
    
    return {"message": "Document supprimé avec succès"}


@router.post("/documents/{document_id}/analyze")
async def analyze_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
<<<<<<< HEAD
    """Analyser un document manuellement"""
    print(f"\n{'='*60}")
    print(f"🔄 ANALYSE DU DOCUMENT {document_id}")
=======
    """Réanalyser un document manuellement"""
    print(f"\n{'='*60}")
    print(f"🔄 RÉANALYSE DU DOCUMENT {document_id}")
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    print(f"{'='*60}\n")

    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document non trouvé")

    # Vérifier que c'est un PDF
    if not (document.file_type == "application/pdf" or document.filename.lower().endswith('.pdf')):
        raise HTTPException(status_code=400, detail="Seuls les fichiers PDF peuvent être analysés")

    document.status = "ANALYZING"
    db.commit()

    try:
        print(f"🤖 LANCEMENT DE L'ANALYSE IA...")
        analysis_result = DocumentAnalyzer.analyze_document(document.file_path)

<<<<<<< HEAD
        # Sauvegarder le type de document détecté
        if analysis_result.get("document_classification"):
            classification = analysis_result["document_classification"]
            document.document_type = classification.get("document_type")
            document.classification_confidence = int(classification.get("confidence", 0))

        # Si l'analyse est REJETÉE (document non-douanier)
        if analysis_result.get("analysis_status") == "REJECTED":
            document.status = "REJECTED"
            document.analyzed_at = datetime.now()
            db.commit()
            
            error_msg = analysis_result.get("error", "Document non-douanier")
            print(f"\n❌ DOCUMENT REJETÉ: {error_msg}")
            
            raise HTTPException(
                status_code=400,
                detail=error_msg
            )

        if analysis_result.get("analysis_status") == "SUCCESS":
            document.status = "ANALYZED"
            document.extracted_text = analysis_result.get("extracted_text")
            
            # Inclure benford_analysis dans extracted_data
            extracted_data = analysis_result.get("extracted_data", {})
            benford_analysis = analysis_result.get("risk_analysis", {}).get("benford_analysis")
            if benford_analysis:
                extracted_data["benford_analysis"] = benford_analysis
            
            # Convertir tous les types non-JSON-sérialisables (numpy, bool, etc.)
            extracted_data = convert_to_json_serializable(extracted_data)
            
            document.extracted_data = extracted_data
            
=======
        if analysis_result.get("analysis_status") == "SUCCESS":
            document.status = "ANALYZED"
            document.extracted_text = analysis_result.get("extracted_text")
            document.extracted_data = analysis_result.get("extracted_data")
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            document.risk_score = analysis_result.get("risk_analysis", {}).get("risk_score")
            document.risk_level = analysis_result.get("risk_analysis", {}).get("risk_level")
            document.risk_factors = analysis_result.get("risk_analysis", {}).get("risk_factors")
            document.recommendation = analysis_result.get("risk_analysis", {}).get("recommendation")
            document.analyzed_at = datetime.now()

            # Mettre à jour le score du dossier
            case = db.query(Case).filter(Case.id == document.case_id).first()
            if case:
                case.risk_score = max(case.risk_score or 0, document.risk_score or 0)
                case.risk_level = document.risk_level

            db.commit()
            db.refresh(document)

<<<<<<< HEAD
            print(f"\n✅ ANALYSE TERMINÉE")
            print(f"   Type: {document.document_type}")
            print(f"   Score: {document.risk_score}/100")

            return {
                "message": "Document analysé avec succès",
                "document_type": document.document_type,
                "classification_confidence": document.classification_confidence,
=======
            print(f"\n✅ RÉANALYSE TERMINÉE")
            print(f"   Score: {document.risk_score}/100")

            return {
                "message": "Document réanalysé avec succès",
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
                "risk_score": document.risk_score,
                "risk_level": document.risk_level,
                "risk_factors": document.risk_factors,
                "recommendation": document.recommendation,
<<<<<<< HEAD
                "benford_analysis": benford_analysis,
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
            }
        else:
            document.status = "ERROR"
            db.commit()
            raise HTTPException(status_code=500, detail=analysis_result.get('error', "Erreur lors de l'analyse"))

<<<<<<< HEAD
    except HTTPException:
        raise
=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    except Exception as e:
        print(f"\n❌ ERREUR: {str(e)}")
        document.status = "ERROR"
        db.commit()
        raise HTTPException(status_code=500, detail=str(e))
