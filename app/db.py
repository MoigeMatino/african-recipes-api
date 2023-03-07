from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_uri='sqlite+pysqlite:///./db.sqlite3:'
engine=create_engine(db_uri, future=True, echo=True)
session=sessionmaker(autocommit=False, autoflush=False,bind=engine)

def get_db() -> None:
    db=session()
    try:
        yield db
    finally:
        db.close()