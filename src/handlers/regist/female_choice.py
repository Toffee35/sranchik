from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.storage import Gender

from . import RegistState

female_choice = Router()


@female_choice.callback_query(F.data == "female_choice")
async def _female_choice(callback: CallbackQuery, state: FSMContext):
    message = callback.message
    if not isinstance(message, Message):
        return

    name = await state.get_value("name")
    if not name:
        await message.delete()
        await message.answer("Пройдите регистрацию заново")
        return

    await state.update_data(gender=Gender.Female)
    await state.set_state(RegistState.avatar)

    await message.delete()
    await message.answer(
        "Отправь аватар",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Взять из профиля", callback_data="profile_avatar"
                    ),
                ]
            ]
        ),
    )

    await callback.answer()
