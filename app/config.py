from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    POSTGRES_PORT:int=os.getenv("POSTGRES_PORT")
    POSTGRES_PASSWORD:str=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER:str=os.getenv("POSTGRES_USER")
    POSTGRES_DB:str=os.getenv("POSTGRES_DB")
    POSTGRES_HOSTNAME:str=os.getenv("POSTGRES_HOSTNAME")

settings = Settings()