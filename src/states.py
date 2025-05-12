from aiogram.fsm.state import State, StatesGroup


class Regist(StatesGroup):
    Name = State()
    Gender = State()
    Avatar = State()


class Base(StatesGroup):
    Main = State()
    Search = State()
    Judging = State()


__all__ = [Regist, Base]
