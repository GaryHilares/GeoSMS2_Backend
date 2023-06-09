from typing import List
from api.control import exceptions
from api.database.cache import set_cache, get_cache
import requests


def get_exchange_rate(args: List[str]) -> str:
    from_currency = args[0]
    to_currency = args[1]
    rate = get_cache(f"curr-{from_currency}-{to_currency}")
    if not rate:
        rates = requests.get(
            f"https://open.er-api.com/v6/latest/{from_currency}"
        ).json()
        if "rates" not in rates or to_currency not in rates["rates"]:
            raise exceptions.WrongArgumentsException("get_exchange_rate", args)
        rate = rates["rates"][to_currency]
        set_cache(f"curr-{from_currency}-{to_currency}", rate)
    return f"{rate} (ExchangeRate-API)"
