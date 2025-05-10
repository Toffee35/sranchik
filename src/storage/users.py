from enum import Enum
from typing import Dict


class Gender(Enum):
    Male = "Мужской"
    Female = "Женский"


class User:
    name: str
    gender: Gender
    avatar: str

    def __init__(self, name: str, gender: Gender, avatar: str):
        self.name = name
        self.gender = gender
        self.avatar = avatar

    def __repr__(self):
        items = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())

        return f"{self.__class__.__name__}({items})"


users: Dict[int, User] = {}
