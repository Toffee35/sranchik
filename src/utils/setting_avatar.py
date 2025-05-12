from typing import List, Optional

from aiogram import html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize, User

from src.keyboards.reply import main
from src.routes.messages.menu import get_menu
from src.storages import users
from src.types import Gender, UserData
from src.utils import repeat_regist


async def setting_avatar(
    photo: List[PhotoSize], message: Message, user: User, state: FSMContext
):
    name: Optional[str] = await state.get_value("name")
    gender: Optional[Gender] = await state.get_value("gender")
    if not (name and gender):
        await repeat_regist(message)
        return

    if not len(photo) > 0:
        await message.answer("Фотография не найдена")
        return

    users[user.id] = UserData(name, gender, photo[0].file_id)

    if invite_id := await state.get_value("invite_id"):
        if (inviter := int(invite_id)) in users:
            users[inviter].invites += 1

    await message.answer(html.italic("Регистрация пройдена"), reply_markup=main)

    await get_menu(message, state)


__all__ = [setting_avatar]
