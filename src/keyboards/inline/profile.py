from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from .back_button import back_button

avatar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📌 Взять из профиля",
                callback_data="profile:avatar",
            )
        ],
        back_button,
    ]
)

name = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📌 Взять из профиля",
                callback_data="profile:name",
            )
        ],
        back_button,
    ]
)

__all__ = [avatar, name]
