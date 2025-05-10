from re import Match

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.functions.regist import gender_choice
from src.structs.states import RegistState

regist_name = Router()


@regist_name.message(RegistState.name, F.text.regexp(r"(\S+)?").as_("match"))
async def _regist_name(message: Message, state: FSMContext, match: Match):
    name = match.group(1)

    if not name:
        await message.answer("Имя не должно содержать пробелов, табов")
        return

    await gender_choice(message, state, name)


__all__ = [regist_name]
