import uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import String, Integer, Column
from typing import List
from db import engine

Base = declarative_base()
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        UUID(as_uuid=True),
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

    # Base.metadata.create_all(bind=engine)