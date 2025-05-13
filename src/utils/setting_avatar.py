from typing import List, Optional

from aiogram import html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize, User

from src.database import Gender, UserData, users_session
from src.keyboards.reply import main
from src.routes.messages.menu import get_menu
from src.utils import repeat_regist


async def setting_avatar(
    photo: List[PhotoSize],
    message: Message,
    user: User,
    state: FSMContext,
    username: str,
):
    name: Optional[str] = await state.get_value("name")
    gender: Optional[Gender] = await state.get_value("gender")
    if not (name and gender):
        await repeat_regist(message)
        return

    if not len(photo) > 0:
        await message.answer("Фотография не найдена")
        return

    async with users_session() as session:
        session.add(
            UserData(
                id=user.id,
                name=name,
                mention=username,
                gender=gender,
                avatar=photo[0].file_id,
            )
        )

        if invite_id := await state.get_value("invite_id"):
            if inviter := await session.get(UserData, invite_id):
                inviter.invites += 1

        await session.commit()

    await message.answer(html.italic("Регистрация пройдена"), reply_markup=main)

    await get_menu(message, state)


__all__ = [setting_avatar]
