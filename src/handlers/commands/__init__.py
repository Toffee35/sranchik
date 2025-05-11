from aiogram import F, Router

from .get import get
from .make import make
from .start import start

commands = Router()
commands.message.filter(F.text.startswith("/"))
commands.include_routers(start, get, make)

__all__ = [commands]
