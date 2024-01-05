from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_base.db"
db = SQLAlchemy(app)
