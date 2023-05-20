import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class BaseConfig(BaseSettings):
    app_name: str = "My App"
    debug: bool = False
    testing: bool = False

    POSTGRES_PORT: Optional[str] = os.getenv("POSTGRES_PORT")
    POSTGRES_PASSWORD: Optional[str] = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER: Optional[str] = os.getenv("POSTGRES_USER")
    POSTGRES_DB: Optional[str] = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: Optional[str] = os.getenv("POSTGRES_HOST")
    POSTGRES_HOSTNAME: Optional[str] = os.getenv("POSTGRES_HOSTNAME")


class DevelopmentConfig(BaseConfig):
    debug: bool = True


class TestingConfig(BaseConfig):
    testing: bool = True


class ProductionConfig(BaseConfig):
    POSTGRES_PORT: Optional[str] = os.getenv("PROD_POSTGRES_PORT")
    POSTGRES_PASSWORD: Optional[str] = os.getenv("PROD_POSTGRES_PASSWORD")
    POSTGRES_USER: Optional[str] = os.getenv("PROD_POSTGRES_USER")
    POSTGRES_DB: Optional[str] = os.getenv("PROD_POSTGRES_DB")
    POSTGRES_HOST: Optional[str] = os.getenv("PROD_POSTGRES_HOST")
    POSTGRES_HOSTNAME: Optional[str] = os.getenv("PROD_POSTGRES_HOSTNAME")


# Use the appropriate configuration class based on the current environment

env: Optional[str] = os.getenv("ENV")

if env == "production" or env == "prod":
    settings: ProductionConfig = ProductionConfig()

if env == "testing":
    settings: TestingConfig = TestingConfig()  # type: ignore [no-redef]

if env != "testing" or env == "production" or env == "prod":
    settings: DevelopmentConfig = DevelopmentConfig()  # type: ignore [no-redef]
