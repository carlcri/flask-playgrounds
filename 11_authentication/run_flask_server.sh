source env/bin/activate

export FLASK_APP=main.py
export FLASK_DEBUG=1

export FLASK_ENV=development
echo FLASK_ENV
flask run
