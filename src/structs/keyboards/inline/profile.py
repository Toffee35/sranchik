from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Друзья", callback_data="my_frends"),
            InlineKeyboardButton(text="Поиск", callback_data="search"),
            InlineKeyboardButton(text="Оценки", callback_data="assessment"),
        ]
    ]
)

__all__ = [profile]
