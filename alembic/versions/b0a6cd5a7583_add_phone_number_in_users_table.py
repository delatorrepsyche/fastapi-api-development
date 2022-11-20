"""add phone number in users table

Revision ID: b0a6cd5a7583
Revises: b2fb4c9dc74b
Create Date: 2022-11-20 11:32:58.614546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0a6cd5a7583'
down_revision = 'b2fb4c9dc74b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column("users", "phone_number")
    pass
