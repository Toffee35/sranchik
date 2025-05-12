from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

judging_choise = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Поцелуй"),
            KeyboardButton(text="Назад"),
            KeyboardButton(text="Дерьмо"),
        ]
    ],
)

__all__ = [judging_choise]
