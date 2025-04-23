"""add started_at, ended_at, and video_url to video_jobs

Revision ID: 9bfe9f7e5400
Revises: 66cc7250c32e
Create Date: 2025-04-23 06:34:46.762535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9bfe9f7e5400'
down_revision = '66cc7250c32e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('video_jobs', sa.Column('started_at', sa.DateTime(), nullable=True))
    op.add_column('video_jobs', sa.Column('ended_at', sa.DateTime(), nullable=True))
    op.add_column('video_jobs', sa.Column('video_url', sa.String(length=200), nullable=False))


def downgrade():
    op.drop_column('video_jobs', 'video_url')
    op.drop_column('video_jobs', 'ended_at')
    op.drop_column('video_jobs', 'started_at')

    op.create_index('ix_encode_profile_details_id', 'encode_profile_details', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('unique_id', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('callback_key', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('callback_url', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('callback_secret_key', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('stream_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('is_activated', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('email_notification_status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('email_notification', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('mobile', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('role', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('unique_id', 'users', ['unique_id'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('email', 'users', ['email'], unique=False)
    op.create_table('encode_profiles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.unique_id'], name='encode_profiles_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_encode_profiles_id', 'encode_profiles', ['id'], unique=False)
    op.create_table('video_jobs',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('video_filename', mysql.VARCHAR(length=220), nullable=False),
    sa.Column('job_by', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('encoding_profile', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('status', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['encoding_profile'], ['encode_profiles.id'], name='video_jobs_ibfk_2', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['job_by'], ['users.unique_id'], name='video_jobs_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_video_jobs_id', 'video_jobs', ['id'], unique=False)
    # ### end Alembic commands ###
