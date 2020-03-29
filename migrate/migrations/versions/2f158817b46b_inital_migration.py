"""Inital migration

Revision ID: 2f158817b46b
Revises: 
Create Date: 2020-03-30 01:03:03.675571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f158817b46b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('organization_needs')
    op.drop_table('organizations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organizations',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('contact_email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('zip_code', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.VARCHAR(length=300), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=300), autoincrement=False, nullable=True),
    sa.Column('accepts_opened', sa.VARCHAR(length=300), autoincrement=False, nullable=True),
    sa.Column('instructions', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('needs', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='organizations_pkey')
    )
    op.create_table('organization_needs',
    sa.Column('organization_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('need', sa.VARCHAR(length=100), autoincrement=False, nullable=False)
    )
    # ### end Alembic commands ###
