from sqlalchemy import text, create_engine


def get_last_price(product_name):

    db_url = "postgresql://postgres:inserthereyoursqlpassword@localhost:5432/fastapi_clients_orders"

    engine = create_engine(db_url)

    query = text("""SELECT price FROM orders WHERE product_name = :product_name ORDER BY timestamp DESC LIMIT 1""")

    with engine.connect() as conn:

        result = conn.execute(query, {"product_name": product_name}).fetchone()

    current_price = float(result[0])


    return current_price