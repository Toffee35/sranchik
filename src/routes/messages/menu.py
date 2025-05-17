from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards import reply
from src.states import Main, Menu

menu = Router()
menu.message.filter(Menu.Search)


@menu.message(F.text.regexp(r"^[^/](@)?(\S+)$"))
async def _search(message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.answer(
        f"""
📝 {html.bold("Имя:")}

💋 {html.bold("Поцелуев:")}
💩 {html.bold("Дерьма:")}
🏅 {html.bold("Место в топе:")}
""",
        reply_markup=reply.base,
    )


__all__ = [menu]
