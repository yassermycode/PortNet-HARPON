import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# 1. Importe tes paramètres et tes modèles
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.core.config import settings
from app.db.base import Base  # C'est ici que tous tes modèles sont rassemblés

# 2. Config Alembic
config = context.config

# Configure les logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 3. Injecte l'URL de la DB depuis ton .env (via settings)
config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))

# 4. Lie les métadonnées (pour qu'Alembic "voie" tes tables)
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Gestion spéciale pour que ça marche avec ou sans Async (ici setup standard sync pour Alembic)
    connectable = context.config.attributes.get("connection", None)

    if connectable is None:
        from sqlalchemy import create_engine
        connectable = create_engine(settings.DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()