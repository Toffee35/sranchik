from aiogram.fsm.state import State, StatesGroup


class Regist(StatesGroup):
    Name = State()
    Gender = State()
    Avatar = State()


class Main(StatesGroup):
    Base = State()

    Profile = State()
    Menu = State()
    Judging = State()


class Menu(StatesGroup):
    Search = State()
    Filter = State()


class Profile(StatesGroup):
    Name = State()
    Avatar = State()


__all__ = [Regist, Main, Menu, Profile]
