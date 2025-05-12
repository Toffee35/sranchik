from aiogram import F, Router

from .check import check
from .make import make
from .start import start

commands = Router()
commands.message.filter(F.from_user.as_("user"), F.text.startswith("/"))
commands.include_routers(start, check, make)

__all__ = [commands]
