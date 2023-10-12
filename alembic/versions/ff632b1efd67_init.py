"""init

Revision ID: ff632b1efd67
Revises: 
Create Date: 2023-10-12 19:34:32.069892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ff632b1efd67"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("question_id", sa.Integer, unique=True),
        sa.Column("question", sa.String, nullable=False),
        sa.Column("answer", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("position", sa.Integer, autoincrement=True, primary_key=True),
    )


def downgrade() -> None:
    op.drop_table("questions")
