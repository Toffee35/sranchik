import asyncio
import sys
from os import getenv

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from src.main import main

load_dotenv()
TOKEN = sys.argv[1] if len(sys.argv) > 1 else getenv("BOT_TOKEN")

props = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=TOKEN, default=props)

if __name__ == "__main__":
    asyncio.run(main(bot))

__all__ = [bot]
