from aiogram import F, Router

from .get import get
from .start import start

commands = Router()
commands.message.filter(F.text.startswith("/"))
commands.include_routers(start, get)

__all__ = [commands]
