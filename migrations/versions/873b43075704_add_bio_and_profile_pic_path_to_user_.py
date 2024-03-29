"""Add bio and profile_pic_path to User class

Revision ID: 873b43075704
Revises: d6d7c073a42e
Create Date: 2019-11-21 15:50:39.399874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '873b43075704'
down_revision = 'd6d7c073a42e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
