from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.session import get_db
from app.db.models.case import Case
from app.db.models.user import User
<<<<<<< HEAD
from app.db.models.document import Document
from app.db.models.note import Note
from app.api.dependencies.auth import get_current_user
from pydantic import BaseModel
from datetime import datetime
import os
=======
from app.api.dependencies.auth import get_current_user
from pydantic import BaseModel
from datetime import datetime
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4

router = APIRouter()

# Schema de création
class CaseCreate(BaseModel):
    case_number: str
    importer_name: str
    declarant_name: Optional[str] = None
    transporter_name: Optional[str] = None
    priority: str = "MEDIUM"
    description: Optional[str] = None

# Schema de mise à jour de statut
class CaseStatusUpdate(BaseModel):
    status: str

# Schema de mise à jour de priorité
class CasePriorityUpdate(BaseModel):
    priority: str

<<<<<<< HEAD
# Schema de mise à jour complète
class CaseUpdate(BaseModel):
    case_number: Optional[str] = None
    importer_name: Optional[str] = None
    declarant_name: Optional[str] = None
    transporter_name: Optional[str] = None
    priority: Optional[str] = None
    description: Optional[str] = None

=======
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
# Schema de réponse
class CaseResponse(BaseModel):
    id: int
    case_number: str
    importer_name: str
    declarant_name: Optional[str]
    transporter_name: Optional[str]
    priority: str
    status: str
    description: Optional[str]
    risk_score: Optional[int]
    created_at: datetime
    created_by: int
    
    class Config:
        from_attributes = True

@router.post("/", response_model=CaseResponse)
async def create_case(
    case_data: CaseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Créer un nouveau dossier"""
    
    print(f"🔵 Données reçues: {case_data}")
    print(f"🔵 Utilisateur: {current_user.username}")
    
    # Vérifier que le case_number n'existe pas déjà
    existing = db.query(Case).filter(Case.case_number == case_data.case_number).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Le dossier {case_data.case_number} existe déjà")
    
    # Créer le dossier
    new_case = Case(
        case_number=case_data.case_number,
        importer_name=case_data.importer_name,
        declarant_name=case_data.declarant_name,
        transporter_name=case_data.transporter_name,
        priority=case_data.priority,
        description=case_data.description,
        status="OPEN",
        created_by=current_user.id,
        risk_score=0
    )
    
    try:
        db.add(new_case)
        db.commit()
        db.refresh(new_case)
        
        print(f"✅ Dossier créé: ID={new_case.id}, Number={new_case.case_number}")
        
        return new_case
        
    except Exception as e:
        db.rollback()
        print(f"❌ Erreur lors de la création: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de la création: {str(e)}")


@router.get("/")
async def get_cases(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer tous les dossiers"""
    
    query = db.query(Case)
    
    if status:
        query = query.filter(Case.status == status)
    
    if priority:
        query = query.filter(Case.priority == priority)
    
    cases = query.offset(skip).limit(limit).all()
    
    return {
        "total": len(cases),
        "cases": cases
    }


@router.get("/stats")
async def get_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les statistiques des dossiers"""
    
    total_cases = db.query(Case).count()
    open_cases = db.query(Case).filter(Case.status == "OPEN").count()
    in_progress_cases = db.query(Case).filter(Case.status == "IN_PROGRESS").count()
    closed_cases = db.query(Case).filter(Case.status == "CLOSED").count()
    archived_cases = db.query(Case).filter(Case.status == "ARCHIVED").count()
    
    return {
        "total_cases": total_cases,
        "open_cases": open_cases,
        "in_progress_cases": in_progress_cases,
        "closed_cases": closed_cases,
        "archived_cases": archived_cases
    }


<<<<<<< HEAD
@router.get("/risk-distribution")
async def get_risk_distribution(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Récupérer la distribution des dossiers par niveau de risque
    
    Catégories :
    - FIABLE (Vert) : Score < 20
    - SIGNALÉ (Orange) : Score 20-74
    - ANOMALIE (Rouge) : Score >= 75
    
    Returns:
        Nombre de dossiers dans chaque catégorie
    """
    print("\n📊 Calcul de la distribution des risques...")
    
    # Récupérer tous les dossiers avec au moins un document analysé
    analyzed_cases = db.query(Case).join(Document).filter(
        Document.status == "ANALYZED"
    ).distinct().all()
    
    # Calculer la distribution
    fiable = 0      # Score < 20 (Vert)
    signale = 0     # Score 20-74 (Orange)
    anomalie = 0    # Score >= 75 (Rouge)
    
    for case in analyzed_cases:
        # Récupérer les documents analysés du dossier
        docs = db.query(Document).filter(
            Document.case_id == case.id,
            Document.status == "ANALYZED"
        ).all()
        
        if not docs:
            continue
        
        # Calculer le score moyen
        risk_scores = [doc.risk_score for doc in docs if doc.risk_score is not None]
        
        if not risk_scores:
            continue
        
        avg_score = sum(risk_scores) / len(risk_scores)
        
        # Catégoriser
        if avg_score < 20:
            fiable += 1
        elif avg_score < 75:
            signale += 1
        else:
            anomalie += 1
    
    total = fiable + signale + anomalie
    
    # Calculer les pourcentages
    fiable_pct = round((fiable / total * 100), 1) if total > 0 else 0
    signale_pct = round((signale / total * 100), 1) if total > 0 else 0
    anomalie_pct = round((anomalie / total * 100), 1) if total > 0 else 0
    
    print(f"✅ Distribution calculée:")
    print(f"   🟢 Fiable: {fiable} ({fiable_pct}%)")
    print(f"   🟠 Signalé: {signale} ({signale_pct}%)")
    print(f"   🔴 Anomalie: {anomalie} ({anomalie_pct}%)")
    print(f"   📊 Total: {total} dossiers analysés\n")
    
    return {
        "total": total,
        "fiable": {
            "count": fiable,
            "percentage": fiable_pct,
            "label": "Fiable",
            "color": "#10b981",  # Vert
            "description": "Score < 20 - Risque faible"
        },
        "signale": {
            "count": signale,
            "percentage": signale_pct,
            "label": "Signalé",
            "color": "#f59e0b",  # Orange
            "description": "Score 20-74 - Risque modéré"
        },
        "anomalie": {
            "count": anomalie,
            "percentage": anomalie_pct,
            "label": "Anomalie",
            "color": "#ef4444",  # Rouge
            "description": "Score ≥ 75 - Risque élevé"
        }
    }


# ========================================
# SYSTÈME D'ARCHIVES ET APPROBATION
# Routes spécifiques (AVANT /{case_id})
# ========================================

@router.post("/{case_id}/approve")
async def approve_case(
=======
@router.get("/{case_id}", response_model=CaseResponse)
async def get_case(
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
<<<<<<< HEAD
    """
    Approuver un dossier et l'archiver automatiquement
    
    Actions :
    - Change le statut en ARCHIVED
    - Enregistre l'utilisateur qui a approuvé
    - Horodatage de l'approbation
    """
    print(f"\n{'='*60}")
    print(f"APPROBATION DU DOSSIER ID: {case_id}")
    print(f"{'='*60}")
    
    # Récupérer le dossier
    case = db.query(Case).filter(Case.id == case_id).first()
    
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    # Vérifier qu'il y a au moins un document analysé
    analyzed_docs = db.query(Document).filter(
        Document.case_id == case_id,
        Document.status == "ANALYZED"
    ).all()
    
    if not analyzed_docs:
        raise HTTPException(
            status_code=400, 
            detail="Impossible d'approuver : aucun document analysé"
        )
    
    # Calculer le score de risque moyen
    risk_scores = [doc.risk_score for doc in analyzed_docs if doc.risk_score is not None]
    avg_risk_score = sum(risk_scores) / len(risk_scores) if risk_scores else 0
    
    # Déterminer le niveau de risque pour l'archive
    if avg_risk_score < 20:
        archive_category = "AUCUN_RISQUE"
        risk_level = "FAIBLE"
    elif avg_risk_score < 75:
        archive_category = "SIGNALE"
        risk_level = "MOYEN"
    else:
        archive_category = "ANOMALIE"
        risk_level = "ELEVE"
    
    # Mettre à jour le dossier
    case.status = "ARCHIVED"
    case.risk_score = int(avg_risk_score)
    case.risk_level = risk_level
=======
    """Récupérer un dossier par son ID"""
    
    print(f"🔵 Récupération du dossier ID: {case_id}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    
    if not case:
        print(f"❌ Dossier {case_id} non trouvé")
        raise HTTPException(status_code=404, detail=f"Dossier {case_id} non trouvé")
    
    print(f"✅ Dossier trouvé: {case.case_number}")
    
    return case


@router.patch("/{case_id}/status", response_model=CaseResponse)
async def update_case_status(
    case_id: int,
    status_update: CaseStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour le statut d'un dossier"""
    
    print(f"🔵 Mise à jour du statut du dossier {case_id} vers {status_update.status}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    # Vérifier que le statut est valide
    valid_statuses = ["OPEN", "IN_PROGRESS", "CLOSED", "ARCHIVED"]
    if status_update.status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f"Statut invalide. Valeurs possibles: {valid_statuses}")
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
    
    case.status = status_update.status
    db.commit()
    db.refresh(case)
    
<<<<<<< HEAD
    # Créer une note automatique d'approbation
    approval_note = Note(
        case_id=case_id,
        content=f"""DOSSIER APPROUVÉ ET ARCHIVÉ

Approuvé par : {current_user.full_name or current_user.username}
Date d'approbation : {datetime.now().strftime("%d/%m/%Y à %H:%M")}
Score de risque final : {int(avg_risk_score)}/100
Catégorie d'archive : {archive_category}
Niveau de risque : {risk_level}

Le dossier a été validé et transféré aux archives.""",
        created_by=current_user.id
    )
    
    db.add(approval_note)
    db.commit()
    
    print(f"Dossier approuvé et archivé")
    print(f"   Score de risque : {int(avg_risk_score)}/100")
    print(f"   Catégorie : {archive_category}")
    print(f"   Niveau : {risk_level}")
    print(f"{'='*60}\n")
    
    return {
        "message": "Dossier approuvé et archivé avec succès",
        "case_id": case_id,
        "status": "ARCHIVED",
        "risk_score": int(avg_risk_score),
        "risk_level": risk_level,
        "archive_category": archive_category
    }


@router.get("/archives")
async def get_archived_cases(
    category: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Récupérer les dossiers archivés, filtrés par catégorie si spécifié
    """
    print(f"\nRécupération des archives (catégorie: {category or 'TOUTES'})")
    
    # Query de base : dossiers archivés
    query = db.query(Case).filter(Case.status == "ARCHIVED")
    
    # Filtrer par catégorie si spécifié
    if category:
        if category == "AUCUN_RISQUE":
            query = query.filter(Case.risk_score < 20)
        elif category == "SIGNALE":
            query = query.filter(Case.risk_score >= 20, Case.risk_score < 75)
        elif category == "ANOMALIE":
            query = query.filter(Case.risk_score >= 75)
    
    # Trier par date de mise à jour (plus récent en premier)
    cases = query.order_by(Case.updated_at.desc()).all()
    
    # Compter par catégorie
    total = len(cases)
    aucun_risque = db.query(Case).filter(
        Case.status == "ARCHIVED",
        Case.risk_score < 20
    ).count()
    signale = db.query(Case).filter(
        Case.status == "ARCHIVED",
        Case.risk_score >= 20,
        Case.risk_score < 75
    ).count()
    anomalie = db.query(Case).filter(
        Case.status == "ARCHIVED",
        Case.risk_score >= 75
    ).count()
    
    print(f"{total} dossier(s) archivé(s) trouvé(s)")
    print(f"   - Aucun risque : {aucun_risque}")
    print(f"   - Signalé : {signale}")
    print(f"   - Anomalie : {anomalie}\n")
    
    return {
        "cases": cases,
        "total": total,
        "stats": {
            "aucun_risque": aucun_risque,
            "signale": signale,
            "anomalie": anomalie
        }
    }


@router.get("/{case_id}", response_model=CaseResponse)
async def get_case(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer un dossier par son ID"""
    
    print(f"🔵 Récupération du dossier ID: {case_id}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    
    if not case:
        print(f"❌ Dossier {case_id} non trouvé")
        raise HTTPException(status_code=404, detail=f"Dossier {case_id} non trouvé")
    
    print(f"✅ Dossier trouvé: {case.case_number}")
    
    return case


@router.put("/{case_id}", response_model=CaseResponse)
async def update_case(
    case_id: int,
    case_update: CaseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour un dossier"""
    
    print(f"🔵 Mise à jour du dossier ID: {case_id}")
    print(f"📦 Données reçues: {case_update}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    
    if not case:
        print(f"❌ Dossier {case_id} non trouvé")
        raise HTTPException(status_code=404, detail=f"Dossier {case_id} non trouvé")
    
    # Mise à jour des champs si fournis
    if case_update.case_number:
        case.case_number = case_update.case_number
    
    if case_update.importer_name:
        case.importer_name = case_update.importer_name
    
    if case_update.declarant_name is not None:
        case.declarant_name = case_update.declarant_name
    
    if case_update.transporter_name is not None:
        case.transporter_name = case_update.transporter_name
    
    if case_update.priority:
        case.priority = case_update.priority
    
    if case_update.description is not None:
        case.description = case_update.description
    
    db.commit()
    db.refresh(case)
    
    print(f"✅ Dossier {case_id} mis à jour avec succès")
    
    return case


@router.patch("/{case_id}/status", response_model=CaseResponse)
async def update_case_status(
    case_id: int,
    status_update: CaseStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour le statut d'un dossier"""
    
    print(f"🔵 Mise à jour du statut du dossier {case_id} vers {status_update.status}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    # Vérifier que le statut est valide
    valid_statuses = ["OPEN", "IN_PROGRESS", "CLOSED", "ARCHIVED"]
    if status_update.status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f"Statut invalide. Valeurs possibles: {valid_statuses}")
    
    case.status = status_update.status
    db.commit()
    db.refresh(case)
    
    print(f"✅ Statut mis à jour: {case.status}")
    
    return case


@router.patch("/{case_id}/priority", response_model=CaseResponse)
async def update_case_priority(
    case_id: int,
    priority_update: CasePriorityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour la priorité d'un dossier"""
    
    print(f"🔵 Mise à jour de la priorité du dossier {case_id} vers {priority_update.priority}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    # Vérifier que la priorité est valide
    valid_priorities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    if priority_update.priority not in valid_priorities:
        raise HTTPException(status_code=400, detail=f"Priorité invalide. Valeurs possibles: {valid_priorities}")
    
    case.priority = priority_update.priority
    db.commit()
    db.refresh(case)
    
    print(f"✅ Priorité mise à jour: {case.priority}")
    
    return case


@router.delete("/{case_id}")
async def delete_case(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Supprimer un dossier et tous ses documents/notes associés"""
    
    print(f"\n🗑️  SUPPRESSION DU DOSSIER {case_id}")
    
    # Récupérer le dossier
    case = db.query(Case).filter(Case.id == case_id).first()
    
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    case_number = case.case_number
    
    # Supprimer les documents associés (fichiers + DB)
    documents = db.query(Document).filter(Document.case_id == case_id).all()
    
    for doc in documents:
        # Supprimer le fichier physique
        try:
            if doc.file_path and os.path.exists(doc.file_path):
                os.remove(doc.file_path)
                print(f"   Fichier supprimé: {doc.filename}")
        except Exception as e:
            print(f"   Erreur suppression fichier: {e}")
        
        # Supprimer de la DB
        db.delete(doc)
    
    # Supprimer les notes associées
    notes = db.query(Note).filter(Note.case_id == case_id).all()
    for note in notes:
        db.delete(note)
    
    print(f"   {len(documents)} document(s) supprimé(s)")
    print(f"   {len(notes)} note(s) supprimée(s)")
    
    # Supprimer le dossier
    db.delete(case)
    db.commit()
    
    print(f"Dossier {case_number} supprimé avec succès\n")
    
    return {"message": "Dossier supprimé avec succès"}

=======
    print(f"✅ Statut mis à jour: {case.status}")
    
    return case


@router.patch("/{case_id}/priority", response_model=CaseResponse)
async def update_case_priority(
    case_id: int,
    priority_update: CasePriorityUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour la priorité d'un dossier"""
    
    print(f"🔵 Mise à jour de la priorité du dossier {case_id} vers {priority_update.priority}")
    
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    
    # Vérifier que la priorité est valide
    valid_priorities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    if priority_update.priority not in valid_priorities:
        raise HTTPException(status_code=400, detail=f"Priorité invalide. Valeurs possibles: {valid_priorities}")
    
    case.priority = priority_update.priority
    db.commit()
    db.refresh(case)
    
    print(f"✅ Priorité mise à jour: {case.priority}")
    
    return case
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
