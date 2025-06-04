"""create freebies table

Revision ID: xxxx
Revises: 7a71dbf71c64
Create Date: 2025-06-04 12:00:00

"""
from alembic import op
import sqlalchemy as sa


revision = 'xxxx'
down_revision = '7a71dbf71c64'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False)
    )


def downgrade():
    op.drop_table('freebies')
