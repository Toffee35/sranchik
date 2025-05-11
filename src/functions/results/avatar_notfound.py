from aiogram.types import Message


async def avatar_notfound(message: Message):
    await message.answer("Фотография не найдена")


__all__ = [avatar_notfound]
