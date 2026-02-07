import requests

def get_market_cap(symbol):
    base = symbol.replace("USDT", "").lower()

    search = requests.get(
        "https://api.coingecko.com/api/v3/search",
        timeout=10
    ).json()

    for coin in search["coins"]:
        if coin["symbol"] == base:
            data = requests.get(
                f"https://api.coingecko.com/api/v3/coins/{coin['id']}",
                timeout=10
            ).json()
            return data["market_data"]["market_cap"]["usd"]

    return None
