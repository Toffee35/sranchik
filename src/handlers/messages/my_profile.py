from aiogram import F, Router, html
from aiogram.types import Message

from src.structs.keyboards import inline
from src.structs.states import BaseState

my_profile = Router()


@my_profile.message(BaseState.base, F.text == "Мой профиль")
async def _my_profile(message: Message):
    await message.answer(
        f"{html.bold('Имя:')}\n{html.bold('Пол:')}\n{html.bold('Говна:')}\n{html.bold('Поцелуев:')}\n{html.bold('Статус:')}",
        reply_markup=inline.profile,
    )


__all__ = [my_profile]
