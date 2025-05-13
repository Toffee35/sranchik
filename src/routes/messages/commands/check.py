from re import Match

from aiogram import F, Router
from aiogram.types import Message, User
from sqlalchemy import select

from src.database import UserData, users_session

check = Router()


@check.message(F.text.regexp(r"^/check(?:\s(\d+))?$").as_("match"))
async def _check(message: Message, user: User, match: Match):
    if user_id := match.group(1):
        user_id = int(user_id)

        if user_id == 0:
            user_id = user.id

        async with users_session() as session:
            if user_data := await session.get(UserData, user_id):
                await message.answer_photo(
                    str(user_data.avatar),
                    caption=f"{user_id}: {user_data}",
                    parse_mode=None,
                )
                return

        await message.answer("Пользователь не найден")
        return

    async with users_session() as session:
        users = await session.scalars(select(UserData.id))

        await message.answer(f"Пользователи в базе: {users.all()}")


__all__ = [check]
