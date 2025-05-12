from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize, User

from src.states import Regist
from src.utils import setting_avatar

regist_avatar = Router()


@regist_avatar.message(Regist.Avatar, F.from_user.as_("user"), F.photo.as_("photo"))
async def _regist_avatar(
    message: Message, user: User, photo: list[PhotoSize], state: FSMContext
):
    await setting_avatar(photo, message, user, state)


__all__ = [regist_avatar]
