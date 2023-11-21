from pydantic import BaseModel
from datetime import datetime
# from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass

class UserBase(BaseModel):
    login: str
    user_fname: str
    user_sname: str


class UserOut(BaseModel):
    id: int
    login: str

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserBase

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    login: str
    password: str
    user_fname: str
    user_sname: str


class UserLogin(BaseModel):
    login: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
    # id: Optional[int] = None