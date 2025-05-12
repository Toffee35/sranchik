from aiogram.types import Message


async def repeat_regist(message: Message):
    await message.answer("Повторите регистрацию - /start")


__all__ = [repeat_regist]
