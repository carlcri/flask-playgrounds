# FLASK VALIDATIONS

Antes de empezar en el tema,  implementaremos la buena practica de separar la configuracion del codigo. Usamos un archivo *.env* donde se definen una serie de variables de entorno a las cuales les asignamos un valor.

Una manera de usar los archivos .env en Python es haciendo uso de la la librería *python-dotenv*:

- añadir una nueva linea al *requirements.txt*: python-dotenv
- crear el archivo .env donde se guardara toda la configuracion de la aplicacion. 
- crear el archivo *config-py* y definir la clase *Config*.

```py
import os
from dotenv import load_dotenv

def secret_key():
    load_dotenv()
    SECRET_KEY = os.environ['SECRET_KEY']
    return SECRET_KEY


def sqlalchemy_uri():
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    return SQLALCHEMY_DATABASE_URI


class Config():
    SECRET_KEY = secret_key()   
    SQLALCHEMY_DATABASE_URI = sqlalchemy_uri()
```
 Y realizando los respectivos cambios en *init.py*:

```py
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from market.config import Config 👈

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
    return app

app = create_app()
db = SQLAlchemy(app)

from market import routes
```

## Añadiendo validators

Nuestro primer validador va a ser *DataRequired*, y cuando se intente enviar la forma, sin el *usuario* mostrara un mensaje:

```py
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='usuario' , validators=[DataRequired()]) 👈
```
![](https://i.imgur.com/ZqVtJI7.png)

### Ejercicio

Añadir mas *validators*, e implementarlos para cumplir con la logica de negocio:

- passowrd and password confirmation deben coincidir
- maximo y minima longitud

#### Enviando Datos de Prueba

![](https://i.imgur.com/GTBlWhU.png)

Nota que en la ruta *register* no se ha implementado todavia ningun metodo, por lo que por defecto esta habilitado solo el metodo GET.

Aqui puedes ver como es que se esta enviando la informacion:

![](https://i.imgur.com/h3oD0cN.png)


## Realizando las primeras pruebas

Lo primero es ir a *register.html*, y añadir el atributo *method*:

```html
<form action="" class="form-register" method="POST">
    <div class="form-register-field">{{ register_form.username.label() | upper }}</div>
    {{ register_form.username(class="form-control", placeholder=" tu usuario")}}
```

### ¿Que es eso de *method="POST"*, y porque es importante?

In HTML forms, the method attribute specifies the HTTP method that the browser should use when submitting the form. The most common methods are GET and POST. Here's a brief explanation:

- GET: This method appends form data to the URL as a query string. It's suitable for requests where the form data doesn't contain sensitive information, and the data is limited in length.

```html
<form action="/example" method="GET">
    <!-- Form fields go here -->
    <input type="submit" value="Submit">
</form>
```

- POST: This method sends the form data as part of the request body, which is more secure than GET. It is suitable for forms that may contain sensitive information, such as passwords, and can handle larger amounts of data.

```html
<form action="/example" method="POST">
    <!-- Form fields go here -->
    <input type="submit" value="Submit">
</form>

```

In your specific HTML code, you have specified **method="POST"** in the <*form*> tag.

This indicates that the form data will be submitted **using the HTTP POST method**. The action="" attribute means that the form will be submitted to the same URL as the one that rendered the form.

The importance of using POST in certain situations, especially when dealing with forms that involve sensitive data like passwords, lies in the fact that the data is not exposed in the URL, making it more secure. Additionally, POST requests can handle larger amounts of data compared to GET requests.

In your Flask route, you've specified methods=['GET', 'POST'] for handling both GET and POST requests. This allows your route to handle form submissions using the POST method. The validate_on_submit() function in Flask-WTF typically works with POST requests to validate form data and protect against CSRF attacks.

### Primera Prueba Fallo

Si en este punto enviamos los datos con el boton *submit* nos mostrara un error:

![](https://i.imgur.com/kLSUCBv.png)

Vamos agregar un parametro que es una lista de los metodos permitidos en la ruta:


```py
@app.route('/register', methods=['GET', 'POST']) 👈
def register_new_user():
    register_form = RegisterForm()
    context = {
        'register_form': register_form,
    }
    
    return render_template('register.html', **context)
```
Y ahora se envian los datos y ya no aparece el error

### Implementando una logica

Cambiaremos el codigo anterior para que haga algo, y no solo mostrar la forma:

1. Que cuando se pulse el boton *submit* se valide
2. Si se valida exitosamente, que muestre en la consola el nombre y correo.
3. Si se valida exitosamente, que me lleve a una nueva ruta: *groceries*.

Probemos el siguiente codigo, y veamos si funciona

```py
@app.route('/register', methods=['GET', 'POST']) 
def register_new_user():
    register_form = RegisterForm() 
    context = {
        'register_form': register_form,
    }

    if register_form.validate_on_submit(): 👈
        user_name = register_form.username.data
        print(f'username: {user_name}')

        return(redirect(url_for('groceries')))
    
    return render_template('register.html', **context)
```

#### Pero algo pasa

Envio la forma, una y otra vez, y me lleva nuevamente a *register*, con desespero reviso el codigo sin encontrar que pasa, algo esta pasando y no se que es. 😫😫😫😫

Una forma de saber que esta pasando es mirar porque no esta validando la forma, simplemente añadiendo estas lineas:

```py
    if register_form.validate_on_submit(): 
        user_name = register_form.username.data
        print(f'username: {user_name}')

        return(redirect(url_for('groceries')))
    
    else:
        click.echo(click.style('Something bad is happenign', fg='red')) 👈
        print(register_form.errors) 👈
```
¿Y que muestra?

![](https://i.imgur.com/fC06jRC.png)

The error message indicates that the CSRF token is missing, and *it's likely the reason why validate_on_submit() is failing*. Flask-WTF uses CSRF protection to prevent Cross-Site Request Forgery attacks.

#### ¿Que es CSFR?

Los token CSRF permiten prevenir un frecuente agujero de seguridad de las aplicaciones web llamado "Cross Site Request Forgery". En español sería algo como "falsificación de petición en sitios cruzados" o simplemente falsificación de solicitud entre sitios.

Básicamente es un ataque de seguridad que permite modificar el estado del servidor haciéndose pasar por un usuarioo determinado. El sitio web confia en el el usuario pero la petición no es real y está siendo falsificada por el atacante. Como el sitio web confía en el usuario, realiza una operación solicitada y la procesa como si se tratase del usuario real.

Este ataque CSRF se puede producir fácilmente. Veamos un ejemplo:

1. Un usuario tiene una cuenta logeada en un sitio web llamemos "A".

2. El usuario navega por otra página web (llamemos "B") y esta página produce un envío de datos hacia "A". Esa solicitud se puede realizar de manera arbitraria, con cualquier conjunto de datos que el atacante quiera, por método POST si lo desea. Como estas solicitudes se pueden generar desde Javascript, el sitio web "B" puede realizar cualquier número de ellas hacia cualquier sitio.

3. La solicitud "falsificada", realizada de manera arbitraria desde "B" a "A" llega al servidor "A", que detecta que el usuario que estaba autenticado previamente, por lo que confía en él y la procesa convenientemente.

Pensemos en la página de un banco. Si el usuario estaba autenticado en el banco y navega por un sitio web atacante que realice solicitudes a la página del banco, como el usuario está previamente autenticado, el banco detectará que es de un cliente autenticado y por lo tanto realizará las operaciones que se le soliciten.

Aquí es donde el token CSRF sirve de ayuda. Este token es generado con cada solicitud en la página del banco, realizada por el usuario en el que confía. En cada formulario que luego el usuario envía, por ejemplo para hacer una transferencia, debe incluir ese token generado, de modo que el banco sabe que la solicitud fue iniciada realmente desde su sitio web, por la persona real.

#### ¿Como lo solucionamos?

The **{{ register_form.hidden_tag() }}** line generates the hidden input field for the CSRF token.

```html
        <form action="" class="form-register" method="POST">
            <!-- CSFR ToKEN -->
            {{ register_form.hidden_tag() }} 👈
```

![](https://i.imgur.com/v4OIWyK.png)

Y ahora si. Se redirige hacia la ruta especificada:

```py
return(redirect(url_for('groceries')))
```

### Haciendo algunas Pruebas

Por lo general sale un *warning* amarillo, pero muchas veces no, por ejemplo cuando el password no coincide, pero si lo imprime en la terminal.

![](https://i.imgur.com/cnXfTck.png)

Tambien esta validando cualquier cadena de texto, como correo, por lo que es necesario, instalarlo de otra forma saldra este error:


    Exception
    Exception: Install 'email_validator' for email validation support.

Se añade una nueva linea en *requirements.txt*:

    email_validator

Y probamos:

![](https://i.imgur.com/QOZmHq5.png)

### Guardando los datos en la BD

De esta forma se acceden los datos en la forma, por ejemplo para el password2:

    register_form.password2.data 


```py
@app.route('/register', methods=['GET', 'POST']) 
def register_new_user():
    register_form = RegisterForm() 
    context = {
        'register_form': register_form,
    }

    if register_form.validate_on_submit(): 
        user_name = register_form.username.data
        click.echo(click.style(f'user_name: {user_name}',  fg='green'))

        new_user = User(username=register_form.username.data, 
                    email_address=register_form.email_address.data, 
                    password_hash=register_form.password2.data)
        
        with app.app_context(): 👈
            db.session.add(new_user)
            db.session.commit()

        return(redirect(url_for('groceries')))
    
    else:
        click.echo(click.style('Something bad is happening', fg='red'))
        print(register_form.errors)
    
    return render_template('register.html', **context)
```

### Realizando mas pruebas

Aqui enviamos una forma que tenga varios errores, como vemos **register_form.errors** es un diccionario:

![](https://i.imgur.com/tjlEXBO.png)

