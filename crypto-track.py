#!/usr/bin/env python3

import requests
import json

with open("crypto-track.json" , 'r') as file:
    data = json.load(file)

CURRENCY = data[0]["CURRENCY"]
SYMBOLS = data[0]["SYMBOLS"] 
total_balance = 0

for item in data[1:]:
    WALLET_ADDRESS = item["WALLET_ADDRESS"]
    SHORTNAME = item["SHORTNAME"]
    FULLNAME = item["FULLNAME"]
    blockcypher_url = f"https://api.blockcypher.com/v1/{SHORTNAME}/main/addrs/{WALLET_ADDRESS}/balance"
    coingecko_url = f"https://api.coingecko.com/api/v3/simple/price?ids={FULLNAME}&vs_currencies={CURRENCY}"

    wallet_request = requests.get(url=blockcypher_url).json()
    wallet_balance = wallet_request["balance"] / 1e8

    price_request = requests.get(url=coingecko_url).json()
    price = price_request[FULLNAME][CURRENCY]

    balance = wallet_balance * price
    total_balance += balance

print(f"{SYMBOLS} {total_balance:.2f}")