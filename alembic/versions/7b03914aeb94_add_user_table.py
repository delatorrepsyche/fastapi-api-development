"""add user table

Revision ID: 7b03914aeb94
Revises: 0cf036b7b1c8
Create Date: 2022-11-20 11:07:39.975143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b03914aeb94'
down_revision = '0cf036b7b1c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email"))
    pass

def downgrade() -> None:
    op.drop_table("users")
    pass