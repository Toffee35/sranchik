from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.storages import users
from src.structs.keyboards import relpy
from src.structs.states import BaseState

assessment = Router()


@assessment.message(BaseState.base, F.text == "Оценка")
async def _assessment(message: Message, state: FSMContext):
    if not len(users) > 1:
        await message.answer(html.italic("0 пользователь для оценки"))
        return

    await state.set_state(BaseState.assessment)
    await message.answer(html.bold("Приступай к оценке"), reply_markup=relpy.assessment)


__all__ = [assessment]
