from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()


class DishInfo(BaseModel):
    text: str # md

class DishExtra(BaseModel):
    name: str
    price: int

class Dish(BaseModel):
    id: str
    name: str
    description: str
    price: int
    info: Optional[DishInfo] = None
    info: List[DishExtra] = []

class User(BaseModel):
    id: uuid.UUID
    name: str
    orders: List[Dish] = []

class Session(BaseModel):
    id: uuid.UUID
    menu: List[Dish] = []
    users: List[User] = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/session/{id}")
def read_item(id: str):
    return {"item_id": id}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: User):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    print("Use 'python3 -m uvicorn main:app --reload'")
