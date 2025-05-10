from enum import Enum
from typing import List


class Gender(Enum):
    Male = "Мужской"
    Female = "Женский"


class UserData:
    name: str
    gender: Gender
    avatar: str
    kisses: int
    shits: int
    invited: List[int]

    def __init__(self, name: str, gender: Gender, avatar: str):
        self.name = name
        self.gender = gender
        self.avatar = avatar
        self.kisses = 0
        self.shits = 0
        self.invited = []

    def __repr__(self):
        items = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())

        return f"{self.__class__.__name__}({items})"


__all__ = [Gender, UserData]
