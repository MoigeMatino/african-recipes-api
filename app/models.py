import uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import String, Integer, Column, Float
from typing import List

Base = declarative_base()
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        String,
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    title = Column(
        String(length=255),
        nullable=False,
        index=True
    )
    serving = Column(Integer)
    ingredients = Column(ARRAY(String), nullable=False)
    instructions = Column(String, nullable=False)
    calories = Column(Float, default=0.0)
    image_file_path = Column(String, nullable=True)
    #history
