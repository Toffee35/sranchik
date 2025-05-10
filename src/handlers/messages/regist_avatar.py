from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.functions.regist import regist_end
from src.structs.states import RegistState

regist_avatar = Router()


@regist_avatar.message(RegistState.avatar)
async def _regist_avatar(message: Message, state: FSMContext):
    print(message.text)
    user = message.from_user
    if not user:
        return

    await regist_end(message, user, state, message.photo)


__all__ = [regist_avatar]
