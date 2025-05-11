from aiogram.types import User
from aiogram.utils.deep_linking import create_start_link
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from src.main import bot


async def add_frend(user: User):
    bot_link = await create_start_link(bot, payload=str(user.id))
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Пригласить нового", url=f"tg://msg_url?url={bot_link}"
                ),
                InlineKeyboardButton(
                    text="Отправить запрос", callback_data=f"frend_req:{user.id}"
                ),
            ]
        ]
    )
