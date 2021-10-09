from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_dishes_for_user(db: Session, user_id: str):
    return db.query(models.Dish).filter(models.Dish.ordered_by_userid.id == user_id).all()


def get_dishes_for_session(db: Session, session_id: str):
    return db.query(models.Dish).filter(models.Dish.session_id == session_id).all()


def get_users_for_session(db: Session, session_id: str):
    return db.query(models.User).filter(models.User.session_id == session_id).all()


def get_user_by_name(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.name == user_name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Session).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(id=str(user.id),
                          name=user.name,
                          orders=user.orders
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_session(db: Session, session: schemas.Session):
    db_session = models.Session(id=str(session.id))
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


def get_session(db: Session, session_id: str):
    return db.query(models.Session).filter(models.Session.id == session_id).first()


def get_dish(db: Session, dish_id: str):
    return db.query(models.Dish).filter(models.Dish.id == dish_id).first()


def get_dishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dish).offset(skip).limit(limit).all()


def create_dish(db: Session, dish: schemas.Dish):
    db_dish = models.Dish(id=str(dish.id),
                          name=dish.name,
                          orders=dish.orders
                          )
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish
