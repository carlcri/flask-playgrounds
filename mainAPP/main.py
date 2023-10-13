# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run
import os
from flask import Flask, request, render_template

# se instancia un objeto de Flask
app = Flask(__name__)


# Ruta raiz
@app.route('/')
def root():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    last_directory = os.path.basename(current_directory)

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