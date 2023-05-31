import uvicorn
from fastapi import FastAPI

from routes.user import UsersRouter

app = FastAPI()

app.include_router(UsersRouter)
# app.include_router(, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
