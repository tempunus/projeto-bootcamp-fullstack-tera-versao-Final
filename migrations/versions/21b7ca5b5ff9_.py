
"""mensagem vazia

ID da revisão: 21b7ca5b5ff9
Revisões:
Data de criação: 2017-08-16 20:07:52.722542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21b7ca5b5ff9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    
    # ### comandos gerados automaticamente pelo Alembic 
    # - ajuste por favor! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    # ### fim dos comandos do Alambique ##


def downgrade():
    
    # ### comandos gerados automaticamente pelo 
    # Alembic - ajuste por favor! ###
    op.drop_table('courses')
    op.drop_table('users')
    # ### fim dos comandos do Alambique ##
