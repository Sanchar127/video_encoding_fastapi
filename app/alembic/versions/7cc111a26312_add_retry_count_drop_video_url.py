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

def upgrade():
    op.create_table(
        's3_credentials',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('access_key', sa.String(length=60), nullable=False),
        sa.Column('secret_key', sa.String(length=60), nullable=False),
        sa.Column('region', sa.String(length=50), nullable=False),
        sa.Column('endpoint', sa.String(length=255), nullable=False),
        sa.Column('bucket', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'system_config',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('config_key', sa.String(), nullable=False),
        sa.Column('config_value', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('updated_by', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['updated_by'], ['users.unique_id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('config_key')
    )

    op.drop_column('users', 'stream_url')


def downgrade():
    op.add_column('users', sa.Column('stream_url', sa.String(length=255), nullable=True))
    # op.drop_table('system_config')
    # op.drop_table('s3_credentials')
