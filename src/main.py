from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from .routes import routes


def main(bot: Bot):
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(routes)

    dp.run_polling(bot)


__all__ = [main]
