from aiogram import Router

from .callbacks import callbacks
from .commands import commands
from .messages import messages

handlers = Router()
handlers.include_routers(callbacks, commands, messages)

__all__ = [handlers]
