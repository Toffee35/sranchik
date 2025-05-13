import enum
from datetime import datetime

from sqlalchemy import Enum, func
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

users_engine: AsyncEngine = create_async_engine("sqlite+aiosqlite:///users.db")
users_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    users_engine, expire_on_commit=False
)


class Gender(enum.Enum):
    Male = "male"
    Female = "female"


class UsersBase(AsyncAttrs, DeclarativeBase):
    pass


class UserData(UsersBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    mention: Mapped[str]
    gender: Mapped[Gender] = mapped_column(Enum(Gender))
    avatar: Mapped[str]
    kisses: Mapped[int] = mapped_column(default=0)
    shits: Mapped[int] = mapped_column(default=0)
    invites: Mapped[int] = mapped_column(default=0)
    last_mailing: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        items = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())

        return f"{self.__class__.__name__}({items})"


__all__ = [Gender, UserData, UsersBase, users_engine, users_session]
