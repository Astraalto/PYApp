import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine("sqlit:///crypto.db")

query = "SELCT * FROM prices"
df = pd.read_sql(query, engine)

print("Average prices: ")
print(df.mean())