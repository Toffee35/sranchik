from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

ffilter: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💁‍♂️ Парня", callback_data="menu:filter:male"),
            InlineKeyboardButton(
                text="💁‍♀️ Девушку", callback_data="menu:filter:female"
            ),
        ],
        [InlineKeyboardButton(text="🤯 Кого угодно", callback_data="menu:filter:none")],
    ]
)


def scroll(page: int, limit: int) -> InlineKeyboardMarkup:
    keyboard = []

    if page > 0:
        keyboard.append(
            InlineKeyboardButton(text="⬅️", callback_data=f"menu:top:{page - 1}")
        )

    if page < limit:
        keyboard.append(
            InlineKeyboardButton(text="➡️", callback_data=f"menu:top:{page + 1}")
        )

    return InlineKeyboardMarkup(inline_keyboard=[keyboard])

__all__ = [ffilter, scroll]