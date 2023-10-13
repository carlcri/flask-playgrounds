# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run

from flask import Flask, request

# se instancia un objeto de Flask
app = Flask(__name__)


# Ruta raiz
@app.route('/')
def root():
    return 'Hello-World'


@app.route('/query-example')
def query_example():

    name = request.args.get('name')
    lastname = request.args.get('lastname')
    age = request.args.get('age')

    return '''
              <h2>my name is: {}</h2>
              <h2>my last name is: {}</h2>
              <h2>I am {} years old'''.format(name, lastname, age)