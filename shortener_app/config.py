# Configuration file

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"


def get_settings() -> Settings:
    settings: Settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
