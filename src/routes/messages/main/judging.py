from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards import reply
from src.states import Main

judging = Router()
judging.message.filter(Main.Judging)


@judging.message(F.text == "🔙 Назад")
async def _back(message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.answer(html.italic("Вы на главной"), reply_markup=reply.base)


@judging.message(F.text == "💋 Поцелуй")
async def _kiss(message: Message):
    await message.answer("😘 Поцелуй (имя пользователя) либо закидай дерьмом")


@judging.message(
    ~F.text.startswith("/"),
    F.text != "💋 Поцелуй",
    F.text != "🔙 Назад",
    F.text != "💩 Дерьмо",
)
async def _message(message: Message):
    await message.answer("😘 Поцелуй (имя пользователя) либо закидай дерьмом")


@judging.message(F.text == "💩 Дерьмо")
async def _shit(message: Message):
    await message.answer("😘 Поцелуй (имя пользователя) либо закидай дерьмом")


__all__ = [judging]
