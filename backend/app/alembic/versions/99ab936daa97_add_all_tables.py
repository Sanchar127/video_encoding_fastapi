"""add all tables

Revision ID: 99ab936daa97
Revises: 
Create Date: 2025-04-29 15:39:46.670144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ab936daa97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create 's3_credentials' table with proper foreign key and InnoDB support
    op.create_table('s3_credentials',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('access_key', sa.String(length=60), nullable=False),
        sa.Column('secret_key', sa.String(length=60), nullable=False),
        sa.Column('region', sa.String(length=50), nullable=False),
        sa.Column('endpoint', sa.String(length=255), nullable=False),
        sa.Column('bucket', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB'  # Ensure using InnoDB engine for foreign key support
    )
    op.create_index(op.f('ix_s3_credentials_id'), 's3_credentials', ['id'], unique=False)

    # Create 'system_config' table with proper foreign key and InnoDB support
    op.create_table('system_config',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('config_key', sa.String(length=100), nullable=False),
        sa.Column('config_value', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('updated_by', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['updated_by'], ['users.unique_id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('config_key'),
        mysql_engine='InnoDB'  # Ensure using InnoDB engine for foreign key support
    )
    op.create_index(op.f('ix_system_config_id'), 'system_config', ['id'], unique=False)
    

def downgrade() -> None:
    # Drop the indexes first (important for foreign key dependencies)
    op.drop_index(op.f('ix_system_config_id'), table_name='system_config')
    op.drop_index(op.f('ix_s3_credentials_id'), table_name='s3_credentials')
    
    # Drop the tables in reverse order to avoid foreign key issues
    op.drop_table('system_config')
    op.drop_table('s3_credentials')
