from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.structs.keyboards import inline
from src.structs.states import RegistState
from src.structs.user import Gender

from ..results import regist_repeat


async def profile_avatar(callback: CallbackQuery, state: FSMContext, gender: Gender):
    message = callback.message
    if not isinstance(message, Message):
        return

    name = await state.get_value("name")
    if not name:
        await message.delete()
        await regist_repeat(message)
        return

    await state.update_data(gender=gender)
    await state.set_state(RegistState.avatar)

    await message.delete()
    await message.answer("Отправь аватар", reply_markup=inline.profile_avatar)

    await callback.answer()


__all__ = [profile_avatar]
