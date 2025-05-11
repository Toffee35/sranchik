from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.functions.regist import regist_end
from src.structs.states import RegistState

profile_avatar = Router()


@profile_avatar.callback_query(RegistState.avatar, F.data == "profile_avatar")
async def _profile_avatar(callback: CallbackQuery, message: Message, state: FSMContext):
    user = callback.from_user

    photos = (await user.get_profile_photos(limit=1)).photos

    await message.delete()
    await regist_end(message, user, state, photos[0] if len(photos) != 0 else None)
    await callback.answer()


__all__ = [profile_avatar]
