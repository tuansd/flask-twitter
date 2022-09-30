"""create orders

Revision ID: 2b56b07e1d30
Revises: 3ba3dad963fd
Create Date: 2022-09-27 22:20:51.018955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b56b07e1d30'
down_revision = '3ba3dad963fd'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE orders(
            id SERIAL PRIMARY KEY,
            dollar_amount_spent NUMERIC,
            customer_id INT NOT NULL,
            CONSTRAINT fk_orders_customers
                FOREIGN KEY(customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE orders;
        """
    )
