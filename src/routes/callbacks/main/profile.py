from aiogram import F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import reply
from src.keyboards.inline import profile as profile_kb
from src.states import Main, Profile

profile = Router()
profile.callback_query.filter(Main.Profile)


@profile.callback_query(F.data == "profile:avatar")
async def _avatar(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Profile.Avatar)

    await message.delete()
    await message.answer(
        html.italic("Давай сменим тебе имя"), reply_markup=reply.remove
    )

    await message.answer("📸 Отправь свою фотку", reply_markup=profile_kb.avatar)
    await callback.answer()


@profile.callback_query(F.data == "profile:clear")
async def _clear(callback: CallbackQuery, message: Message):
    await message.answer(html.italic("Все готово"))

    await callback.answer()


@profile.callback_query(F.data == "profile:name")
async def _name(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.set_state(Profile.Name)

    await message.delete()
    await message.answer(
        html.italic("Давай сменим тебе имя"), reply_markup=reply.remove
    )

    await message.answer("📝 Назови свое имя", reply_markup=profile_kb.name)
    await callback.answer()


__all__ = [profile]
