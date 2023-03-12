from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DB_PORT:int=os.getenv("DB_PORT")
    POSTGRES_PASSWORD:str=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER:str=os.getenv("POSTGRES_USER")
    POSTGRES_DB:str=os.getenv("POSTGRES_DB")
    POSTGRES_HOST:str=os.getenv("POSTGRES_HOST")
    POSTGRES_HOSTNAME:str=os.getenv("POSTGRES_HOSTNAME")

    
settings = Settings()