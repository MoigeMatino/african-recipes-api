import uuid
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, String



def get_current_datetime() -> datetime:
    return datetime.now()

def generate_uuid() -> str:
    return str(uuid.uuid4())

def generate_fake_email() -> str:
    return f"{uuid.uuid4()}@fake.african.recipes"

class Base(DeclarativeBase):
    __abstract__ = True
    __allow_unmapped__ = True

    id : Mapped[uuid.UUID] = mapped_column(String, primary_key=True, default=generate_uuid)
    created_at = mapped_column(DateTime, default=get_current_datetime, nullable=False)
    updated_at = mapped_column(
        DateTime, default=None, onupdate=get_current_datetime, nullable=True
    )