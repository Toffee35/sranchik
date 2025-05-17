from aiogram import Router
from aiogram.filters import StateFilter

from src.states import Main

from .menu import menu
from .profile import profile

main = Router()
main.callback_query.filter(StateFilter(Main.Menu, Main.Base, Main.Profile))
main.include_routers(profile, menu)

__all__ = [main]
