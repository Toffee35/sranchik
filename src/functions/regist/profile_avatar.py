from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.states import RegistState
from src.structs.user import Gender


async def profile_avatar(callback: CallbackQuery, state: FSMContext, gender: Gender):
    message = callback.message
    if not isinstance(message, Message):
        return

    name = await state.get_value("name")
    if not name:
        await message.delete()
        await message.answer("Пройдите регистрацию заново - /start")
        return

    await state.update_data(gender=gender)
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


__all__ = [profile_avatar]
