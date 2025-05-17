from re import Match

from aiogram import F, Router, html
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards import reply
from src.states import Main, Regist

regist = Router()
regist.message.filter(StateFilter(Regist.Avatar, Regist.Name))


@regist.message(Regist.Avatar, F.photo[0].file_id)
async def _avatar(message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.answer(html.italic("Регистрация пройдена"), reply_markup=reply.base)


@regist.message(Regist.Name, F.text.regexp(r"^[^/](\S+)?$").as_("match"))
async def _regist_name(message: Message, match: Match, state: FSMContext):
    if match.group(1):
        await state.set_state(Regist.Gender)

        await message.answer("👽 Какого ты пола?", reply_markup=regist.name)
        return

    await message.answer("Имя не должно содержать пробелов")


__all__ = [regist]
