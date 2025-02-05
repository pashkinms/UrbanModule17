"""empty message

Revision ID: 0bf72580babe
Revises: 2fd59a2eba70
Create Date: 2025-02-05 17:46:13.448302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bf72580babe'
down_revision: Union[str, None] = '2fd59a2eba70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
