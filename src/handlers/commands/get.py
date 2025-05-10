from re import Match
from typing import Optional

from aiogram import F, Router
from aiogram.types import Message

from src.storages import users
from src.structs.user import UserData

get = Router()


@get.message(F.text.regexp(r"/get(?:\s(\d+))?$").as_("match"))
async def _get(message: Message, match: Match[Optional[str]]):
    user_id: Optional[str] = match.group(1)

    if not user_id:
        await message.answer(f"Пользователи в базе: {list(users.keys())}")
        return

    user_data: Optional[UserData] = users.get(int(user_id))

    if not user_data:
        await message.answer(f"Пользователь {user_id} не найден")
        return

    await message.answer_photo(
        user_data.avatar,
        caption=f"<b>Имя:</b> {user_data.name}\n<b>Пол:</b> {user_data.gender.value}",
    )


__all__ = [get]
