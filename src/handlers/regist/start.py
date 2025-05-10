from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.storage.users import users

from . import RegistState

start = Router()


@start.message(CommandStart())
async def _start(message: Message, state: FSMContext):
    user = message.from_user

    if not user:
        return

    users.pop(user.id, None)

    await state.set_state(RegistState.name)

    await message.answer(
        "Назови свое имя",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Имя из профиля", callback_data="profile_name"
                    )
                ]
            ]
        ),
    )
