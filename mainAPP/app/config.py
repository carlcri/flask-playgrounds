import os
from dotenv import load_dotenv

# Load config from .env file
def conection_string() -> str:
    load_dotenv()
    NEON_URI = os.environ["NEON_URI"]
    return NEON_URI


def secret_key() -> str:
    load_dotenv()
    SECRET_KEY = os.environ["SECRET_KEY"]
    return SECRET_KEY


class Config:
    SECRET_KEY = secret_key()
    NEON_URI = conection_string()