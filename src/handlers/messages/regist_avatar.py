from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, User

from src.functions.regist import regist_end
from src.structs.states import RegistState

regist_avatar = Router()


@regist_avatar.message(
    RegistState.avatar, F.from_user.username, F.from_user.as_("user")
)
async def _regist_avatar(message: Message, user: User, state: FSMContext):
    await regist_end(message, user, state, message.photo)


__all__ = [regist_avatar]
