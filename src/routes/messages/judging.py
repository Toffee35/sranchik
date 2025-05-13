from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy import func, select

from src.database import UserData, users_session
from src.keyboards.reply import judging_choise
from src.states import Base

judging = Router()


@judging.message(F.text == "Оценка")
async def _judging(message: Message, state: FSMContext):
    async with users_session() as session:
        if users_count := await session.scalar(
            select(func.count()).select_from(UserData)
        ):
            if not users_count > 1:
                await message.answer(
                    html.italic("Пока что ты единственный кого можно оценить...")
                )
                return

    await state.set_state(Base.Judging)

    await message.answer("Погнали оценивать", reply_markup=judging_choise)


__all__ = [judging]
