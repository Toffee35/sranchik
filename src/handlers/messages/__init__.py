from aiogram import F, Router

from .assessment import assessment
from .back import back
from .menu import menu
from .my_profile import my_profile
from .regist_avatar import regist_avatar
from .regist_name import regist_name

messages = Router()
messages.message.filter(~F.text.startswith("/"))
messages.include_routers(back, menu, my_profile, regist_avatar, regist_name, assessment)

__all__ = [messages]
