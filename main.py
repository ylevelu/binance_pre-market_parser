import time
import json
from services.binance_futures import get_usdt_futures, get_futures_ticker
from services.binance_spot import get_spot_tokens
from services.coingecko import get_market_cap
from tg.notifier import send
from config import CHECK_INTERVAL

send("Бот запущен ✔️")

with open("storage/seen.json") as f:
    seen = set(json.load(f)["tokens"])

while True:
    try:
        futures = get_usdt_futures()
        tickers = get_futures_ticker()
        spot_tokens = get_spot_tokens()

        for f in futures:
            symbol = f["symbol"]
            base = f["baseAsset"]

            # ❌ если уже есть спот — пропускаем
            if base in spot_tokens:
                continue

            # ❌ если уже отправляли
            if symbol in seen:
                continue

            t = tickers.get(symbol)
            if not t:
                continue

            price = t["lastPrice"]
            volume = t["quoteVolume"]
            cap = get_market_cap(symbol)

            message = (
                "*BINANCE FUTURES PRE-MARKET*\n\n"
                f"Token: `{base}`\n"
                f"Ticker: `{symbol}`\n"
                f"Price: `{price}`\n"
                f"24h Volume: `${volume}`\n"
                f"Market Cap: `{cap}`\n\n"
                "Spot listing: *NOT YET*\n"
                "TGE / Tokenomics pending"
            )

            send(message)

            seen.add(symbol)
            with open("storage/seen.json", "w") as f:
                json.dump({"tokens": list(seen)}, f)

        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(10)
