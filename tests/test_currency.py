from api.commands.currency import get_exchange_rate
from dotenv import load_dotenv

load_dotenv()


def test_rate_conversion():
    assert 3.5 <= float(get_exchange_rate(["USD", "PEN"]).split(" ")[0]) <= 4.0
    assert 0.0 <= float(get_exchange_rate(["PEN", "USD"]).split(" ")[0]) <= 0.5
