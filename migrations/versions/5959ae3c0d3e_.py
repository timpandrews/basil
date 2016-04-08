"""empty message

Revision ID: 5959ae3c0d3e
Revises: 4f851adcf334
Create Date: 2016-04-06 12:11:42.917426

"""

# revision identifiers, used by Alembic.
revision = '5959ae3c0d3e'
down_revision = '4f851adcf334'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feed', sa.Column('plantName', sa.String(length=256), nullable=True))
    op.add_column('feed', sa.Column('plantingDate', sa.DateTime(), nullable=True))
    op.add_column('feed', sa.Column('plantingType', sa.String(length=4), nullable=True))
    op.add_column('feed', sa.Column('reminderEndDate', sa.DateTime(), nullable=True))
    op.add_column('feed', sa.Column('reminderStartDate', sa.DateTime(), nullable=True))
    op.alter_column('feed', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('feed', 'public',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('following', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('planting', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('reminder', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('user', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('reminder', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('planting', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('following', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('feed', 'public',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('feed', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_column('feed', 'reminderStartDate')
    op.drop_column('feed', 'reminderEndDate')
    op.drop_column('feed', 'plantingType')
    op.drop_column('feed', 'plantingDate')
    op.drop_column('feed', 'plantName')
    ### end Alembic commands ###
