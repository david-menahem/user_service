from api.internalAPI import poll_service
from model.user import User
from repository import user_repository


async def get_by_id(user_id: int) -> User:
    user = await user_repository.get_by_id(user_id)
    if user:
        return user
    else:
        raise Exception(f"User with id: {user_id} does not exist")


async def create(user: User) -> User:
    return await user_repository.create(user)


async def update(user_id: int, user: User) -> User:
    await get_by_id(user_id)
    user.id = user_id
    return await user_repository.update(user)


async def soft_delete(user_id: int):
    await get_by_id(user_id)
    await poll_service.delete_answers_by_user_id(user_id)
    await user_repository.soft_delete(user_id)


async def register_user(user_id: int) -> str:
    await get_by_id(user_id)
    if await user_repository.register_user(user_id):
        return f"User with id: {user_id} is successfully registered"
    else:
        return f"User with id: {user_id} is inactive and cannot register"

