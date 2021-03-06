"""empty message

Revision ID: 1f0315371b9b
Revises: 762402052503
Create Date: 2021-04-07 01:35:24.980296

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f0315371b9b'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=28), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=28), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('firstname', sa.String(length=15), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(length=15), nullable=False))
    op.add_column('user', sa.Column('username', sa.String(length=50), nullable=False))
    op.create_unique_constraint(None, 'user', ['password'])
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
