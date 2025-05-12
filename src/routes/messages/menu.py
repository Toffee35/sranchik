from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.states import Base

menu = Router()


@menu.message(F.text == "Меню")
async def get_menu(message: Message, state: FSMContext):
    await state.set_state(Base.Main)

    await message.answer("Меню")


__all__ = [menu, get_menu]
