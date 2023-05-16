"""change recipe id type to string

Revision ID: 0763ee4b7314
Revises: 969a5b9b30fb
Create Date: 2023-05-10 11:21:02.031848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0763ee4b7314'
down_revision = '969a5b9b30fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('recipes', 'id', type_=sa.UUID)


def downgrade() -> None:
    op.alter_column('recipes', 'id', type_=sa.UUID)
