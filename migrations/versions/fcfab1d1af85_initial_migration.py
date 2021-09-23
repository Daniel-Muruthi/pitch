"""Initial Migration

Revision ID: fcfab1d1af85
Revises: a75e350b0951
Create Date: 2021-09-23 19:54:34.524739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fcfab1d1af85'
down_revision = 'a75e350b0951'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('minutepitches', sa.Column('postdate', sa.DateTime(), nullable=True))
    op.drop_column('minutepitches', 'postedat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('minutepitches', sa.Column('postedat', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('minutepitches', 'postdate')
    # ### end Alembic commands ###
