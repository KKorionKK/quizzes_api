from dataclasses import dataclass
from dotenv import find_dotenv, dotenv_values
from functools import cache


@dataclass
class Settings:
    DB_NAME: str
    PG_USER: str
    PG_PASSWORD: str
    DB_ADAPTER: str
    DB_HOST: str
    DB_PORT: str


@cache
def get_settings() -> Settings:
    settings = dotenv_values(find_dotenv())
    return Settings(**settings)
