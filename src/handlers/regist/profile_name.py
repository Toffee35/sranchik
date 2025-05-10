from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from . import RegistState

profile_name = Router()

@profile_name.callback_query(F.data == "profile_name")
async def _profile_name(callback: CallbackQuery, state: FSMContext):
    message = callback.message
    if not isinstance(message, Message):
        return

    await state.update_data(name=callback.from_user.first_name)
    await state.set_state(RegistState.gender)

    await message.delete()
    await message.answer(
        "Укажи свой пол",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Мужской", callback_data="male_choice"),
                    InlineKeyboardButton(text="Женский", callback_data="female_choice"),
                ]
            ]
        ),
    )

    await callback.answer()