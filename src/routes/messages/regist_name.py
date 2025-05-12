from re import Match

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.states import Regist
from src.utils import setting_name

regist_name = Router()


@regist_name.message(Regist.Name, F.text.regexp(r"^[^/](\S+)?$").as_("match"))
async def _regist_name(message: Message, match: Match, state: FSMContext):
    if name := match.group(1):
        await setting_name(name, message, state)
        return

    await message.answer("Имя не должно содержать пробелов")


__all__ = [regist_name]
