from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class User(BaseModel):
    name = str
    email = str
    password = str


class UserCreateRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

# class UserCreateRequest(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
