"""create user table

Revision ID: 00000000
Revises: 
Create Date: 2023-10-23 19:08:52.809189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00000000'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('registered', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('user')
