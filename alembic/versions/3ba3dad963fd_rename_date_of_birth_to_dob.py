"""rename date_of_birth to dob

Revision ID: 3ba3dad963fd
Revises: 99a35e8b63a0
Create Date: 2022-09-27 22:16:52.311472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ba3dad963fd'
down_revision = '99a35e8b63a0'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
            RENAME COLUMN date_of_birth TO dob;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
            RENAME COLUMN dob TO date_of_birth;
        """
    )
