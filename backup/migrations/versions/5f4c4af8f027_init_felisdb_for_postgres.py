"""init felisdb for postgres

Revision ID: 5f4c4af8f027
Revises: 
Create Date: 2020-01-06 13:39:14.451256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f4c4af8f027'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('unique_id', sa.Integer(), nullable=False),
    sa.Column('short_link', sa.String(length=80), nullable=True),
    sa.Column('full_link', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('unique_id'),
    sa.UniqueConstraint('short_link')
    )
    op.create_index(op.f('ix_entry_unique_id'), 'entry', ['unique_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entry_unique_id'), table_name='entry')
    op.drop_table('entry')
    # ### end Alembic commands ###
