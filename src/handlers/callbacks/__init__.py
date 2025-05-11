from aiogram import F, Router

from .gender_choice import gender_choice
from .my_frends import my_frends
from .profile_avatar import profile_avatar
from .profile_name import profile_name

regist = Router()
regist.callback_query.filter(F.message.delete)
regist.include_routers(gender_choice, profile_avatar, profile_name)

callbacks = Router()
callbacks.callback_query.filter(F.message.as_("message"))
callbacks.include_routers(regist, my_frends)

__all__ = [callbacks]
