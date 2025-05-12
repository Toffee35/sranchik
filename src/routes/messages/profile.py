from aiogram import F, Router, html
from aiogram.types import Message, User

from src.storages import users
from src.types import Gender
from src.utils import repeat_regist

profile = Router()


@profile.message(F.from_user.as_("user"), F.text == "Профиль")
async def _profile(message: Message, user: User):
    if user_data := users.get(user.id):
        await message.answer_photo(
            user_data.avatar,
            caption=f"""
{html.bold("Имя:")} {user_data.name}
{html.bold("Пол:")} {"Мужской" if user_data.gender == Gender.Male else "Женский"}

{html.bold("Поцелуи:")} {user_data.kisses}
{html.bold("Дерьмо:")} {user_data.shits}

{html.bold("Статус:")} {"Базовый" if user_data.invites < 3 else "VIP"}
""",
        )
        return

    await repeat_regist(message)


__all__ = [profile]
