"""empty message

Revision ID: b017f4733af3
Revises: 3b8fcc66fdfc
Create Date: 2023-11-01 16:30:03.438551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b017f4733af3'
down_revision = '3b8fcc66fdfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('datetime_created',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('datetime_created',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###
