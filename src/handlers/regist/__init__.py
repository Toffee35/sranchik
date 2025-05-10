from aiogram import Router

from src.states import RegistState

__all__ = ["RegistState"]

from .female_choice import female_choice
from .male_choice import male_choice
from .profile_avatar import profile_avatar
from .profile_name import profile_name
from .start import start

regist = Router()
regist.include_routers(female_choice, male_choice, profile_avatar, profile_name, start)
