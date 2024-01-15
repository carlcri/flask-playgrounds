import os
from dotenv import load_dotenv

def secret_key():
    load_dotenv()
    SECRET_KEY = os.environ['SECRET_KEY']
    return SECRET_KEY


def sqlalchemy_uri():
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    return SQLALCHEMY_DATABASE_URI


class Config():
    SECRET_KEY = secret_key()   
    SQLALCHEMY_DATABASE_URI = sqlalchemy_uri()