"""empty message

Revision ID: 228b6bc0f524
Revises: 
Create Date: 2022-03-29 09:48:38.006371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228b6bc0f524'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tid', sa.Integer(), nullable=True),
    sa.Column('field1_1', sa.VARCHAR(), nullable=True),
    sa.Column('field2_1', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['tid'], ['test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test1')
    # ### end Alembic commands ###
