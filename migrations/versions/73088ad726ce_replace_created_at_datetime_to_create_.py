"""replace created_at datetime to create_at float

Revision ID: 73088ad726ce
Revises: 03bb6f684c1a
Create Date: 2023-07-14 07:48:09.496977

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '73088ad726ce'
down_revision = '03bb6f684c1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cross_course', sa.Column('create_at', sa.Float(), nullable=True))
    op.drop_column('cross_course', 'created_at')
    op.add_column('currency', sa.Column('create_at', sa.Float(), nullable=True))
    op.drop_column('currency', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('currency', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('currency', 'create_at')
    op.add_column('cross_course', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('cross_course', 'create_at')
    # ### end Alembic commands ###
