"""added products and orders_products table

Revision ID: c7cba6f61696
Revises: 7aac20cccc93
Create Date: 2022-04-18 23:11:30.575409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7cba6f61696'
down_revision = '7aac20cccc93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('orders_products',
    sa.Column('register_id', sa.Integer(), nullable=False),
    sa.Column('sale_value', sa.Numeric(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('register_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_products')
    op.drop_table('products')
    # ### end Alembic commands ###
