from enum import Enum
from typing import List, Optional


class Gender(Enum):
    Male = "Мужской"
    Female = "Женский"


class UserData:
    name: str
    mention: str
    gender: Gender
    avatar: str
    kisses: int
    shits: int
    invites: int
    frends: List[int]

    def __init__(
        self,
        name: str,
        mention: str,
        gender: Gender,
        avatar: str,
        inviter: Optional[int],
    ):
        self.name = name
        self.mention = mention
        self.gender = gender
        self.avatar = avatar
        self.kisses = 0
        self.shits = 0
        self.invites = 0
        self.frends = [inviter] if inviter else []

    def __repr__(self):
        items = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())

        return f"{self.__class__.__name__}({items})"


__all__ = [Gender, UserData]
