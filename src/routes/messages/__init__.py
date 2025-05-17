from aiogram import Router

from .commands import commands
from .main import main
from .menu import menu
from .profile import profile
from .regist import regist

messages = Router()
messages.include_routers(
    main,
    regist,
    commands,
    profile,
    menu,
)


__all__ = [messages]
