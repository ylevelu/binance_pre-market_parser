import requests

SPOT_EXCHANGE_INFO = "https://api.binance.com/api/v3/exchangeInfo"


def get_spot_symbols() -> set:
    r = requests.get(SPOT_EXCHANGE_INFO, timeout=10)
    r.raise_for_status()
    data = r.json()

    return {s["symbol"] for s in data.get("symbols", [])}
