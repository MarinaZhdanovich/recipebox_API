import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    DB_USER: str
    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    INIT_RECIPE: list = [
        {"name": "omelet", "description": "a great breakfast option", "difficulty": 2,
         "instructions": "mix all the ingredients and put in the oven for 20 minutes"},
        {"name": "rice milk soup", "description": "instant soup", "difficulty": 1,
         "instructions": "cook rice for 20 minutes, add milk and bring to a boil"}
    ]

    INIT_INGREDIENT: list = [
        {"name": "egg", },
        {"name": "milk", },
        {"name": "salt", },
        {"name": "water", },
        {"name": "rise", },
    ]

    INIT_USER: dict = {
        "username": "User1",
        "email": "user@test.com",
        "password": "U12e-!aQ",
        "is_active": "true",
        "role_id": 1
    }

    INIT_RECIPE_INGREDIENT: list = [
        {"recipe_id": 1, "ingredient_id": 1, "quantity": "10 units"},
        {"recipe_id": 1, "ingredient_id": 2, "quantity": "0.5 liters"},
        {"recipe_id": 1, "ingredient_id": 3, "quantity": "1 teaspoon of salt"},
        {"recipe_id": 2, "ingredient_id": 5, "quantity": "0.5 glass"},
        {"recipe_id": 2, "ingredient_id": 4, "quantity": "1 glasses"},
        {"recipe_id": 2, "ingredient_id": 2, "quantity": "2 glasses"},
        {"recipe_id": 2, "ingredient_id": 3, "quantity": "0.5 teaspoon of salt"}

    ]

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)-7s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, 'logs', 'api.log'),
            "formatter": "standard",
            "encoding": "UTF-8",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 1000
        }
    },
    "loggers": {
        "bookshelf": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}