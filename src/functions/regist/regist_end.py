from typing import List, Optional

from aiogram import html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize, User

from src.storages import users
from src.structs.keyboards import relpy
from src.structs.states import BaseState
from src.structs.user import Gender, UserData

from ..results import avatar_notfound, regist_repeat


async def regist_end(
    message: Message, user: User, state: FSMContext, photos: Optional[List[PhotoSize]]
):
    name: Optional[str] = await state.get_value("name")
    gender: Optional[Gender] = await state.get_value("gender")
    if not (name and gender):
        await regist_repeat(message)
        return

    if not photos:
        await avatar_notfound(message)
        return

    if len(photos) == 0:
        await avatar_notfound(message)
        return

    inviter = await state.get_value("inviter")
    if inviter in users:
        users[inviter].invites += 1
        users[inviter].frends.append(user.id)
    else:
        inviter = None

    users[user.id] = UserData(name, user.username, gender, photos[0].file_id, inviter)

    await state.clear()
    await state.set_state(BaseState.base)

    await message.answer(html.italic("Регистрация пройдена."), reply_markup=relpy.base)


__all__ = [regist_end]
