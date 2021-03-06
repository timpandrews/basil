"""empty message

Revision ID: 04f37dfcd4ed
Revises: 5718bcd79157
Create Date: 2016-03-31 12:19:25.364521

"""

# revision identifiers, used by Alembic.
revision = '04f37dfcd4ed'
down_revision = '5718bcd79157'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.Column('badge', sa.String(length=256), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column(u'diary', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column(u'following', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column(u'user', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'user', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column(u'following', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column(u'diary', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_table('reminder')
    ### end Alembic commands ###
