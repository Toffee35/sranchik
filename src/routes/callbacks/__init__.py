from aiogram import F, Router
from aiogram.filters import StateFilter

from src.states import Regist

from .gender import gender
from .take_from_profile import take_from_profile

regist = Router()
regist.callback_query.filter(
    StateFilter(Regist.Name, Regist.Gender, Regist.Avatar),
    F.message.delete,
    F.message.as_("message"),
)

regist.include_routers(take_from_profile, gender)


callbacks = Router()
callbacks.include_routers(regist)

__all__ = [callbacks]
