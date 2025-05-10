from re import Match

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.functions.regist import gender_choice
from src.states import RegistState

profile_name = Router()


@profile_name.message(RegistState.name, F.text.regexp(r"(\S+$)?").as_("match"))
async def _name_message(message: Message, state: FSMContext, match: Match):
    await gender_choice(message, state, match.group(1))


@profile_name.callback_query(F.data == "profile_name")
async def _profile_name(callback: CallbackQuery, state: FSMContext):
    message = callback.message
    if not isinstance(message, Message):
        return

    await message.delete()
    await gender_choice(message, state, callback.from_user.first_name)

    await callback.answer()


__all__ = [profile_name]
