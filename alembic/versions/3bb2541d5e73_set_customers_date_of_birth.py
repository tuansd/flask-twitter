"""set customers date_of_birth

Revision ID: 3bb2541d5e73
Revises: 9d5c4726c495
Create Date: 2022-09-27 22:04:39.152295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bb2541d5e73'
down_revision = '9d5c4726c495'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth SET NOT NULL;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth DROP NOT NULL;
        """
    )
