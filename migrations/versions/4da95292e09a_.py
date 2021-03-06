"""empty message

Revision ID: 4da95292e09a
Revises: 5959ae3c0d3e
Create Date: 2016-04-08 11:10:45.730507

"""

# revision identifiers, used by Alembic.
revision = '4da95292e09a'
down_revision = '5959ae3c0d3e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planting')
    op.drop_table('reminder')
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
    op.create_table('reminder',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('title', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('detail', mysql.TEXT(), nullable=True),
    sa.Column('badge', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('create_date', mysql.DATETIME(), nullable=True),
    sa.Column('update_date', mysql.DATETIME(), nullable=True),
    sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('reminder_date', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], name=u'reminder_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('planting',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('plantingType', mysql.VARCHAR(length=75), nullable=True),
    sa.Column('plantName', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('badge', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('publish_date', mysql.DATETIME(), nullable=True),
    sa.Column('update_date', mysql.DATETIME(), nullable=True),
    sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], name=u'planting_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
