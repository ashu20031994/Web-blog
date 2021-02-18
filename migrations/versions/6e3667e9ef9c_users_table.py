"""users table

Revision ID: 6e3667e9ef9c
Revises: 2bbd4afe3455
Create Date: 2021-02-05 12:27:38.126147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e3667e9ef9c'
down_revision = '2bbd4afe3455'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('post_author_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_author_fkey', 'post', 'user', ['author'], ['id'])
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###
