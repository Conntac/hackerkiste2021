from typing import Optional, List
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from schemas import *
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    created = crud.create_user(db=db, user=user)
    return None

@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    print(users)
    # return None
    return users

@app.get("/session/{id}", response_model=schemas.Session)
def read_item(id: str):
    return {"item_id": id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: schemas.User):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    print("Use 'python3 -m uvicorn main:app --reload'")
