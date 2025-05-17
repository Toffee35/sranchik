from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards.inline import regist
from src.states import Regist

start = Router()


@start.message(F.text.regexp(r"^/start(?:\s(\d+))?$"))
async def _start(message: Message, state: FSMContext):
    await state.set_state(Regist.Name)

    await message.answer("📝 Назови свое имя", reply_markup=regist.name)


__all__ = [start]
