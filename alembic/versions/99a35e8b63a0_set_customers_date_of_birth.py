"""set customers date_of_birth

Revision ID: 99a35e8b63a0
Revises: 3bb2541d5e73
Create Date: 2022-09-27 22:10:30.892867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a35e8b63a0'
down_revision = '3bb2541d5e73'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth SET DEFAULT now();
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth DROP DEFAULT;
        """
    )
