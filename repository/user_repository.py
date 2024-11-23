from typing import Optional

from model.user import User
from repository.database import database

TABLE = "users"


async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE} WHERE id=:user_id"
    value = {"user_id": user_id}
    result = await database.fetch_one(query, value)
    if result:
        return User(**result)
    else:
        return None


async def create(user: User) -> User:
    query = f"""
        INSERT INTO {TABLE}
        (first_name, last_name, email, age, address, joining_date, is_registered)
        VALUES (:first_name, :last_name, :email, :age, :address, :joining_date, :is_registered)
        """
    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "email": user.email,
              "age": user.age,
              "address": user.address,
              "joining_date": user.joining_date,
              "is_registered": False}
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    user = await get_by_id(last_record_id[0])
    return user


async def update(user: User) -> User:
    query = f"""
        UPDATE {TABLE} SET
        first_name=:first_name, last_name=:last_name, email=:email, 
        age=:age, address=:address, joining_date=:joining_date
        WHERE id=:user_id
        """
    values = {"first_name": user.first_name,
              "last_name": user.last_name,
              "email": user.email,
              "age": user.age,
              "address": user.address,
              "joining_date": user.joining_date,
              "user_id": user.id}
    await database.execute(query, values)
    return await get_by_id(user.id)


async def soft_delete(user_id: int):
    query = f"""
    UPDATE {TABLE} SET
    is_registered=:is_registered,
    is_active=:is_active
    WHERE id=:user_id
    """
    values = {"user_id": user_id, "is_active": False, "is_registered": False}
    await database.execute(query, values)


async def register_user(user_id: int) -> bool:
    user = await get_by_id(user_id)
    if user.is_active:
        query = f"""
            UPDATE {TABLE} SET
            is_registered=:is_registered
            WHERE id=:user_id
        """
        values = {"user_id": user_id, "is_registered": True}
        await database.execute(query, values)
        return True
    else:
        return False

