"""empty message

Revision ID: 8712245b1f5f
Revises: 96a474b8a6cd
Create Date: 2016-03-24 19:55:04.684467

"""

# revision identifiers, used by Alembic.
revision = '8712245b1f5f'
down_revision = '96a474b8a6cd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sb__user')
    op.drop_table('sb__bookmark')
    op.alter_column('diary', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('diary', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.create_table('sb__bookmark',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('url', mysql.TEXT(), nullable=False),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('sb__user',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
