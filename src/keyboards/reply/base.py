from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup

base: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="📄 Меню"),
            KeyboardButton(text="🏅 Оценивать"),
        ]
    ],
)

__all__ = [base]
