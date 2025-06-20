"""added expenses table

Revision ID: 41e4b252233e
Revises: 574d94e15029
Create Date: 2025-06-09 03:44:48.016094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41e4b252233e'
down_revision: Union[str, None] = '574d94e15029'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('food', 'travel', 'rent', 'outing', name='expensescategory'), nullable=True),
    sa.Column('finance_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['finance_id'], ['finances.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expenses_id'), 'expenses', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_expenses_id'), table_name='expenses')
    op.drop_table('expenses')
    # ### end Alembic commands ###
