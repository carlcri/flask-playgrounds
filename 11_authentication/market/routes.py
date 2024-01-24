from market import app, db  
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, flash, request
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
        user_name = register_form.username.data.lower()
        click.echo(click.style(f'user_name: {user_name}',  fg='green'))

        new_user = User(username=register_form.username.data.lower(), 
                    email_address=register_form.email_address.data.lower(), 
                    password=register_form.password2.data)
        
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
            flash(f'usuario: {user_name} creado con exito', category="success")

        return(redirect(url_for('groceries')))
    
    else:
        click.echo(click.style('Something bad is happening', fg='red'))
        for error_msg in register_form.errors.values():
            flash(error_msg, category="danger")
        
    return render_template('register.html', **context)



@app.route('/delete')
def delete_user():
    id = request.args.get('id')

    with app.app_context():
        user = User.query.filter_by(id=id).first()

        if not user:
            flash(f'usuario con {id} no existe', category="danger")
        else:
            db.session.delete(user)
            db.session.commit()
            flash(f'usuario {id} eliminado', category='success')

    return render_template('delete.html', id=id)


@app.route('/login')
def login_user():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }

    return render_template('login.html', **context)