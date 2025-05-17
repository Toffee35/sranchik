from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup

judging: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="💋 Поцелуй"),
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="💩 Дерьмо"),
        ]
    ],
)

__all__ = [judging]
