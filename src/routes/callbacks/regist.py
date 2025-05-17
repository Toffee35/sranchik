from aiogram import F, Router, html
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import reply
from src.keyboards.inline import regist as regist_kb
from src.states import Main, Regist

regist = Router()
regist.callback_query.filter(StateFilter(Regist.Name, Regist.Gender, Regist.Avatar))

@regist.callback_query(Regist.Avatar, F.data == "regist:avatar")
async def _avatar(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Main.Base)

    await message.delete()
    await message.answer(html.italic("Регистрация пройдена"), reply_markup=reply.base)

    await callback.answer()

@regist.callback_query(Regist.Gender, F.data.regexp(r"^regist:gender:((?:fe)?male)$"))
async def _gender(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Regist.Avatar)

    await message.delete()
    await message.answer("📸 Отправь свою фотку", reply_markup=regist_kb.avatar)

    await callback.answer()

@regist.callback_query(Regist.Name, F.data == "regist:name")
async def _name(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Regist.Gender)

    await message.delete()
    await message.answer("👽 Какого ты пола?", reply_markup=regist_kb.gender)

    await callback.answer()

__all__ = [regist]
