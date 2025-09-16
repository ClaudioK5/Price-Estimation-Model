import pandas as pd
import numpy as np
import statsmodels.api as sm
from sqlalchemy import create_engine, text


def elasticity_calculator(product_name):

    db_url = "postgresql://postgres:inserthereyoursqlpassword@localhost:5432/fastapi_clients_orders"

    engine = create_engine(db_url)

    query = text("""SELECT product_name, amount, price FROM orders WHERE product_name = :product_name""")

    df = pd.read_sql(query, engine, params={"product_name": product_name})

    df_item = (df.groupby(['product_name', 'price']).agg(total_amount_sold=('amount', 'sum')).reset_index())

    df_item['log_price'] = np.log(df_item['price'])

    df_item['log_amount'] = np.log(df_item['total_amount_sold'])

    X = sm.add_constant(df_item['log_price'])

    y = df_item['log_amount']

    model = sm.OLS(y, X).fit()

    elasticity = model.params['log_price']


    return elasticity
