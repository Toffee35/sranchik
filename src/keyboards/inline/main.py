from aiogram.types import User
from aiogram.utils.deep_linking import create_start_link
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.main import bot


async def menu(user: User):
    bot_link: str = await create_start_link(bot, str(user.id))

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📤 Поделиться ссылкой", url=f"tg://msg_url?url={bot_link}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔎 Найти пользователя", callback_data="menu:search"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔥 Посмотреть топ", callback_data="menu:top:0"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗑 Фильтр по полу", callback_data="menu:filter"
                )
            ],
        ]
    )


profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Изменить имя", callback_data="profile:name"),
            InlineKeyboardButton(
                text="📸 Сменить аватар", callback_data="profile:avatar"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 Почистить от дерьма", callback_data="profile:clear"
            )
        ],
    ]
)


__all__ = [profile, menu]
