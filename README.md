# Binance USDT-M Futures Pre-Market Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Overview

This bot monitors **USDT-M Futures on Binance** that are **available for trading but not yet listed on the spot market**. These tokens are often called **pre-market tokens**, and they can be highly relevant for hype projects, upcoming tokenomics announcements, TGE events, and airdrops.

The bot automatically sends notifications to a **Telegram channel** with detailed information about each new pre-market token.

---

## 📝 Features

- Tracks **USDT-M Futures contracts** that are **not listed on Binance Spot**  
- Sends **Telegram notifications** for newly appearing pre-market tokens  
- Provides the following information:  
  - Token name and symbol  
  - Initial trading price  
  - 24h trading volume  
  - Market capitalization (via CoinGecko)  
  - Spot listing status  
  - TGE / Tokenomics pending warning  
- Automatically sends a **startup message** to the channel:  
Bot started ✔️


---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/ylevelu/binance_pre-market_parser.git
cd binance_pre-market_parser
Create a virtual environment (recommended):

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Configure config.py:

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHANNEL = "@your_channel_username_or_ID"
CHECK_INTERVAL = 60  # check interval in seconds
Add your bot to the Telegram channel and make it an administrator (permission to send messages is required).

▶️ Usage
Run the bot:

python main.py
The bot will start and continuously monitor Binance USDT-M pre-market futures, sending notifications for new tokens directly to your Telegram channel.

📂 Project Structure
binance_usdt_futures_premarket_bot/
│
├── main.py                # Main script
├── config.py              # Configuration file
├── requirements.txt       # Dependencies
│
├── services/              # API handlers
│   ├── binance_futures.py
│   ├── binance_spot.py
│   └── coingecko.py
│
├── tg/                    # Telegram notifier
│   └── notifier.py
│
└── storage/
    └── seen.json          # List of already notified tokens

```
## ⚠️ Notes
Works only with USDT-M Futures

Tracks tokens not yet listed on Spot

Pre-market period: any, market capitalization: any

Can be extended with:

WebSocket for real-time monitoring

Filters by volume or market cap

Integration with Discord

Docker deployment

Advanced logging

