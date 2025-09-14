from decide_price_strategy import decide_price_strategy
from elasticity_calculator import elasticity_calculator
from get_last_price import get_last_price
from sqlalchemy import create_engine
import pandas as pd
import time
from datetime import datetime, timedelta

db_url = "postgresql://postgres:inserthereyoursqlpassword@localhost:5432/fastapi_clients_orders"

engine = create_engine(db_url)

product_list = pd.read_sql("SELECT DISTINCT product_name FROM orders", engine)["product_name"].tolist()


while True:

    today = datetime.today()


    if (today + timedelta(days=1)).day == 1:

        for product_name in product_list:

           elasticity = elasticity_calculator(product_name)

           current_price = get_last_price(product_name)

           new_price = decide_price_strategy(elasticity, current_price)

           JSON_result = { "product_name": product_name, "price": new_price}

        time.sleep(86400)

    time.sleep(86400)





