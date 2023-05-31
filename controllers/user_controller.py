# from fastapi import FastAPI, HTTPException
import bcrypt
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, Field

from config.db import collection
from schemas.user import UsersEntity


def get_users():
    users = [user for user in collection.find()]
    # users = collection.find_all()
    transformed_users = UsersEntity(users)
    return transformed_users


class UserCreateRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)


def create_user(user: UserCreateRequest):
    user_data = {
        "name": user.name,
        "email": user.email,
        "password": bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    }

    user_exists = collection.find_one({"username": user.name}) is not None
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Check if the email already exists in the database.
    email_exists = collection.find_one({"email": user.email}) is not None
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already exists")

    result = collection.insert_one(user_data)
    inserted_id = result.inserted_id
    print("Insert", inserted_id)
    return {"message": "User created successfully", "user": result}
