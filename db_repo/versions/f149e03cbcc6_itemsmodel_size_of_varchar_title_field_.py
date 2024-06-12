"""ItemsModel: size of VARCHAR 'title' field was changed from 20 to 64

Revision ID: f149e03cbcc6
Revises: 19bdba5e3569
Create Date: 2024-06-12 09:09:02.440445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f149e03cbcc6'
down_revision = '19bdba5e3569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=64),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
