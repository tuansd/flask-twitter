CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE customers;

-- Run command: 
alembic revision -m "create customers" -- create customers table
alembic upgrade head
alembic downgrade <->
alembic revision -m "add customers date_of_birth"  -- add column date_of_birth to customers table

----------------------
alembic upgrade <->

alembic upgrade head
alembic downgrade base



-- Edit two function:
def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )

def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )


-- Other alembic command:
alembic current

-- SET NOT NULL migration
$ alembic revision -m "set customers date_of_birth"
$ alembic upgrade head
$ alembic downgrade "id from upgrade"