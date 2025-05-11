from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from src.functions.results import regist_repeat
from src.storages import users
from src.structs.states import BaseState

my_frends = Router()


@my_frends.callback_query(BaseState.base, F.data == "my_frends")
async def _my_frends(callback: CallbackQuery, message: Message):
    if user_data := users.get(callback.from_user.id):
        await message.answer(f"Твои друзья: {user_data.frends}")
    else:
        await regist_repeat(message)

    await callback.answer()


__all__ = [my_frends]
