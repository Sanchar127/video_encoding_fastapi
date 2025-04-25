"""Adding  encode profile details in video job

Revision ID: 0a5d2f54a223
Revises: 477952827354
Create Date: 2025-04-24 09:58:11.596180

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a5d2f54a223'
down_revision = '477952827354'
branch_labels = None
depends_on = None


"""Add encoding_profileDetails column to video_jobs"""



def upgrade():
    # Add the new column to the video_jobs table
    op.add_column('video_jobs', sa.Column('encoding_profileDetails', sa.Integer(), nullable=False))


def downgrade():
    # If we need to rollback, drop the column
    op.drop_column('video_jobs', 'encoding_profileDetails')
