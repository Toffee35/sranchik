from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

avatar: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📌 Взять из профиля",
                callback_data="regist:avatar",
            )
        ]
    ]
)

gender: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨️ Парня", callback_data="regist:gender:male"),
            InlineKeyboardButton(
                text="👩 Девушку", callback_data="regist:gender:female"
            ),
        ]
    ]
)

name: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📌 Взять из профиля",
                callback_data="regist:name",
            )
        ]
    ]
)

__all__ = [avatar, name]
