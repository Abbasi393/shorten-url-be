from pydantic import BaseModel, EmailStr


class UserCreateModel(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponseModel(UserCreateModel):
    pass


class UserLoginModel(BaseModel):
    username: str
    password: str


class TokenResponseModel(BaseModel):
    access_token: str
    token_type: str
