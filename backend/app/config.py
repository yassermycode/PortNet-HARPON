from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "PortNet HARPON"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Database - PostgreSQL
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "admin"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "harpon_db"
    
    # Database URL (SQLite par défaut si pas de PostgreSQL)
    DATABASE_URL: str = "sqlite:///./portnet_harpon.db"
    
    # JWT
    SECRET_KEY: str = "votre-clef-secrete-super-securisee-changez-moi-en-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 heures
    
    # CORS
    BACKEND_CORS_ORIGINS: str = "*"
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_PER_MINUTE: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"  # Permet les champs supplémentaires

settings = Settings()
