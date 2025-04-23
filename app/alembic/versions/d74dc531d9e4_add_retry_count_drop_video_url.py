"""Add retry_count, drop video_url

Revision ID: d74dc531d9e4
Revises: 7cc111a26312
Create Date: 2025-04-23 06:53:35.676292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd74dc531d9e4'
down_revision = '7cc111a26312'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
