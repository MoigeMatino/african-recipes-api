from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session, mapped_column
from sqlalchemy import String, Integer
from typing import List
from db import engine

Base = declarative_base()


class Recipe(Base):
    __tablename__='recipes'

    title=mapped_column(String, index=True, nullable=False)
    serving=mapped_column(Integer)
    ingredients:List[str]=mapped_column(str, nullable=False)
    instructions=mapped_column(str, nullable=False)

    Base.metadata.create_all(bind=engine)