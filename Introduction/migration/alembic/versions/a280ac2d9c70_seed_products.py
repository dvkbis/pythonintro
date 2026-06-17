"""Seed products

Revision ID: a280ac2d9c70
Revises: a5fc3f5357ea
Create Date: 2026-06-17 11:34:10.566173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a280ac2d9c70'
down_revision: Union[str, Sequence[str], None] = 'a5fc3f5357ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    product_type_table = sa.table(
    "product_type",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String),
    sa.column("description", sa.String),
    )


    op.bulk_insert(
        product_type_table,
        [
            {
                "id": 1,
                "name": "Electronics",
                "description": "Electronic devices and accessories",
            },
            {
                "id": 2,
                "name": "Books",
                "description": "Books and documentation",
            },
            {
                "id": 3,
                "name": "Furniture",
                "description": "Office and home furniture",
            },
        ],
    )

    product_table = sa.table(
        "product",
        sa.column("id", sa.Integer),
        sa.column("name", sa.String),
        sa.column("description", sa.String),
        sa.column("price", sa.Float),
        sa.column("product_type_id", sa.Integer),
    )

    op.bulk_insert(
        product_table,
        [
            {
                "id": 1,
                "name": "Dell XPS 15",
                "description": "Professional laptop",
                "price": 1799.99,
                "product_type_id": 1,
            },
            {
                "id": 2,
                "name": "Mechanical Keyboard",
                "description": "RGB mechanical keyboard",
                "price": 129.99,
                "product_type_id": 1,
            },
            {
                "id": 3,
                "name": "Clean Code",
                "description": "Software craftsmanship book",
                "price": 39.99,
                "product_type_id": 2,
            },
            {
                "id": 4,
                "name": "Office Chair",
                "description": "Ergonomic office chair",
                "price": 249.99,
                "product_type_id": 3,
            },
        ],
    )

def downgrade() -> None:
    op.execute(sa.text("DELETE FROM product WHERE id IN (1,2,3,4)"))
    op.execute(sa.text("DELETE FROM product_type WHERE id IN (1,2,3)"))
