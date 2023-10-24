# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run
import os, click
from flask import request, render_template
from app.services import EmployeeService

# importamos la funcion para crear la aplicacion y la forma
from app import create_app

app = create_app()


# Ruta raiz
@app.route('/')
def root():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    last_directory = os.path.basename(current_directory)

    print(app.config['SECRET_KEY'])
    print(app.config['NEON_URI'])

    return f'Current Project: {last_directory}'



@app.route('/query-example')
def query_example():

    name = request.args.get('name')
    lastname = request.args.get('lastname')
    age = request.args.get('age')

    context = {
        'name': name,
        'lastname': lastname,
        'age': age,
    }

    return render_template('query_example.html', **context)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():

    if request.method == 'POST':
        name = request.form.get('name')
        context = {
            'name': name
            }

        return render_template('form_example.html', **context)

    return render_template('form_example.html')


@app.route('/query-by-id/<id>')
def query_employee_by_id(id):

    connection_string = app.config['NEON_URI']
    result = EmployeeService.query_employee_by_id(connection_string, id)
    context = result
    context.update({'query_id': id})

    return render_template('query_by_id.html', **context)


@app.route('/new-employee', methods=['GET', 'POST'])
def new_employee():

    if request.method == 'POST':

        name = request.form.get('name')
        lastname = request.form.get('lastname')
        birthdate = request.form.get('birthdate')

        click.echo(click.style(f'fecha de nacimiento: {birthdate}, type: {type(birthdate)}' , fg='green'))

        context = {
            'name': name,
            'lastname': lastname,
            'birthdate': birthdate,
            }
        
        connection_string = app.config['NEON_URI']
        returned_id = EmployeeService.insert_employee(connection_string=connection_string,
                                                       **context)
        
        context.update({'returned_id': returned_id})

        return render_template('new_employee.html', **context)

    return render_template('new_employee.html')

    


#    return f'your age:{age}'



