"""create table order and user

Revision ID: de79071ba9c2
Revises: 
Create Date: 2022-04-15 00:41:22.072233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de79071ba9c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('children', sa.Integer(), nullable=True),
    sa.Column('married', sa.Boolean(), nullable=True),
    sa.Column('account_balance', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('users')
    # ### end Alembic commands ###