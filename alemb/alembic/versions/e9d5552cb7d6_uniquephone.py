"""uniquephone

Revision ID: e9d5552cb7d6
Revises: 3e517ea44f55
Create Date: 2025-06-04 16:17:42.288849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9d5552cb7d6'
down_revision: Union[str, None] = '3e517ea44f55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users")as batch_op:
        batch_op.create_unique_constraint("uq_user_phone",["phone"])


def downgrade() -> None:
     with op.batch_alter_table("users")as batch_op:
        batch_op.drop_constraint("uq_users_phone",type='unique')
