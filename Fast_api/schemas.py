from pydantic import BaseModel
from typing import List

# schemas/item.py
# schemas/user.py


# pydantic -> 데이터 유효성 검증
# Item
class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: str | None = None
    description: str | None = None

class Item(BaseModel):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  # orm 방식으로 데이터 필드 읽기가 가능


# User
class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    email: str

    items: List[Item] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    email: str | None = None
    password: str | None = None
