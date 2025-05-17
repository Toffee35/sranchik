from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Main

from .base_menu_profile import base_menu_profile
from .judging import judging

main = Router()
main.message.filter(StateFilter(Main.Base, Main.Profile, Main.Judging, Main.Menu))
main.include_routers(base_menu_profile, judging)