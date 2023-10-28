# export FLASK_APP=main.py
# export FLASK_DEBUG=1
# flask run

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 


@app.route('/test')
def test():
    return render_template('test.html')

