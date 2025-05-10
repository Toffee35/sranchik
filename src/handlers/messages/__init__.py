from aiogram import F, Router

from .regist_avatar import regist_avatar
from .regist_name import regist_name

messages = Router()
messages.message.filter(~F.text.startswith("/"))
messages.include_routers(regist_avatar, regist_name)

__all__ = [messages]
