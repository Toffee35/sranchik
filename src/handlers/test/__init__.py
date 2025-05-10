from aiogram import Router

from .chech import check

test = Router()
test.include_routers(check)