from aiogram import Router

from .check import check

test = Router()
test.include_routers(check)

__all__ = [test]
