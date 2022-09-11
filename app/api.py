from fastapi import FastAPI

from .exceptions import (
    InvalidJudgeResult,
    InvalidJudgeResultHandler,
    InvalidToken,
    InvalidTokenHandler,
    RoomNotFound,
    RoomNotFoundHandler,
)
from .routers import room, user

app = FastAPI()
app.include_router(user.router)
app.include_router(room.router)

app.add_exception_handler(InvalidToken, InvalidTokenHandler)
app.add_exception_handler(RoomNotFound, RoomNotFoundHandler)
app.add_exception_handler(InvalidJudgeResult, InvalidJudgeResultHandler)


# Sample APIs
@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
