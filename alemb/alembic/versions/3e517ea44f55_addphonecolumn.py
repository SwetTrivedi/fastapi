"""addphonecolumn

Revision ID: 3e517ea44f55
Revises: 0fd911dc56fb
Create Date: 2025-06-04 15:43:53.710595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e517ea44f55'
down_revision: Union[str, None] = '0fd911dc56fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone",sa.Integer))


def downgrade() -> None:
    op.drop_column("users","phone")
