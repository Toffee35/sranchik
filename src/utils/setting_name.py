from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards.inline import gender_selection
from src.states import Regist


async def setting_name(name: str, message: Message, state: FSMContext):
    await state.update_data(name=name)
    await state.set_state(Regist.Gender)

    await message.answer("Какого вы пола", reply_markup=gender_selection)


__all__ = [setting_name]
