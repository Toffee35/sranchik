from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import reply
from src.states import Main, Menu

menu_filter = Router()
menu_filter.callback_query.filter(Menu.Filter)


@menu_filter.callback_query(F.data.regexp(r"^menu:filter:(none|(?:fe)?male)$"))
async def _menu_filter(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.delete()
    await message.answer(
        html.italic("Отлично! Фильтр настроен..."), reply_markup=reply.base
    )

    await callback.answer()


__all__ = [menu_filter]
