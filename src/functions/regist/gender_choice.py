from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.structs.keyboards import inline
from src.structs.states import RegistState


async def gender_choice(message: Message, state: FSMContext, name: str):
    await state.update_data(name=name)

    await state.set_state(RegistState.gender)
    await message.answer(
        "Укажи свой пол",
        reply_markup=inline.gender_choice,
    )


__all__ = [gender_choice]
