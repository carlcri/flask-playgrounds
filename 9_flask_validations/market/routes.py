from market import app
from market.models import Item
from market.forms import RegisterForm
from flask import render_template, redirect, url_for
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
    print(app.config['SECRET_KEY'])
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return render_template('test.html')


@app.route('/groceries')
def groceries():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 2, 'precio unitario': 14}
    ]
    return render_template('groceries.html', items=items)


@app.route('/register', methods=['GET', 'POST']) 
def register_new_user():
    register_form = RegisterForm() 
    context = {
        'register_form': register_form,
    }

    if register_form.validate_on_submit(): 
        user_name = register_form.username.data
        click.echo(click.style(f'user_name: {user_name}',  fg='green'))

        return(redirect(url_for('groceries')))
    
    else:
        click.echo(click.style('Something bad is happening', fg='red'))
        print(register_form.errors)
    
    return render_template('register.html', **context)