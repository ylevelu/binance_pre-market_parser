import requests

FUTURES_INFO = "https://fapi.binance.com/fapi/v1/exchangeInfo"
FUTURES_TICKER = "https://fapi.binance.com/fapi/v1/ticker/24hr"

def get_usdt_futures():
    data = requests.get(FUTURES_INFO, timeout=10).json()
    return [
        s for s in data["symbols"]
        if s["quoteAsset"] == "USDT" and s["contractStatus"] == "TRADING"
    ]

def get_futures_ticker():
    data = requests.get(FUTURES_TICKER, timeout=10).json()
    return {i["symbol"]: i for i in data}
