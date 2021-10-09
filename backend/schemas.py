from typing import Optional, List
from pydantic import BaseModel
import uuid

from database import Base


class DishInfo(BaseModel):
    text: str  # md

    class Config:
        orm_mode = True


class DishExtraCategory(BaseModel):
    id: str

    class Config:
        orm_mode = True


class DishExtra(BaseModel):
    id: str
    name: str
    price: int

    class Config:
        orm_mode = True


class Dish(BaseModel):
    id: str
    name: str
    description: str
    price: int
    info: Optional[DishInfo] = None
    extras: List[DishExtra] = []

    class Config:
        orm_mode = True


class User(BaseModel):
    id: uuid.UUID
    name: str
    orders: List[Dish] = []

    class Config:
        orm_mode = True


class Session(BaseModel):
    id: uuid.UUID
    name: str
    owner: User
    menu: List[Dish] = []
    users: List[User] = []
    finalized: bool

    class Config:
        orm_mode = True
