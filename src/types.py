from enum import Enum


class Gender(Enum):
    Male = "male"
    Female = "female"


class UserData:
    name: str
    gender: Gender
    avatar: str
    kisses: int
    shits: int
    invites: int

    def __init__(self, name: str, gender: Gender, avatar: str):
        self.name = name
        self.gender = gender
        self.avatar = avatar

        self.kisses = 0
        self.shits = 0
        self.invites = 0

    def __repr__(self):
        items = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())

        return f"{self.__class__.__name__}({items})"


__all__ = [Gender, UserData]
