from aiogram import Router

from .callbacks import callbacks
from .messages import messages

routes = Router()
routes.include_routers(callbacks, messages)

__all__ = [routes]
