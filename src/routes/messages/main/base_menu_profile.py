from aiogram import F, Router, html
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, User

from src.keyboards import reply
from src.keyboards.inline import main as main_kb
from src.states import Main

base_menu_profile = Router()
base_menu_profile.message.filter(StateFilter(Main.Base, Main.Menu, Main.Profile))


@base_menu_profile.message(F.text == "🏅 Оценивать")
async def _judging(message: Message, state: FSMContext):
    await state.set_state(Main.Judging)

    await message.answer(html.italic("Поехали оценивать"), reply_markup=reply.judging)


@base_menu_profile.message(
    F.text == "📄 Меню",
    F.from_user.as_("user"),
)
async def _menu(message: Message, user: User, state: FSMContext):
    await state.set_state(Main.Menu)

    inline_kb = await main_kb.menu(user)

    await message.answer(
        f"""
📨 {html.bold("Делись ссылкой с друзьями и получи VIP статус")}

С VIP статусом ты сможешь:
    📸 {html.italic("Ставить видео или несколько фоток в профиль")}
    🧹 {html.italic("Стирать дерьмо со своего профиля")}
    💌 {html.italic("Отправлять сообщения пользователям")}
    🔎 {html.italic("Искать по полу")}
""",
        reply_markup=inline_kb,
    )


@base_menu_profile.message(F.text == "👤 Профиль")
async def _profile(message: Message, state: FSMContext):
    await state.set_state(Main.Profile)

    await message.answer(
        f"""
(👨/👩) {html.bold("Имя:")}
☺️ {html.bold("Пол:")}

💋 {html.bold("Поцелуев:")}
💩 {html.bold("Дерьма:")}
🏅 {html.bold("Место в топе:")}

📋 {html.bold("Статус:")}
""",
        reply_markup=main_kb.profile,
    )


__all__ = [base_menu_profile]
