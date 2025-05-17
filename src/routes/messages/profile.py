from re import Match

from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards import reply
from src.states import Main, Profile

profile = Router()
profile.message.filter(StateFilter(Profile.Avatar, Profile.Name))


@profile.message(Profile.Avatar, F.photo[0].file_id)
async def _avatar(message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.answer("Аватарка установлена", reply_markup=reply.base)

@profile.message(Profile.Name, F.text.regexp(r"^[^/](\S+)?$").as_("match"))
async def _update_name(message: Message, match: Match, state: FSMContext):
    if match.group(1):
        await state.set_state(Main.Base)

        await message.answer("Имя установлено", reply_markup=reply.base)
        return

    await message.answer("Имя не должно содержать пробелов")

__all__ = [profile]
