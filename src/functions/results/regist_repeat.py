from aiogram.types import Message


async def regist_repeat(message: Message):
    await message.answer("Пройдите регистрацию заново - /start")


__all__ = [regist_repeat]
