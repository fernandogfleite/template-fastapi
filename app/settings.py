from pydantic import BaseSettings

from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    DB_URL: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
