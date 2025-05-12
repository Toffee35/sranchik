from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Оценка"),
        ]
    ],
)

__all__ = [main]
