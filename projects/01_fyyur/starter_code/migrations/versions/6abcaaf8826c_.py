"""empty message

Revision ID: 6abcaaf8826c
Revises: d4d585087960
Create Date: 2022-05-29 07:51:04.624878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6abcaaf8826c'
down_revision = 'd4d585087960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Venue', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'created_at')
    op.drop_column('Artist', 'created_at')
    # ### end Alembic commands ###
