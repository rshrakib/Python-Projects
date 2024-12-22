# https://api.coinbase.com/v2/prices/buy?currency=usd

import requests

resposnse = requests.get("https://api.coinbase.com/v2/prices/buy?currency=usd")

price = float(resposnse.json()['data']['amount'])
print(price)