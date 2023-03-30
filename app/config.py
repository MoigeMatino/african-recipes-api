from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class BaseConfig(BaseSettings):
    app_name: str = "My App"
    debug: bool = False
    testing: bool = False

    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")

class DevelopmentConfig(BaseConfig):
    debug: bool = True

class TestingConfig(BaseConfig):
    testing: bool = True

class ProductionConfig(BaseConfig):
    POSTGRES_PORT: int = os.getenv("PROD_POSTGRES_PORT")
    POSTGRES_PASSWORD: str = os.getenv("PROD_POSTGRES_PASSWORD")
    POSTGRES_USER: str = os.getenv("PROD_POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("PROD_POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("PROD_POSTGRES_HOST")

# Use the appropriate configuration class based on the current environment

env: str = os.getenv('ENV')

if env == "production" or env == 'prod':
    config = ProductionConfig()
elif env == "testing":
    config = TestingConfig()
else:
    config = DevelopmentConfig()