from market import app
from market.models import Item
from flask import render_template
import click


@app.route('/')
@app.route('/home')
def home():
    consulta = Item.query.filter_by(precio=10.45)
    for item in consulta:
        click.echo(click.style(f'item_id:{item.id} precio:{item.precio}', fg='green'))
        
    consulta = Item.query.all()
    return render_template('home.html', consulta=consulta) 


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/groceries')
def groceries():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 2, 'precio unitario': 14}
    ]
    return render_template('groceries.html', items=items)

