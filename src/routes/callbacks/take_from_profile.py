from re import Match

from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, UserProfilePhotos

from src.states import Regist
from src.utils import setting_avatar, setting_name

take_from_profile = Router()


@take_from_profile.callback_query(
    StateFilter(Regist.Name, Regist.Avatar),
    F.data.regexp(r"^take_from_profile:(name|avatar)$").as_("match"),
)
async def _take_from_profile(
    callback: CallbackQuery, message: Message, match: Match, state: FSMContext
):
    item: str = match.group(1)

    await message.delete()

    user = callback.from_user

    match item:
        case "name":
            await setting_name(user.first_name, message, state)
        case "avatar":
            photos: UserProfilePhotos = await user.get_profile_photos(limit=1)

            await setting_avatar(photos.photos[0], message, user, state)
        case _:
            return

    await callback.answer()


__all__ = [take_from_profile]
