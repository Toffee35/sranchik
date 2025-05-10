from aiogram import F, Router, html
from aiogram.types import Message

from src.structs.keyboards import inline
from src.structs.states import BaseState

menu = Router()


@menu.message(BaseState.base, F.text == "Меню")
async def _menu(message: Message):
    await message.answer(html.bold("Меню"), reply_markup=inline.menu)


__all__ = [menu]
