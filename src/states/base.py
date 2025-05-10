from aiogram.fsm.state import State, StatesGroup


class BaseState(StatesGroup):
    base = State()
