import os
from dotenv import load_dotenv

def secret_key():
    load_dotenv()
#    SECRET_KEY='miclavesecreta'
    SECRET_KEY = os.environ['SECRET_KEY']
    return SECRET_KEY


def sqlalchemy_uri():
    load_dotenv()
#    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_DATABASE_URI='sqlite:///data_base.db'
    return SQLALCHEMY_DATABASE_URI


class Config():
    SECRET_KEY = secret_key()   
    SQLALCHEMY_DATABASE_URI = sqlalchemy_uri()
    