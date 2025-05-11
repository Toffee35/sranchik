from re import Match

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, User

from src.storages import users
from src.structs.keyboards import inline
from src.structs.states import RegistState

start = Router()


@start.message(
    F.text.regexp(r"^/start(?:\s(\d+))?$").as_("match"), F.from_user.as_("user")
)
async def _start(message: Message, user: User, state: FSMContext, match: Match):
    users.pop(user.id, None)
    await state.clear()

    if invite_id := match.group(1):
        if int(invite_id) != user.id:
            await state.update_data(inviter=int(invite_id))

    await state.set_state(RegistState.name)
    await message.answer("Назови свое имя", reply_markup=inline.profile_name)


__all__ = [start]
