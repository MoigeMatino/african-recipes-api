"""change recipe id type to string

Revision ID: 22a4b9b3a2ca
Revises: 969a5b9b30fb
Create Date: 2023-05-10 11:16:39.955087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22a4b9b3a2ca'
down_revision = '969a5b9b30fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('recipes', 'id', type_=sa.types.UUID)


def downgrade() -> None:
    op.alter_column('recipes', 'id', type_=sa.String)
