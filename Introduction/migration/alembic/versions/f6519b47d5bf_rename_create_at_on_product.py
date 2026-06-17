"""Rename create_at on product

Revision ID: f6519b47d5bf
Revises: a280ac2d9c70
Create Date: 2026-06-17 14:07:47.618574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6519b47d5bf'
down_revision: Union[str, Sequence[str], None] = 'a280ac2d9c70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("product", "create_at", new_column_name="created_at")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("product", "created_at", new_column_name="create_at")
    pass
