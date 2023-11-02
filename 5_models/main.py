# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
import click

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_base.db"
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    producto = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    precio = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'{self.producto}'


@app.route('/')
@app.route('/home')
def home():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 2, 'precio unitario': 14}
    ]
    consulta = Item.query.filter_by(precio=10.5)
    for item in consulta:
        click.echo(click.style(f'item_id:{item.id} precio:{item.precio}', fg='green'))
        
    consulta = Item.query.all()

    return render_template('home.html', items=items, consulta=consulta) 


@app.route('/test')
def test():
    return render_template('test.html')

