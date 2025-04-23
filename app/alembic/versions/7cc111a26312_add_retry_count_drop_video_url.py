"""add encoding_profileDetails column

Revision ID: 7cc111a26312
Revises: 9bfe9f7e5400
Create Date: 2025-04-23 06:50:39.706102
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7cc111a26312'
down_revision = '9bfe9f7e5400'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'video_jobs',
        sa.Column('encoding_profileDetails', sa.Integer(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('video_jobs', 'encoding_profileDetails')
