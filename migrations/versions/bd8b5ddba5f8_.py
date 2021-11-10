"""empty message

Revision ID: bd8b5ddba5f8
Revises: 2a8862e192ff
Create Date: 2021-02-22 11:58:24.591087

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd8b5ddba5f8'
down_revision = '2a8862e192ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'Forename')
    op.drop_column('post', 'Surname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('Surname', mysql.VARCHAR(length=15), nullable=False))
    op.add_column('post', sa.Column('Forename', mysql.VARCHAR(length=15), nullable=False))
    # ### end Alembic commands ###
