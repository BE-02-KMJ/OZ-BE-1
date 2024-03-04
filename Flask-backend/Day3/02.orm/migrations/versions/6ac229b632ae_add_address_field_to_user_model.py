"""Add address field to User Model

Revision ID: 6ac229b632ae
Revises: 
Create Date: 2024-03-04 14:18:33.320842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ac229b632ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['address'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('address')

    # ### end Alembic commands ###
