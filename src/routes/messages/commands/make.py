from re import Match

from aiogram import F, Router
from aiogram.types import Message, User

from src.storages import users

make = Router()


@make.message(F.text.regexp(r"^/make\s(\S)(\S)\s(\d+)\s(\S+)$").as_("match"))
async def _make(message: Message, user: User, match: Match):
    group = match.group(1)
    item = match.group(2)
    identifier = int(match.group(3))
    value = match.group(4)

    if identifier == 0:
        identifier = user.id

    try:
        match group:
            case "u":
                match item:
                    case "k":
                        users[identifier].kisses = int(value)
                    case "s":
                        users[identifier].shits = int(value)
                    case "i":
                        users[identifier].invites = int(value)
                    case _:
                        raise Exception("Не известный первый аргумент")
            case _:
                raise Exception("Не известный первый аргумент")
    except Exception as e:
        await message.answer(f"Ошибка {e.__class__.__name__}: {e}")


__all__ = [make]
