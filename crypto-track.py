#!/usr/bin/env python3

import requests

WALLET_ADDRESS = ""
CURRENCY = "eur" # Some other examples would be "usd", "jpy", "try", "cad", "chy" and more. For more references, please visit https://docs.coingecko.com/reference/simple-supported-currencies
BLOCKCHYPER_IDS = "btc" # Some other examples would be "ltc", "sol", "ada" and more
COINGECKO_IDS = "bitcoin" # Coins full name
SYMBOLS = "€" # If you want to change the logo for the output, you can change it here


blockcypher_url = f"https://api.blockcypher.com/v1/{BLOCKCHYPER_IDS}/main/addrs/{WALLET_ADDRESS}/balance"
coingecko_url = f"https://api.coingecko.com/api/v3/simple/price?ids={COINGECKO_IDS}&vs_currencies={CURRENCY}"


wallet_request = requests.get(url=blockcypher_url).json()
wallet_balance = wallet_request["balance"] / 1e8

price_request = requests.get(url=coingecko_url).json()
price = price_request[COINGECKO_IDS][CURRENCY]

balance = wallet_balance * price

print(f"{SYMBOLS} {balance:.2f}")