from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

profile_avatar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Взять из профиля", callback_data="profile_avatar"
            ),
        ]
    ]
)

__all__ = [profile_avatar]
