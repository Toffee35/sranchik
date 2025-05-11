from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from src.functions.results import regist_repeat
from src.storages import users
from src.structs.keyboards import inline
from src.structs.states import BaseState

my_frends = Router()


@my_frends.callback_query(BaseState.base, F.data == "my_frends")
async def _my_frends(callback: CallbackQuery, message: Message):
    user = callback.from_user

    if user_data := users.get(user.id):
        if len(user_data.frends) == 0:
            inline_keyboard = await inline.add_frend(user)

            await message.answer(
                "Покачто никого в друзях нет...", reply_markup=inline_keyboard
            )
            return

        await message.answer(
            f"Твои друзья:\n{'\n'.join(f'@{users[user_id].mention}' for user_id in user_data.frends)}"
        )
    else:
        await regist_repeat(message)

    await callback.answer()


__all__ = [my_frends]
