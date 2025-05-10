from aiogram import Router

from .regist import regist
from .test import test

handlers = Router()
handlers.include_routers(regist, test)
