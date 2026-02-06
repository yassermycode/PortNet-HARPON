import sys
import os
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine
from app.db.base_class import Base  # ← Importé ici

# Import TOUS les models
from app.db.models.case import Case
from app.db.models.document import Document
from app.db.models.extraction import Extraction
from app.db.models.entity import Entity
from app.db.models.case_entity_link import CaseEntityLink
from app.db.models.feature import Feature
from app.db.models.signal import Signal
from app.db.models.document_similarity import DocumentSimilarity
from app.db.models.audit_log import AuditLog

from app.constants import CaseStatus, RiskLevel, RecommendedAction, EntityType, EventType
from datetime import datetime, timedelta
import random
# Add backend to path
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine
from app.db.base_class import Base  # ← Importé ici

# Import TOUS les models
from app.db.models.case import Case
from app.db.models.document import Document
from app.db.models.extraction import Extraction
from app.db.models.entity import Entity
from app.db.models.case_entity_link import CaseEntityLink
from app.db.models.feature import Feature
from app.db.models.signal import Signal
from app.db.models.document_similarity import DocumentSimilarity
from app.db.models.audit_log import AuditLog

from app.constants import CaseStatus, RiskLevel, RecommendedAction, EntityType, EventType
from datetime import datetime, timedelta
import random

# Force SQLAlchemy à charger tous les mappers
from app.db.base import Base
_ = [Case, Document, Extraction, Entity, CaseEntityLink, Feature, Signal, DocumentSimilarity, AuditLog]

def clear_data(db: Session):
    """Supprime toutes les données existantes"""
    db.query(AuditLog).delete()
    db.query(Signal).delete()
    db.query(Feature).delete()
    db.query(CaseEntityLink).delete()
    db.query(Entity).delete()
    db.query(Case).delete()
    db.commit()
    print("🗑️  Données existantes supprimées")


def create_entities(db: Session):
    """Crée 25 entités (8 importers, 8 forwarders, 9 suppliers)"""
    entities = []
    
    # 8 IMPORTERS
    importers = [
        "ACME_IMPORT", "GLOBEX_TRADE", "SOKOLOW_GOODS", "INITECH_SA",
        "UMBRELLA_CORP", "WAYNE_IMPORT", "STARK_TRADE", "OSCORP_LOGISTICS"
    ]
    for name in importers:
        entity = Entity(
            name=name,
            normalized_name=name,
            entity_type=EntityType.IMPORTER.value,
            risk_score_history=[]
        )
        entities.append(entity)
        db.add(entity)
    
    # 8 FORWARDERS
    forwarders = [
        "DHL_FORWARDING", "MAERSK_LOGISTICS", "FEDEX_FREIGHT", "KUEHNE_NAGEL",
        "BOLLORE_LOGISTICS", "GEFCO_TRANSIT", "SCHENKER_FORWARD", "PANALPINA_SERVICES"
    ]
    for name in forwarders:
        entity = Entity(
            name=name,
            normalized_name=name,
            entity_type=EntityType.FORWARDER.value,
            risk_score_history=[]
        )
        entities.append(entity)
        db.add(entity)
    
    # 9 SUPPLIERS
    suppliers = [
        "CHINA_FACTORY_A", "VIETNAM_ELECTRONICS", "INDIA_TEXTILES", "TURKEY_STEEL",
        "POLAND_MACHINERY", "GERMANY_AUTO_PARTS", "ITALY_FURNITURE", "SPAIN_CERAMICS",
        "THAILAND_PLASTICS"
    ]
    for name in suppliers:
        entity = Entity(
            name=name,
            normalized_name=name,
            entity_type=EntityType.SUPPLIER.value,
            risk_score_history=[]
        )
        entities.append(entity)
        db.add(entity)
    
    db.commit()
    print(f"✅ {len(entities)} entités créées")
    return entities


def create_cases(db: Session, entities: list):
    """Crée 50 cases (45 normaux + 5 frauduleux)"""
    cases = []
    
    for i in range(1, 51):
        reference_id = f"REF-{2026000 + i}"
        
        # Dossiers frauduleux tous les 10
        if i % 10 == 0:
            status = CaseStatus.FLAGGED.value
            global_score = random.randint(75, 95)
            risk_level = random.choice([RiskLevel.HIGH.value, RiskLevel.CRITICAL.value])
            recommended_action = RecommendedAction.INSPECT.value
            created_at = datetime.now() - timedelta(days=random.randint(1, 15))
        else:
            status = CaseStatus.CLEARED.value
            global_score = random.randint(5, 35)
            risk_level = RiskLevel.LOW.value
            recommended_action = RecommendedAction.RELEASE.value
            created_at = datetime.now() - timedelta(days=random.randint(1, 30))
        
        case = Case(
            reference_id=reference_id,
            status=status,
            global_score=global_score,
            risk_level=risk_level,
            recommended_action=recommended_action,
            risk_breakdown_json={"details": "Auto-generated"},
            created_at=created_at,
            updated_at=created_at
        )
        db.add(case)
        db.flush()  # Pour obtenir l'id
        cases.append(case)
    
    db.commit()
    print(f"✅ {len(cases)} cases créés (45 normaux + 5 frauduleux)")
    return cases


def link_entities_to_cases(db: Session, cases: list, entities: list):
    """Lie les entités aux cases"""
    importers = [e for e in entities if e.entity_type == EntityType.IMPORTER.value]
    forwarders = [e for e in entities if e.entity_type == EntityType.FORWARDER.value]
    suppliers = [e for e in entities if e.entity_type == EntityType.SUPPLIER.value]
    
    # Entités suspectes pour les cas frauduleux (créer un cluster)
    suspicious_importer = entities[0]  # ACME_IMPORT
    suspicious_forwarder = entities[8]  # DHL_FORWARDING
    suspicious_supplier = entities[16]  # CHINA_FACTORY_A
    
    links_count = 0
    
    for case in cases:
        # Choisir les entités
        if case.global_score > 70:  # Frauduleux - utiliser entités suspectes
            importer = suspicious_importer
            forwarder = suspicious_forwarder
            supplier = suspicious_supplier
        else:  # Normal - entités aléatoires
            importer = random.choice(importers)
            forwarder = random.choice(forwarders)
            supplier = random.choice(suppliers)
        
        # Créer les liens
        link1 = CaseEntityLink(case_id=case.id, entity_id=importer.id, role="importer")
        link2 = CaseEntityLink(case_id=case.id, entity_id=forwarder.id, role="forwarder")
        link3 = CaseEntityLink(case_id=case.id, entity_id=supplier.id, role="supplier")
        
        db.add(link1)
        db.add(link2)
        db.add(link3)
        links_count += 3
    
    db.commit()
    print(f"✅ {links_count} liens entités-cases créés")


def create_features(db: Session, cases: list):
    """Crée des features pour chaque case"""
    features_count = 0
    
    for case in cases:
        is_fraudulent = case.global_score > 70
        
        # Feature 1: total_weight
        if is_fraudulent:
            total_weight = random.uniform(15000, 50000)  # Outlier
        else:
            total_weight = random.uniform(100, 5000)
        
        # Feature 2: declared_value
        if is_fraudulent:
            declared_value = random.uniform(500000, 2000000)  # Outlier
        else:
            declared_value = random.uniform(1000, 50000)
        
        # Feature 3: price_per_kg
        price_per_kg = declared_value / total_weight
        
        # Feature 4: hs_code_risk
        if is_fraudulent:
            hs_code_risk = random.uniform(0.7, 0.95)
        else:
            hs_code_risk = random.uniform(0.1, 0.3)
        
        # Créer les features
        db.add(Feature(case_id=case.id, feature_name="total_weight", feature_value=total_weight))
        db.add(Feature(case_id=case.id, feature_name="declared_value", feature_value=declared_value))
        db.add(Feature(case_id=case.id, feature_name="price_per_kg", feature_value=price_per_kg))
        db.add(Feature(case_id=case.id, feature_name="hs_code_risk", feature_value=hs_code_risk))
        features_count += 4
    
    db.commit()
    print(f"✅ {features_count} features créées")


def create_signals(db: Session, cases: list):
    """Crée des signaux pour les cases frauduleux"""
    signals_count = 0
    
    for case in cases:
        if case.global_score > 70:  # Frauduleux uniquement
            # Récupérer les features
            features = db.query(Feature).filter(Feature.case_id == case.id).all()
            feature_dict = {f.feature_name: f.feature_value for f in features}
            
            # Signal 1: WEIGHT_ANOMALY
            signal1 = Signal(
                case_id=case.id,
                algo_source="rule_engine",
                signal_type="WEIGHT_ANOMALY",
                severity="HIGH",
                score_contribution=25,
                evidence_json={
                    "reason": "Poids déclaré dépasse capacité conteneur",
                    "expected_max": 28000,
                    "declared": feature_dict.get("total_weight", 0)
                }
            )
            db.add(signal1)
            signals_count += 1
            
            # Signal 2: PRICE_ANOMALY
            signal2 = Signal(
                case_id=case.id,
                algo_source="rule_engine",
                signal_type="PRICE_ANOMALY",
                severity="MEDIUM",
                score_contribution=20,
                evidence_json={
                    "reason": "Prix/kg anormalement bas",
                    "market_avg": 15.5,
                    "declared": feature_dict.get("price_per_kg", 0)
                }
            )
            db.add(signal2)
            signals_count += 1
    
    db.commit()
    print(f"✅ {signals_count} signaux créés")


def create_audit_logs(db: Session, cases: list):
    """Crée des logs d'audit pour chaque case"""
    logs_count = 0
    
    for case in cases:
        # Log 1: CASE_CREATED
        log1 = AuditLog(
            case_id=case.id,
            event_type=EventType.CASE_CREATED.value,
            actor="system",
            payload_json={"reference_id": case.reference_id},
            created_at=case.created_at
        )
        db.add(log1)
        logs_count += 1
        
        # Log 2: ANALYSIS_DONE
        log2 = AuditLog(
            case_id=case.id,
            event_type=EventType.ANALYSIS_DONE.value,
            actor="system",
            payload_json={
                "reference_id": case.reference_id,
                "score": case.global_score,
                "risk_level": case.risk_level
            },
            created_at=case.created_at + timedelta(minutes=2)
        )
        db.add(log2)
        logs_count += 1
    
    db.commit()
    print(f"✅ {logs_count} logs d'audit créés")


def main():
    """Fonction principale de seed"""
    print("🌱 Démarrage du seed...")
    
    db = SessionLocal()
    try:
        clear_data(db)
        entities = create_entities(db)
        cases = create_cases(db, entities)
        link_entities_to_cases(db, cases, entities)
        create_features(db, cases)
        create_signals(db, cases)
        create_audit_logs(db, cases)
        
        print(f"\n✅ Seed terminé : 50 cases, 25 entities, 150 links, 200 features, 10 signals, 100 audit logs")
    except Exception as e:
        print(f"❌ Erreur lors du seed: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()

