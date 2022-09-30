"""drop fk_orders_customers

Revision ID: ca00b98a3adf
Revises: 2b56b07e1d30
Create Date: 2022-09-27 22:29:36.281782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca00b98a3adf'
down_revision = '2b56b07e1d30'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE orders           
            DROP CONSTRAINT fk_orders_customers;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE orders
            
            ADD CONSTRAINT fk_orders_customers
            FOREIGN KEY(customer_id)
            REFERENCES customers(id)
            ON DELETE CASCADE;
        """
    )
