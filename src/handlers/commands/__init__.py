from aiogram import F, Router

from src.storages import settings

from .get import get
from .make import make
from .start import start

admin = Router()
admin.message.filter(F.from_user.id.in_(settings.admins))
admin.include_routers(get, make)

commands = Router()
commands.message.filter(F.text.startswith("/"))
commands.include_routers(start, admin)

__all__ = [commands]
