from aiogram.fsm.state import State, StatesGroup


class RegistState(StatesGroup):
    name = State()
    gender = State()
    avatar = State()
