import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL

bot = Bot(token=TELEGRAM_BOT_TOKEN)


def send(text: str):
    asyncio.run(
        bot.send_message(
            chat_id=TELEGRAM_CHANNEL,
            text=text,
            parse_mode=ParseMode.MARKDOWN
        )
    )
