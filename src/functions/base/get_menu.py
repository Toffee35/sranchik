from aiogram import html
from aiogram.types import Message

from src.structs.keyboards import inline


async def get_menu(message: Message):
    await message.answer(html.bold("Меню"), reply_markup=inline.menu)
