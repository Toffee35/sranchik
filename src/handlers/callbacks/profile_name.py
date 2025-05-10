from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.functions.regist import gender_choice
from src.structs.states import RegistState

profile_name = Router()


@profile_name.callback_query(RegistState.name, F.data == "profile_name")
async def _profile_name(callback: CallbackQuery, state: FSMContext):
    message = callback.message
    if not isinstance(message, Message):
        return

    await message.delete()
    await gender_choice(message, state, callback.from_user.first_name)

    await callback.answer()


__all__ = [profile_name]
