from sqlalchemy import create_engine
import pandas as pd


engine = create_engine("sqlite:///crypto.db")

df =pd.read_csv("crypto_prices.csv")

df.to_sql(
    "prices", engine, if_exists="append", index=False
)

print("Data inserted")