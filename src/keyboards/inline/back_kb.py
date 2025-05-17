from aiogram.utils.keyboard import InlineKeyboardMarkup

from .back_button import back_button

back_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[back_button])

__all__ = [back_kb]
