import os
from pydantic_settings import BaseSettings


class DefaultSettings(BaseSettings):
    """
    Default configs for application
    """
    ENV: str = os.getenv("ENV", "local")

    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "etl_pipeline")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "airflow")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "airflow")
    POSTGRES_CONTAINER_NAME: str = os.getenv("POSTGRES_CONTAINER_NAME", "postgres_db")

def get_settings() -> DefaultSettings:
    return DefaultSettings()