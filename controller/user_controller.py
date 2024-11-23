from fastapi import APIRouter, HTTPException
from starlette import status

from model.user import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get(path="/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_by_id(user_id: int) -> User:
    try:
        return await user_service.get_by_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(path="/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create(user: User) -> User:
    try:
        return await user_service.create(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def update(user_id: int, user: User) -> User:
    try:
        return await user_service.update(user_id, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(path="/{user_id}", status_code=status.HTTP_200_OK)
async def soft_delete(user_id: int):
    try:
        await user_service.soft_delete(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/register_user/{user_id}", status_code=status.HTTP_200_OK)
async def register_user(user_id: int):
    try:
        return await user_service.register_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

