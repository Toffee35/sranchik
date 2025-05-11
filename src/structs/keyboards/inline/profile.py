from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Удалить меня", callback_data="delete_me"),
            InlineKeyboardButton(text="Друзья", callback_data="my_frends"),
            InlineKeyboardButton(text="Оценки", callback_data="assessment"),
        ]
    ]
)

__all__ = [profile]
