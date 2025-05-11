from re import Match
from typing import Optional

from aiogram import F, Router
from aiogram.types import Message, User

from src.storages import users

get = Router()


@get.message(F.text.regexp(r"^/get(?:\s(\d+))?$").as_("match"), F.from_user.as_("user"))
async def _get(message: Message, user: User, match: Match[Optional[str]]):
    if user_id := match.group(1):
        user_id: int = int(user_id if user_id != "0" else user.id)

        if user_data := users.get(user_id):
            await message.answer_photo(
                user_data.avatar, caption=f"{user_id}: {user_data}", parse_mode=None
            )
            return

        await message.answer(f"Пользователь {user_id} не найден")
        return

    await message.answer(f"Пользователи в базе: {list(users.keys())}")


__all__ = [get]
