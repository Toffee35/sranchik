import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = sys.argv[1] if len(sys.argv) > 1 else getenv("BOT_TOKEN")

props = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=TOKEN, default=props)


def main():
    from .routes import routes

    dp = Dispatcher()
    dp.include_router(routes)

    dp.run_polling(bot)


__all__ = [main, bot]
