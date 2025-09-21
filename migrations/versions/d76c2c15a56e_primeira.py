"""primeira

Revision ID: d76c2c15a56e
Revises: 
Create Date: 2025-09-21 14:54:44.321016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd76c2c15a56e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema.
    faz"""
    op.create_table(
        'pessoa',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema.
    desfaz"""
    op.drop_table('pessoa')
