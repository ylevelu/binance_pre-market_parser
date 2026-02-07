import time
import json
from config import CHECK_INTERVAL
from services.binance_spot import get_spot_symbols
from services.binance_futures import get_premarket_usdtm_symbols
from tg.notifier import send

SEEN_FILE = "storage/seen.json"


def load_seen():
    try:
        with open(SEEN_FILE, "r") as f:
            return set(json.load(f))
    except Exception:
        return set()


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)


def main():
    send("*Bot started ✔️*")

    seen = load_seen()

    while True:
        try:
            spot = get_spot_symbols()
            premarket = get_premarket_usdtm_symbols(spot)

            for token in premarket:
                symbol = token["symbol"]
                if symbol in seen:
                    continue

                msg = (
                    f"*New Binance USDT-M Pre-Market*\n\n"
                    f"• Symbol: `{symbol}`\n"
                    f"• Price: `{token['price']}` USDT\n"
                    f"• 24h Volume: `{token['volume']:.2f}` USDT\n\n"
                    f"_Fresh futures contract, spot not listed yet_"
                )

                send(msg)
                seen.add(symbol)

            save_seen(seen)

        except Exception as e:
            print("MAIN LOOP ERROR:", e)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
