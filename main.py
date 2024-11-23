from fastapi import FastAPI

from repository.database import database
from controller.user_controller import router as user_router
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shut_down():
    await database.disconnect()


app.include_router(user_router)