import time
import requests
from config import PREMARKET_MAX_AGE_HOURS

FUTURES_INFO = "https://fapi.binance.com/fapi/v1/exchangeInfo"
FUTURES_TICKER = "https://fapi.binance.com/fapi/v1/ticker/24hr"


def get_usdtm_futures():
    r = requests.get(FUTURES_INFO, timeout=10)
    r.raise_for_status()
    return r.json().get("symbols", [])


def get_24h_tickers():
    r = requests.get(FUTURES_TICKER, timeout=10)
    r.raise_for_status()
    return r.json()


def get_premarket_usdtm_symbols(spot_symbols: set):
    futures = get_usdtm_futures()
    tickers = get_24h_tickers()
    ticker_map = {t["symbol"]: t for t in tickers}

    now = int(time.time())
    max_age = PREMARKET_MAX_AGE_HOURS * 3600

    result = []

    for item in futures:
        symbol = item.get("symbol")

        if not symbol or not symbol.endswith("USDT"):
            continue

        if item.get("contractType") != "PERPETUAL":
            continue

        # ❌ synthetic / index
        if symbol.startswith(("1000", "BTCDOM")):
            continue

        # ❌ уже есть на споте
        if symbol in spot_symbols:
            continue

        onboard_ms = item.get("onboardDate")
        if not onboard_ms:
            continue

        onboard_sec = onboard_ms // 1000

        # ❌ старый контракт
        if now - onboard_sec > max_age:
            continue

        ticker = ticker_map.get(symbol)
        if not ticker:
            continue

        result.append({
            "symbol": symbol,
            "price": float(ticker.get("lastPrice", 0)),
            "volume": float(ticker.get("quoteVolume", 0)),
            "onboard": onboard_sec
        })

    return result
