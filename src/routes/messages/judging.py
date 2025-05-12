from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards.reply import judging_choise
from src.states import Base
from src.storages import users
judging = Router()


@judging.message(F.text == "Оценка")
async def _judging(message: Message, state: FSMContext):
    if not len(users) > 1:
        await message.answer(html.italic("Пока что ты единственный кого можно оценить..."))
        return

    await state.set_state(Base.Judging)

    await message.answer("Погнали оценивать", reply_markup=judging_choise)


__all__ = [judging]
