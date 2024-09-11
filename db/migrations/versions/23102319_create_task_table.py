"""create task table

Revision ID: 23102320
Revises: 00000000
Create Date: 2023-10-23 20:09:13.334975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23102320'
down_revision = '00000000'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('task',
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('state', sa.Enum('TODO', 'IN_PROGRESS', 'DONE', name='taskstate'), nullable=False),
        sa.Column('user_id', sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )


def downgrade():
    op.drop_table('task')
