import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    last_directory = os.path.basename(current_directory)

    return f'Current Project: {last_directory}'

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hola, {name}! Has enviado el formulario.'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
