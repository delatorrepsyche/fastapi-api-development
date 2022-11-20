"""create posts table

Revision ID: f37cc3b33d56
Revises: 
Create Date: 2022-11-18 09:30:35.123169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f37cc3b33d56'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
