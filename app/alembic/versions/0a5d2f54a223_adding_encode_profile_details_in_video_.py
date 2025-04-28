"""Remove stream_url column from users table

Revision ID: affd31695a94
Revises: 0a5d2f54a223
Create Date: 2025-04-25
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'affd31695a94'
down_revision = '0a5d2f54a223'
branch_labels = None
depends_on = None


def upgrade():
    # Remove the stream_url column from the users table
    op.drop_column('users', 'stream_url')


def downgrade():
    # Re-add the stream_url column in case of rollback
    op.add_column('users', sa.Column('stream_url', sa.String(255), nullable=True))
