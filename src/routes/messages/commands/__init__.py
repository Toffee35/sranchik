from aiogram import F, Router

from .start import start

commands = Router()
commands.message.filter(F.text.startswith("/"))
commands.include_routers(start)

__all__ = [commands]
