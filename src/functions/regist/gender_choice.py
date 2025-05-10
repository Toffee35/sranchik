from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.states import RegistState


async def gender_choice(message: Message, state: FSMContext, name: str):
    await state.update_data(name=name)

    await state.set_state(RegistState.gender)
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


__all__ = [gender_choice]
