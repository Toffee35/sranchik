import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

_TOKEN = sys.argv[1] if len(sys.argv) > 1 else getenv("BOT_TOKEN")

params = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=_TOKEN, default=params)


def main():
    from .handlers import handlers

    dp = Dispatcher()
    dp.include_router(handlers)

    dp.run_polling(bot)


__all__ = [main, bot]
