from re import Match

from aiogram import F, Router
from aiogram.types import Message, User

from src.database import UserData, users_session

make = Router()


@make.message(F.text.regexp(r"^/make\s(\S)(\S)\s(\d+)\s(\S+)$").as_("match"))
async def _make(message: Message, user: User, match: Match):
    group = match.group(1)
    item = match.group(2)
    identifier = int(match.group(3))
    value = match.group(4)

    if identifier == 0:
        identifier = user.id

    async with users_session() as session:
        try:
            match group:
                case "u":
                    user_data = await session.get(UserData, identifier)

                    match item:
                        case "k":
                            user_data.kisses = int(value)
                        case "s":
                            user_data.shits = int(value)
                        case "i":
                            user_data.invites = int(value)
                        case _:
                            raise Exception("Не известный первый аргумент")
                case _:
                    raise Exception("Не известный первый аргумент")
        except Exception as e:
            await message.answer(f"Ошибка {e.__class__.__name__}: {e}")
        else:
            await session.commit()


__all__ = [make]
