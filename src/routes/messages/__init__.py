from aiogram import F, Router
from aiogram.enums import ChatType
from aiogram.filters import StateFilter

from src.states import Base, Regist

from .back import back
from .commands import commands
from .judging import judging
from .menu import menu
from .profile import profile
from .regist_avatar import regist_avatar
from .regist_name import regist_name

regist = Router()
regist.message.filter(StateFilter(Regist.Name, Regist.Avatar))
regist.include_routers(regist_name, regist_avatar)


base = Router()
base.message.filter(Base.Main)
base.include_routers(judging, menu, profile)


messages = Router()
messages.message.filter(F.chat.type == ChatType.PRIVATE)

messages.include_router(commands)
messages.include_routers(regist, base, back)


__all__ = [messages]
