from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.structs.keyboards import relpy
from src.structs.states import BaseState

back = Router()


@back.message(BaseState.assessment, F.text == "Назад")
async def _back(message: Message, state: FSMContext):
    await state.set_state(BaseState.base)

    await message.answer(html.bold("Моя статистика"), reply_markup=relpy.base)


__all__ = [back]
