from typing import Optional, List

from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session

import crud
import models
import schemas
import uuid
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
    db_user = crud.get_user(db, user_id=str(user.id))
    if db_user:
        raise HTTPException(status_code=400, detail="Already registered")

    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/session/{id}", response_model=schemas.Session)
def read_session(id: str, db: Session = Depends(get_db)):
    return crud.get_session(db, id)


@app.get("/session/new", response_model=schemas.Session)
def create_session(db: Session = Depends(get_db)):
    session = schemas.Session(
        id=uuid.uuid4()
    )
    return crud.create_session(db, session)


@app.post("/dishes/", response_model=schemas.Dish)
def create_dish(dish: schemas.Dish, db: Session = Depends(get_db)):
    db_dish = crud.get_dish(db, dish_id=str(dish.id))
    if db_dish:
        raise HTTPException(status_code=400, detail="Already registered")

    return crud.create_dish(db=db, dish=dish)


@app.get("/dishes/", response_model=List[schemas.Dish])
def read_dish(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_dishes(db, skip=skip, limit=limit)


if __name__ == "__main__":
    print("Use 'python3 -m uvicorn main:app --reload'")
