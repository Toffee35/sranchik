from re import Match
from typing import Optional

from aiogram import F, Router
from aiogram.types import Message

from src.storage import User, users

check = Router()


@check.message(F.text.regexp(r"^/check(?:\s(\d+))?").as_("match"))
async def _check(message: Message, match: Match):
    user_id: Optional[str] = match.group(1)

    if user_id:
        user_data: Optional[User] = users.get(int(user_id))

        if not user_data:
            await message.answer("Не найден")

        await message.answer_photo(
            user_data.avatar,
            caption=f"<b>Имя:</b> {user_data.name}\n<b>Пол:</b> {user_data.gender.value}",
        )
    else:
        await message.answer(f"{users}", parse_mode=None)
