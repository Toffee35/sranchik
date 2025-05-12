from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup


def take_from_profile(item: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Взять из профиля", callback_data=f"take_from_profile:{item}"
                )
            ]
        ]
    )


__all__ = [take_from_profile]
