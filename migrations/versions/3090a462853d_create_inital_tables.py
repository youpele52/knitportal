"""create inital tables

Revision ID: 3090a462853d
Revises: 
Create Date: 2023-05-09 22:08:38.490352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3090a462853d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('availability', sa.String(), nullable=True),
    sa.Column('needle_size', sa.String(), nullable=True),
    sa.Column('composition', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brand', 'name', name='_brand_name_uc')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
