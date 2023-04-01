from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

DATABASE_URL = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
engine=create_engine(DATABASE_URL, future=True, echo=True)
SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)

def get_db() -> None:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()