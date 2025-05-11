from aiogram import F, Router

from src.structs.states import BaseState

from .assessment import assessment
from .back import back
from .menu import menu
from .my_profile import my_profile
from .regist_avatar import regist_avatar
from .regist_name import regist_name

base = Router()
base.message.filter(~F.text.startswith("/"), BaseState.base)
base.include_routers(menu, my_profile, assessment)

messages = Router()
messages.message.filter(~F.text.startswith("/"))
messages.include_routers(base, back, regist_avatar, regist_name)

__all__ = [messages]
