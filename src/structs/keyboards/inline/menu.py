from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поиск", callback_data="search"),
            InlineKeyboardButton(text="VIP", callback_data="vip_info"),
            InlineKeyboardButton(text="Топ", callback_data="global_tops"),
        ]
    ]
)

__all__ = [menu]
