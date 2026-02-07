import requests

SPOT_INFO = "https://api.binance.com/api/v3/exchangeInfo"

def get_spot_tokens():
    data = requests.get(SPOT_INFO, timeout=10).json()
    return {s["baseAsset"] for s in data["symbols"]}
