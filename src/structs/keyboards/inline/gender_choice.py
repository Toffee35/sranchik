from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

gender_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мужской", callback_data="male_choice"),
            InlineKeyboardButton(text="Женский", callback_data="female_choice"),
        ]
    ]
)

__all__ = [gender_choice]
