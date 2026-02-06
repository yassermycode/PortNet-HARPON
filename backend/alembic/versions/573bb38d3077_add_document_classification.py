"""add_document_classification

Revision ID: 573bb38d3077
Revises: 99b91d6b076f
Create Date: 2026-02-04 22:01:10.943871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '573bb38d3077'
down_revision: Union[str, None] = '99b91d6b076f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('documents', sa.Column('document_type', sa.String(), nullable=True))
    op.add_column('documents', sa.Column('classification_confidence', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('documents', 'classification_confidence')
    op.drop_column('documents', 'document_type')