from fastapi import APIRouter

from controllers.user_controller import get_users, create_user
from models.user import UserCreateRequest

UsersRouter = APIRouter()


@UsersRouter.get("/users")
def get_users_route():
    return {"users": get_users()}


@UsersRouter.post("/users")
def create_user_route(user: UserCreateRequest):
    print(user)
    return create_user(user)
