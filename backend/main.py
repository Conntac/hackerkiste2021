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


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


# @app.get("/users/{id}/dishes", response_model=List[schemas.Dish])
# def read_dishes_for_user(id: str, db: Session = Depends(get_db)):
#     return crud.get_dishes_for_user(db, user_id=id)


@app.get("/session/", response_model=List[schemas.Session])
def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_sessions(db, skip=skip, limit=limit)


@app.get("/session/new", response_model=schemas.Session)
def create_session(db: Session = Depends(get_db)):
    session = schemas.Session(
        id=uuid.uuid4()
    )
    return crud.create_session(db, session)


@app.get("/session/{session_id}", response_model=schemas.Session)
def read_session(session_id: str, db: Session = Depends(get_db)):
    session = crud.get_session(db, session_id)
    if session is None:
        raise HTTPException(status_code=404)
    return session


@app.post("/session/{session_id}/users", response_model=schemas.User)
def create_user_for_session(session_id: str, user_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user_name=user_name)
    if db_user:
        raise HTTPException(status_code=400, detail="Already registered")

    user = schemas.User(
        id=uuid.uuid4(),
        name=user_name
    )

    db_user = crud.create_user(db=db, user=user)

    db_user.session_id = session_id
    db.commit()

    return db_user


@app.get("/session/{session_id}/users", response_model=List[schemas.User])
def read_users_for_session(session_id: str, db: Session = Depends(get_db)):
    return crud.get_users_for_session(db, session_id=session_id)


@app.post("/session/{session_id}/menu", response_model=schemas.Dish)
def create_dishes_for_session(session_id: str, dishes: List[schemas.Dish], db: Session = Depends(get_db)):
    db_dishes = []

    for dish in dishes:
        if dish.id != "":
            db_dish = crud.get_dish(db, dish_id=dish.id)
            if db_dish:
                raise HTTPException(
                    status_code=400, detail="Already registered")
            print("WARN: will ignore manually set id")

        dish.id = uuid.uuid4()

        db_dish = crud.create_dish(db=db, dish=dish)
        db_dish.session_id = session_id

        db_dishes.append(db_dish)

    db.commit()

    return db_dishes


@app.get("/session/{session_id}/menu", response_model=List[schemas.Dish])
def read_dishes_for_session(session_id: str, db: Session = Depends(get_db)):
    return crud.get_dishes_for_session(db, session_id=session_id)


@app.get("/session/{session_id}/menu/summary")
def read_summary_for_dishes_for_session(session_id: str, db: Session = Depends(get_db)):
    dishes = crud.get_dishes_for_session(db, session_id=session_id)
    dish_sum = 0
    for dish in dishes:
        dish_sum += dish.price
    return {"sum": dish_sum}


# @app.post("/dishes/", response_model=schemas.Dish)
# def create_dish(dish: schemas.Dish, db: Session = Depends(get_db)):
#     db_dish = crud.get_dish(db, dish_id=str(dish.id))
#     if db_dish:
#         raise HTTPException(status_code=400, detail="Already registered")

#     return crud.create_dish(db=db, dish=dish)


# @app.get("/dishes/", response_model=List[schemas.Dish])
# def read_dish(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud.get_dishes(db, skip=skip, limit=limit)


if __name__ == "__main__":
    print("Use 'python3 -m uvicorn main:app --reload'")
