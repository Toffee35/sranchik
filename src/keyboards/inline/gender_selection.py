from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

gender_selection: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мужского", callback_data="gender:male"),
            InlineKeyboardButton(text="Женского", callback_data="gender:female"),
        ]
    ]
)


__all__ = [gender_selection]
