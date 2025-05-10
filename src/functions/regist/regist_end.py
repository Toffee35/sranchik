from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize, User

from src.storages import users
from src.structs.states import BaseState
from src.structs.user import UserData


async def regist_end(
    message: Message, user: User, state: FSMContext, photos: list[PhotoSize]
):
    name = await state.get_value("name")
    gender = await state.get_value("gender")
    if not name or not gender:
        await message.answer("Пройдите регистрацию заново - /start")
        return

    if not len(photos) > 0:
        await message.answer("Фотография не найдена")
        return

    users[user.id] = UserData(name, gender, photos[0].file_id)

    await state.clear()
    await state.set_state(BaseState.base)

    await message.answer("Регистрация пройдена")


__all__ = [regist_end]
