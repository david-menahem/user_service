import httpx

from config.config import Config

config = Config()


async def delete_answers_by_user_id(user_id: int):
    url = f"{config.POLL_SERVICE_BASE_URL}/answer/{user_id}"
    async with (httpx.AsyncClient() as client):
        try:
            await client.delete(url)
        except httpx.HTTPStatusError as e:
            raise Exception(f"Failed to delete answers for user with id {user_id} - Error: {str(e)}")