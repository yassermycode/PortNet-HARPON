"""
Script pour initialiser la table users avec SQL direct.
"""

from app.db.session import engine
from sqlalchemy import text

def init_users_table():
    """Crée la table users avec SQL direct."""
    
    sql = """
    -- Supprimer la table si elle existe
    DROP TABLE IF EXISTS users CASCADE;
    
    -- Créer la table users
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        hashed_password VARCHAR(255) NOT NULL,
        full_name VARCHAR(255),
        role VARCHAR(50) NOT NULL DEFAULT 'ANALYST',
        is_active BOOLEAN DEFAULT TRUE,
        is_superuser BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    );
    
    -- Créer les index
    CREATE INDEX idx_users_username ON users(username);
    CREATE INDEX idx_users_email ON users(email);
    CREATE INDEX idx_users_role ON users(role);
    """
    
    print("🔄 Création de la table users...")
    
    with engine.connect() as conn:
        conn.execute(text(sql))
        conn.commit()
    
    print("✅ Table users créée avec succès !")

if __name__ == "__main__":
    init_users_table()
