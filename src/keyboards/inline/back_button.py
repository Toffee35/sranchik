from typing import List

from aiogram.utils.keyboard import InlineKeyboardButton

back_button: List[InlineKeyboardButton] = [
    InlineKeyboardButton(text="❌ Обратно на главную", callback_data="back_main")
]

__all__ = [back_button]
