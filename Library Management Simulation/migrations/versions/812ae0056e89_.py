"""empty message

Revision ID: 812ae0056e89
Revises: 55c5d1e233ed
Create Date: 2021-05-16 02:18:49.887293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '812ae0056e89'
down_revision = '55c5d1e233ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False))
    # ### end Alembic commands ###