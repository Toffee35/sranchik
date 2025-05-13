from .user import Gender, UserData, UsersBase, users_engine, users_session


async def create_tables():
    async with users_engine.begin() as conn:
        await conn.run_sync(UsersBase.metadata.create_all)


__all__ = [Gender, UserData, users_session, create_tables]
