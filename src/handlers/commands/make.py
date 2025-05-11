from re import Match
from typing import Optional

from aiogram import F, Router, html
from aiogram.types import Message

from src.storages import users

make = Router()


@make.message(F.text.regexp(r"^/make\s(\S)(\S)(?:\s(\d+))?(?:\s(\S+))?$").as_("match"))
async def _make(message: Message, match: Match):
    group: Optional[str] = match.group(1)
    item: Optional[str] = match.group(2)
    integer: Optional[str] = match.group(3)
    string: Optional[str] = match.group(4)

    try:
        match group:
            case "u":  # изменение юзера
                match item:
                    case "k":  # а именно поцелуи
                        users[int(integer)].kisses = int(string)
                    case "s":  # а именно дерьмо
                        users[int(integer)].shits = int(string)
                    case "i":  # а именно инвайты
                        users[int(integer)].invites = int(string)
                    case _:
                        raise ValueError("Не известный предмет")
            case _:
                raise ValueError("Не известная группа")
    except Exception as e:
        await message.answer(f"Ошибка {e.__class__.__name__}: {e}", parse_mode=None)
    else:
        await message.answer(html.italic("Готово."))


__all__ = [make]
