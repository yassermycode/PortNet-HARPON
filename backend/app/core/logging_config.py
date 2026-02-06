"""
Logging Configuration
Configuration centralisée des logs de sécurité.
"""

import logging
import sys
from pathlib import Path

# Créer le dossier logs s'il n'existe pas
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configuration du format des logs
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Logger principal
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT,
    handlers=[
        # Console
        logging.StreamHandler(sys.stdout),
        # Fichier général
        logging.FileHandler("logs/app.log"),
    ]
)

# Logger spécifique pour la sécurité
security_logger = logging.getLogger("security")
security_logger.setLevel(logging.INFO)

# Handler pour les logs de sécurité
security_handler = logging.FileHandler("logs/security.log")
security_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
security_logger.addHandler(security_handler)

# Logger pour les requêtes
request_logger = logging.getLogger("requests")
request_logger.setLevel(logging.INFO)
request_handler = logging.FileHandler("logs/requests.log")
request_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
request_logger.addHandler(request_handler)


def log_security_event(event_type: str, username: str, details: str, success: bool = True):
    """Log un événement de sécurité."""
    status = "SUCCESS" if success else "FAILURE"
    security_logger.info(f"{status} - {event_type} - User: {username} - {details}")


def log_request(method: str, path: str, user: str, status_code: int):
    """Log une requête HTTP."""
    request_logger.info(f"{method} {path} - User: {user} - Status: {status_code}")
