from aiogram import F, Router, html
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import reply
from src.states import Main, Menu, Profile

back_main = Router()
back_main.callback_query.filter(StateFilter(Menu.Search, Profile.Name, Profile.Avatar))


@back_main.callback_query(F.data == "back_main")
async def _back_main(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.delete()
    await message.answer(html.italic("Вы на главной"), reply_markup=reply.base)

    await callback.answer()


__all__ = [back_main]
