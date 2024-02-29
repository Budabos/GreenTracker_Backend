"""Updated user model

Revision ID: c113e30be4ec
Revises: 52a8d00bb3b7
Create Date: 2024-02-29 19:00:06.708549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c113e30be4ec'
down_revision = '52a8d00bb3b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_status', sa.String(), server_default='active', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('account_status')

    # ### end Alembic commands ###