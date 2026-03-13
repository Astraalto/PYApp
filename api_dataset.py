import requests
import pandas as pd

URL = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd"
}

response = requests.get(URL, params = params)
data = response.json()

df = pd.DataFrame(data).T
df["timestamp"] = pd.Timestamp.now()

print(df)
df.to_csv("crypto_prices.csv")
