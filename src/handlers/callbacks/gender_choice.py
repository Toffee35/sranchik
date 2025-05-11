from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.functions.regist import profile_avatar
from src.structs.states import RegistState
from src.structs.user import Gender

gender_choice = Router()
gender_choice.callback_query.filter(RegistState.gender)


@gender_choice.callback_query(F.data == "female_choice")
async def _female_choice(callback: CallbackQuery, message: Message, state: FSMContext):
    await profile_avatar(callback, message, state, Gender.Female)


@gender_choice.callback_query(F.data == "male_choice")
async def _male_choice(callback: CallbackQuery, message: Message, state: FSMContext):
    await profile_avatar(callback, message, state, Gender.Male)


__all__ = [gender_choice]
