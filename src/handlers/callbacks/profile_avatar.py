from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.functions.regist import regist_end
from src.structs.states import RegistState

profile_avatar = Router()


@profile_avatar.callback_query(RegistState.avatar, F.data == "profile_avatar")
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
