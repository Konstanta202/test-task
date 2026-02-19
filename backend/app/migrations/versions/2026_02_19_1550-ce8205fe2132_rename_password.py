"""rename password

Revision ID: ce8205fe2132
Revises: f44552105606
Create Date: 2026-02-19 15:50:33.704981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce8205fe2132'
down_revision: Union[str, Sequence[str], None] = 'f44552105606'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'hash_password', new_column_name='password')


def downgrade() -> None:
    op.alter_column('users', 'password', new_column_name='hash_password')
