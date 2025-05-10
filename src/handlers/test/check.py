from re import Match
from typing import Optional

from aiogram import F, Router
from aiogram.types import Message

from src.storages import users
from src.structs.user import UserData

check = Router()


@check.message(F.text.regexp(r"^/check\s?(\d+)?$").as_("match"))
async def _check(message: Message, match: Match):
    user_id: Optional[str] = match.group(1)

    if not user_id:
        await message.answer(f"Пользователи в базе: {list(users.keys())}")
        return

    user_data: Optional[UserData] = users.get(int(user_id))

    if not user_data:
        await message.answer("Пользователь не найден")
        return

    await message.answer_photo(
        user_data.avatar,
        caption=f"<b>Имя:</b> {user_data.name}\n<b>Пол:</b> {user_data.gender.value}",
    )


__all__ = [check]
