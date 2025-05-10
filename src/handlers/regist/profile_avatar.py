from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.functions.regist import regist_end
from src.states import RegistState

profile_avatar = Router()


@profile_avatar.message(RegistState.avatar)
async def _avatar_message(message: Message, state: FSMContext):
    user = message.from_user
    if not user:
        return

    await regist_end(message, user, state, message.photo)


@profile_avatar.callback_query(F.data == "profile_avatar")
async def _profile_avatar(callback: CallbackQuery, state: FSMContext):
    user = callback.from_user

    message = callback.message
    if not isinstance(message, Message):
        return

    photos = await user.get_profile_photos(limit=1)

    await message.delete()
    await regist_end(message, user, state, photos.photos[0])

    await callback.answer()


__all__ = [profile_avatar]
