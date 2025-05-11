from aiogram import F, Router, html
from aiogram.types import Message, User

from src.functions.results import regist_repeat
from src.storages import users
from src.structs.keyboards import inline
from src.structs.states import BaseState

my_profile = Router()


@my_profile.message(BaseState.base, F.from_user.as_("user"), F.text == "Мой профиль")
async def _my_profile(message: Message, user: User):
    if user_data := users.get(user.id):
        await message.answer_photo(
            user_data.avatar,
            caption=f"""
{html.bold("Имя:")} {user_data.name}
{html.bold("Пол:")} {user_data.gender.value}
{html.bold("Поцелуев:")} {user_data.kisses}
{html.bold("Дерьма:")} {user_data.shits}
{html.bold("Статус:")} {"VIP" if user_data.invites > 5 else "Базовый"}
""",
            reply_markup=inline.profile,
        )
        return

    await regist_repeat(message)


__all__ = [my_profile]
