from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize, User

from src.states import Regist
from src.utils import setting_avatar

regist_avatar = Router()


@regist_avatar.message(
    Regist.Avatar,
    F.from_user.as_("user"),
    F.from_user.username.as_("username"),
    F.photo.as_("photo"),
)
async def _regist_avatar(
    message: Message,
    user: User,
    photo: list[PhotoSize],
    state: FSMContext,
    username: str,
):
    await setting_avatar(photo, message, user, state, username)


__all__ = [regist_avatar]
