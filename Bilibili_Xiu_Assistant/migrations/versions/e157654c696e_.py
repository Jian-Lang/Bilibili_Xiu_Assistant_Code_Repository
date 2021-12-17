"""empty message

Revision ID: e157654c696e
Revises: 29a7cef00dc3
Create Date: 2021-11-20 16:26:14.694482

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e157654c696e'
down_revision = '29a7cef00dc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Sign', sa.String(length=255), nullable=True))
    op.drop_column('user', 'icon')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('icon', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True))
    op.drop_column('user', 'Sign')
    # ### end Alembic commands ###
