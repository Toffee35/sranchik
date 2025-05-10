from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

profile_name = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Имя из профиля", callback_data="profile_name")]
    ]
)

__all__ = [profile_name]
