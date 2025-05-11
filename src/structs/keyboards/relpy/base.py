from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup

base = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Мой профиль"),
            KeyboardButton(text="Оценка"),
            KeyboardButton(text="Меню"),
        ]
    ],
)

__all__ = [base]
