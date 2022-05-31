"""empty message

Revision ID: 657d5dc73f25
Revises: 6abcaaf8826c
Create Date: 2022-05-30 18:19:45.158555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657d5dc73f25'
down_revision = '6abcaaf8826c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###