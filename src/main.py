from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from .database import create_tables
from .routes import routes


async def main(bot: Bot):
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(routes)

    await create_tables()

    await dp.start_polling(bot)


__all__ = [main]
