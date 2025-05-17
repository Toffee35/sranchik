from re import Match

from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import reply
from src.keyboards.inline import menu as menu_kb
from src.keyboards.inline.back_kb import back_kb
from src.states import Main, Menu

menu = Router()
menu.callback_query.filter(Main.Menu)


@menu.callback_query(F.data == "menu:filter")
async def _filter(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Menu.Filter)

    await message.delete()
    await message.answer(html.italic("Привереда..."), reply_markup=reply.remove)

    await message.answer("👽 Кого ты хочешь искать?", reply_markup=menu_kb.ffilter)
    await callback.answer()


@menu.callback_query(F.data == "menu:search")
async def _search(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Menu.Search)

    await message.delete()
    await message.answer(html.italic("Приступаю к поиску"), reply_markup=reply.remove)

    await message.answer(
        "Упомнините того чей профиль хотите просмотреть",
        reply_markup=back_kb,
    )
    await callback.answer()


@menu.callback_query(F.data.regexp(r"^menu:top:(\d+)$").as_("match"))
async def _top(callback: CallbackQuery, message: Message, match: Match):
    page = int(match.group(1))

    await message.delete()
    await message.answer(
        f"""
📝 {html.bold("Имя:")}

💋 {html.bold("Поцелуев:")}
💩 {html.bold("Дерьма:")}
""",
        reply_markup=menu_kb.scroll(page, 3),
    )

    await callback.answer()


__all__ = [menu]
