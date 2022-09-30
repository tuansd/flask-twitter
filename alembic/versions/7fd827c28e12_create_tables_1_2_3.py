"""create tables 1 2 3

Revision ID: 7fd827c28e12
Revises: ca00b98a3adf
Create Date: 2022-09-27 22:34:43.623638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fd827c28e12'
down_revision = 'ca00b98a3adf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE table1 (id SERIAL PRIMARY KEY);
        CREATE TABLE table2 (id SERIAL PRIMARY KEY);
        CREATE TABLE table3 (id SERIAL PRIMARY KEY);
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE table1;
        DROP TABLE table2;
        DROP TABLE table3;
        """
    )
