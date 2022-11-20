"""add content column to posts table

Revision ID: 0cf036b7b1c8
Revises: f37cc3b33d56
Create Date: 2022-11-18 09:54:51.608714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf036b7b1c8'
down_revision = 'f37cc3b33d56'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
