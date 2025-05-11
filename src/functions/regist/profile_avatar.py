from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.structs.keyboards import inline
from src.structs.states import RegistState
from src.structs.user import Gender

from ..results import regist_repeat


async def profile_avatar(
    callback: CallbackQuery, message: Message, state: FSMContext, gender: Gender
):
    await message.delete()

    if not await state.get_value("name"):
        await regist_repeat(message)
        return

    await state.update_data(gender=gender)
    await state.set_state(RegistState.avatar)

    await message.answer("Отправь аватар", reply_markup=inline.profile_avatar)
    await callback.answer()


__all__ = [profile_avatar]
