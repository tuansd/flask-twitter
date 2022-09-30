"""alter customers date_of_birth

Revision ID: 9d5c4726c495
Revises: a56ecee8c5e1
Create Date: 2022-09-27 21:51:56.238399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d5c4726c495'
down_revision = 'a56ecee8c5e1'
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
