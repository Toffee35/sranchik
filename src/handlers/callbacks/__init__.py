from aiogram import Router

from .gender_choice import gender_choice
from .profile_avatar import profile_avatar
from .profile_name import profile_name

callbacks = Router()
callbacks.include_routers(gender_choice, profile_avatar, profile_name)

__all__ = [callbacks]
