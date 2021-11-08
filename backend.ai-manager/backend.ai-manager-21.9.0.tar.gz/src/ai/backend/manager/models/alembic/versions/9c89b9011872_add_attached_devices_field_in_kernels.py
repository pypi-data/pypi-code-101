"""add_attached_devices_field_in_kernels

Revision ID: 9c89b9011872
Revises: 2a82340fa30e
Create Date: 2019-08-04 16:38:52.781990

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9c89b9011872'
down_revision = '2a82340fa30e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kernels', sa.Column('attached_devices',
                                       postgresql.JSONB(astext_type=sa.Text()),
                                       nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kernels', 'attached_devices')
    # ### end Alembic commands ###
