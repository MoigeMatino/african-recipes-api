from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session, mapped_column

db_uri='sqlite+pysqlite:///./db.sqlite3:'
engine=create_engine(db_uri, future=True, echo=True)
session=sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base=declarative_base()

def get_db() -> None:
    db=session()
    try:
        yield db
    finally:
        db.close()