"""add customers date_of_birth

Revision ID: a56ecee8c5e1
Revises: 7d02ad94f1e4
Create Date: 2022-09-27 20:44:05.121353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a56ecee8c5e1'
down_revision = '7d02ad94f1e4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
