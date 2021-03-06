"""Initial migration.

Revision ID: 2a8862e192ff
Revises: 
Create Date: 2021-02-22 11:53:32.952602

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2a8862e192ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('Forename', sa.String(length=15), nullable=False))
    op.add_column('post', sa.Column('Surname', sa.String(length=15), nullable=False))
    op.drop_column('user', 'Forename')
    op.drop_column('user', 'Surname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Surname', mysql.VARCHAR(length=15), nullable=True))
    op.add_column('user', sa.Column('Forename', mysql.VARCHAR(length=15), nullable=True))
    op.drop_column('post', 'Surname')
    op.drop_column('post', 'Forename')
    # ### end Alembic commands ###
