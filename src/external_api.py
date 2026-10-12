import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_amount(transaction: dict) -> float:
    """Функция возврата стоимости транзакции в рублях"""
    API_KEY = os.getenv("API_KEY")
    amount = float(transaction["amount"])
    result = amount
    currency = transaction["currency"]["code"]
    if currency != "RUB":
        payload: dict = {}
        params = {"amount": str(amount), "from": currency, "to": "RUB"}
        headers = {"apikey": str(API_KEY)}
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        result = float(response.json()["result"])
    return result


#
# print(get_amount({"amount": 100, "currency": {"code": "USD"}}))
