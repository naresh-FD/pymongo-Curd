def UserEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "email": str(item["email"]),
        "password": str(item["password"]),
    }


def UsersEntity(entity) -> list:
    return [UserEntity(user) for user in entity]

# from typing import List
#
# from pydantic import BaseModel, EmailStr, Field
#
#
# class UserBase(BaseModel):
#     name: str = Field(..., min_length=2, max_length=50)
#     email: EmailStr
#
#
# class UserCreateRequest(UserBase):
#     password: str = Field(..., min_length=8)
#
#
# class UserResponse(UserBase):
#     id: str = Field(..., alias="_id")
#
#     class Config:
#         orm_mode = True
#
#
# def UserEntity(item) -> UserResponse:
#     return UserResponse(id=str(item["_id"]), name=item["name"], email=item["email"])
#
#
# def UsersEntity(entity) -> List[UserResponse]:
#     return [UserEntity(user) for user in entity]
