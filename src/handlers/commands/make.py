from re import Match
from typing import Optional

from aiogram import F, Router, html
from aiogram.types import Message

from src.storages import users

make = Router()


@make.message(
    F.text.regexp(r"^/make(?:\s(\S+))?(?:\s(\d+))?(?:\s(\S+))?$").as_("match")
)
async def _make(
    message: Message, match: Match[Optional[str], Optional[str], Optional[str]]
):
    group: Optional[str] = match.group(1)
    item: Optional[str] = match.group(2)
    value: Optional[str] = match.group(3)
    if not (group and item and value):
        await message.answer("Не верные аргументы")

    try:
        match group:
            case "k":
                users[int(item)].kisses = int(value)
            case "s":
                users[int(item)].shits = int(value)
            case "i":
                users[int(item)].invites = int(value)
            case _:
                raise ValueError("Не известный аргумент")
    except Exception as e:
        await message.answer(f"Ошибка {e.__class__.__name__}: {e}", parse_mode=None)
    else:
        await message.answer(html.italic("Готово."))


__all__ = [make]
