from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
engine=create_engine(DATABASE_URL, future=True, echo=True)
SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)

def get_db() -> None:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()