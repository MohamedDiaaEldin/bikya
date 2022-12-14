"""empty message

Revision ID: 9126481a3e53
Revises: bb08bbd03a74
Create Date: 2022-07-28 22:28:08.707793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9126481a3e53'
down_revision = 'bb08bbd03a74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer_otp',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('otp', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('matrial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('buy_category_matrial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matrial_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['matrial_id'], ['matrial.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['zone_id'], ['zone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matrial_category',
    sa.Column('matrial_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('total_weight', sa.Float(), nullable=False),
    sa.Column('km_price', sa.Float(), nullable=False),
    sa.Column('km_points', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['matrial_id'], ['matrial.id'], ),
    sa.PrimaryKeyConstraint('matrial_id', 'category_id')
    )
    op.create_table('sell_categorymatrial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matrial_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('delivery_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('points', sa.Float(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['delivery_id'], ['delivery.id'], ),
    sa.ForeignKeyConstraint(['matrial_id'], ['matrial.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sell_categorymatrial')
    op.drop_table('matrial_category')
    op.drop_table('delivery')
    op.drop_table('buy_category_matrial')
    op.drop_table('zone')
    op.drop_table('matrial')
    op.drop_table('customer_otp')
    op.drop_table('admin')
    # ### end Alembic commands ###
