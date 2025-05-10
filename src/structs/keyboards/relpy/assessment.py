from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup

assessment = ReplyKeyboardMarkup(
    is_persistent=True,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="💩"),
            KeyboardButton(text="Назад"),
            KeyboardButton(text="💋"),
        ]
    ],
)

__all__ = [assessment]
