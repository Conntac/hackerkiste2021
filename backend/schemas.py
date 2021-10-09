from typing import Optional, List
from pydantic import BaseModel
import uuid

from database import Base


class DishInfo(BaseModel):
    __tablename__ = "dishinfos"

    text: str  # md

    class Config:
        orm_mode = True


class DishExtra(BaseModel):
    __tablename__ = "dishextras"

    id: str
    name: str
    price: int

    class Config:
        orm_mode = True


class Dish(BaseModel):
    __tablename__ = "dishes"

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
    menu: List[Dish] = []
    users: List[User] = []
    finalized: bool

    class Config:
        orm_mode = True
