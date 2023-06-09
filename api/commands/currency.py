from typing import List
from api.control import exceptions
import requests

def get_exchange_rate(args: List[str]) -> str:
    from_currency = args[0]
    to_currency = args[1]
    rates = requests.get(f"https://open.er-api.com/v6/latest/{from_currency}").json()
    if "rates" not in rates or to_currency not in rates["rates"]:
        raise exceptions.WrongArgumentsException("get_exchange_rate", args)
    rate = rates["rates"][to_currency]
    return f"{rate} (ExchangeRate-API)"