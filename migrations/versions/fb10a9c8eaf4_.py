"""empty message

Revision ID: fb10a9c8eaf4
Revises: 
Create Date: 2020-12-27 20:24:10.459767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb10a9c8eaf4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('learners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slackname', sa.String(length=200), nullable=False),
    sa.Column('firstname', sa.String(length=200), nullable=False),
    sa.Column('lastname', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('learners')
    # ### end Alembic commands ###
