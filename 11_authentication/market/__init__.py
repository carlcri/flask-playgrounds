from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from market.config import Config

from flask_bcrypt import Bcrypt

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
#    app.config['SECRET_KEY']='546d97931c703853c879afa4'
    return app

app = create_app()

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_base.db"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from market import routes