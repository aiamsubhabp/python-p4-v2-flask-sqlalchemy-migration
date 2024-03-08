"""rename address

Revision ID: 0d729d8ba0a8
Revises: 50978936e436
Create Date: 2024-03-08 18:40:34.048911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d729d8ba0a8'
down_revision = '50978936e436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###