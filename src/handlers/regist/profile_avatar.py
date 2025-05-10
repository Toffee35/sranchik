from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.states import BaseState
from src.storage import User, users

profile_avatar = Router()


@profile_avatar.callback_query(F.data == "profile_avatar")
async def _profile_avatar(callback: CallbackQuery, state: FSMContext):
    user = callback.from_user

    message = callback.message
    if not isinstance(message, Message):
        return

    name = await state.get_value("name")
    gender = await state.get_value("gender")
    if not name or not gender:
        await message.delete()
        await message.answer("Пройдите регистрацию заново")
        return

    photos = await user.get_profile_photos(limit=1)
    if not photos.total_count > 0:
        await message.answer("Аватарка не обнаружена")
        return

    users[user.id] = User(name, gender, photos.photos[0][0].file_id)

    await state.clear()
    await state.set_state(BaseState.base)

    await message.delete()
    await message.answer("Регистрация пройдена")

    await callback.answer()
