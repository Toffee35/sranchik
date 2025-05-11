from aiogram import F, Router
from aiogram.types import Message

from src.functions.base import get_menu
from src.structs.states import BaseState

menu = Router()


@menu.message(BaseState.base, F.text == "Меню")
async def _menu(message: Message):
    await get_menu(message)


__all__ = [menu]
