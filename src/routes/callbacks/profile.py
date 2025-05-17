from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import reply
from src.states import Main, Profile

profile = Router()
profile.callback_query.filter(StateFilter(Profile.Name, Profile.Avatar))


@profile.callback_query(Profile.Avatar, F.data == "profile:avatar")
async def _avatar(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.delete()
    await message.answer("Аватарка установлена", reply_markup=reply.base)

    await callback.answer()


@profile.callback_query(Profile.Name, F.data == "profile:name")
async def _name(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.delete()
    await message.answer("Имя установлено", reply_markup=reply.base)

    await callback.answer()


__all__ = [profile]
