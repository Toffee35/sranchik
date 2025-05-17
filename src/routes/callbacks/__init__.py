from aiogram import F, Router

from .back_main import back_main
from .main import main
from .menu_filter import menu_filter
from .profile import profile
from .regist import regist

callbacks = Router()
callbacks.callback_query.filter(F.message.delete, F.message.as_("message"))
callbacks.include_routers(
    regist,
    main,
    profile,
    back_main,
    menu_filter,
)

__all__ = [callbacks]
