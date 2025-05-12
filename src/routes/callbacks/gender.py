from re import Match

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards.inline import take_from_profile
from src.states import Regist
from src.types import Gender
from src.utils import repeat_regist

gender = Router()


@gender.callback_query(
    Regist.Gender,
    F.data.regexp(r"^gender:((?:fe)?male)$").as_("match"),
)
async def _gender(
    callback: CallbackQuery, message: Message, match: Match, state: FSMContext
):
    user_gender: str = match.group(1)

    await message.delete()

    name = await state.get_value("name")
    if not name:
        await repeat_regist(message)
        return

    await state.update_data(
        gender=Gender.Male if user_gender == "male" else Gender.Female
    )
    await state.set_state(Regist.Avatar)

    await message.answer("Оправь свое фото", reply_markup=take_from_profile("avatar"))

    await callback.answer()


__all__ = [gender]
