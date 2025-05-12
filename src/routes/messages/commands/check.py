from re import Match

from aiogram import F, Router
from aiogram.types import Message, User

from src.storages import users

check = Router()


@check.message(F.text.regexp(r"^/check(?:\s(\d+))?$").as_("match"))
async def _check(message: Message, user: User, match: Match):
    if user_id := match.group(1):
        user_id = int(user_id)

        if user_id == 0:
            user_id = user.id

        if user_data := users.get(user_id):
            await message.answer_photo(
                user_data.avatar, caption=f"{user_id}: {user_data}", parse_mode=None
            )
            return

        await message.answer("Пользователь не найден")
        return

    await message.answer(f"Пользователи в базе: {list(users.keys())}")


__all__ = [check]
