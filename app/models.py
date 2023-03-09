import uuid
from sqlalchemy.orm import declarative_base, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Integer
from typing import List
from db import engine

Base = declarative_base()


class Recipe(Base):
    __tablename__='recipes'

    id=mapped_column(UUID(as_uuid=True), index=True, primary_key=True, default=uuid.uuid4)
    title=mapped_column(String, index=True, nullable=False)
    serving=mapped_column(Integer)
    ingredients:List[str]=mapped_column(str, nullable=False)
    instructions=mapped_column(str, nullable=False)

    Base.metadata.create_all(bind=engine)