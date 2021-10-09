from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from database import Base


class User(Base):
    __tablename__ = "users"

    # id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    id = Column(String(length=36), default=lambda: str(
        uuid.uuid4()), primary_key=True, index=True)
    name = Column(String, index=True)

    session_id = Column(String(length=36), ForeignKey('sessions.id'))

    orders = relationship("Dish", back_populates="ordered_by")
    in_session = relationship("Session", back_populates="users")
    owns = relationship("Session", back_populates="owner")


class Session(Base):
    __tablename__ = "sessions"

    id = Column(String(length=36), default=lambda: str(
        uuid.uuid4()), primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(String(length=36), ForeignKey('users.id'))
    finalized = Column(Boolean)

    menu = relationship("Dish", back_populates="belongs_to")
    owner = relationship("User", back_populates="owns")
    users = relationship("User", back_populates="in_session")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(String(length=36), default=lambda: str(
        uuid.uuid4()), primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)

    session_id = Column(String(length=36), ForeignKey('sessions.id'))
    ordered_by_userid = Column(String(length=36), ForeignKey('users.id'))

    belongs_to = relationship("Session", back_populates="menu")
    ordered_by = relationship("User", back_populates="orders")
    meal_info = relationship("DishInfo", back_populates="owner")
    side_meal_categories = relationship(
        "DishExtraCategory", back_populates="owner")


class DishInfo(Base):
    __tablename__ = "dishinfos"

    name = Column(String, primary_key=True, index=True)

    dish_id = Column(String(length=36), ForeignKey('dishes.id'))
    owner = relationship("Dish", back_populates="meal_info")


class DishExtraCategory(Base):
    __tablename__ = "dishextracategories"

    id = Column(String(length=36), default=lambda: str(
        uuid.uuid4()), primary_key=True, index=True)
    dish_id = Column(String(length=36), ForeignKey('dishes.id'))

    owner = relationship("Dish", back_populates="side_meal_categories")
    side_meals = relationship("DishExtra", back_populates="side_meal_category")


class DishExtra(Base):
    __tablename__ = "dishextras"

    id = Column(String(length=36), default=lambda: str(
        uuid.uuid4()), primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    dish_extra_category_id = Column(
        String(length=36), ForeignKey('dishextracategories.id'))

    side_meal_category = relationship(
        "DishExtraCategory", back_populates="side_meals")
