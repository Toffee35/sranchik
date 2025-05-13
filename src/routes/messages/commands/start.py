from re import Match

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, User

from src.database import UserData, users_session
from src.keyboards.inline import take_from_profile
from src.routes.messages.menu import get_menu
from src.states import Regist

start = Router()


@start.message(F.text.regexp(r"^/start(?:\s(\d+))?$").as_("match"))
async def _start(message: Message, user: User, match: Match, state: FSMContext):
    async with users_session() as session:
        if await session.get(UserData, user.id):
            await get_menu(message, state)
            return

    await state.clear()

    await state.update_data(invite_id=match.group(1))
    await state.set_state(Regist.Name)

    await message.answer("Назови свое имя", reply_markup=take_from_profile("name"))


__all__ = [start]
