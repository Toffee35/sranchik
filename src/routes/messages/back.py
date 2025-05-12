from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards.reply import main
from src.states import Base

from .menu import get_menu

back = Router()


@back.message(Base.Judging, F.text == "Назад")
async def _back(message: Message, state: FSMContext):
    await message.answer(html.italic("Возврат в меню..."), reply_markup=main)

    await get_menu(message, state)


__all__ = [back]
