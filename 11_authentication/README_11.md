# User Authentication

Ya tenemos un FORM funcional para registrar a los usuarios. Sin embargo corregiremos algunos *bugs*, por ejemplo:

![](https://i.imgur.com/eTrAIMB.png)

Que siempre se guarde en la BD datos en minusculas tanto para el correo como para el usuario, usando simplemente la funcion lower().

### routes.py

```py
 if register_form.validate_on_submit(): 
        user_name = register_form.username.data.lower()
        click.echo(click.style(f'user_name: {user_name}',  fg='green'))

        new_user = User(username=register_form.username.data.lower(), 👈
                    email_address=register_form.email_address.data.lower(), 👈
                    password_hash=register_form.password2.data)
```

### forms.py

```py
    def validate_username(self, username_to_validate):
        with app.app_context():
            consulta = User.query.filter_by(username=username_to_validate.data.lower()).first() 👈
        if consulta is not None:
            raise ValidationError(f'Usuario: {consulta} ya existe, intente nuevamente') 
        
    
    def validate_email_address(self, email_to_validate):
        with app.app_context():
            consulta = User.query.filter_by(email_address=email_to_validate.data.lower()).first() 👈
            if consulta is not None:
                raise ValidationError(f'correo {consulta.email_address}: ya existe, intento otro correo')
```

## Borrando filas de la BD

Necesitamos borrar ciertas filas usando *flask-sqlalchemy*. Modificamos temporalmente *config.py*. Y de esta forma realizamos la operacion directamente desde el interprete:

```py
from market.config import Config
from market.models import User
from market import db, app

with app.app_context():
    user = User.query.filter_by(id=17).first()
    db.session.delete(user)
    db.session.commit()
```

https://www.delftstack.com/howto/python-flask/flask-sqlalchemy-delete/

## Guardando los passwords encriptados

Estamos guardando los passwords en *plain text*, lo primero es añadir una nueva dependencia a *requirements.txt*:

    flask_bcrypt

Verificamos con el comando *pip freeze* que se haya instalado. La importamos en *dunder init file* el *init.py*:

    from flask_bcrypt import Bcrypt

Y Crearemos una instancia de Bcrypt para usarla en toda la aplicacion, usando nuestra aplicacion como argumento:

    bcrypt = Bcrypt(app)

```py
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from market.config import Config

from flask_bcrypt import Bcrypt 👈

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
#    app.config['SECRET_KEY']='546d97931c703853c879afa4'
    return app

app = create_app()

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_base.db"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app) 👈

from market import routes
```
Ahora debemos ir a nuestro *models.py* y crear algunas propiedades adicionales, ¿Te acuerdas cuando estudiamos getters and setters? Pues esta es la oportunidad de usarlos.

Ve a la seccion de *0_Getters* para ver un ejemplo practico antes de este tema avanzado.

Para la clase *user* creo el *getter* y el *setter*

```py
    @property
    def password(self):
        return self.password_hash
    

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8') 
```

 Y aunque hize pruebas en *0_Getters* y el codigo que muestro no deberia funcionar, aqui si funciona. En *routes.py*:

 ```py
        new_user = User(username=register_form.username.data.lower(), 
                    email_address=register_form.email_address.data.lower(), 
                    password=register_form.password2.data) 👈
```
Se cambio *password_hash* que es el atributo de clase, por el nombre del decorador. 

![](https://i.imgur.com/U8faB9l.png)

Como vez ahora, el password se guarda de manera hasheada. 🆗

## Creando una ruta para borrar usuarios

Ya que he creado tantos usuarios, necesito borrarlos de alguna forma. Asi que haciendo uso del concepto de los *query arguments*, hago la primera implementacion:

Importamos *request*

    from flask import render_template, redirect, url_for, flash, request

Y probamos:

```py
@app.route('/delete')
def delete_user():
    id = request.args.get('id')
    return f'id : {id}'
```

![](https://i.imgur.com/oF3QL62.png)

Y finalmente implementamos toda la funcion:

```py
@app.route('/delete')
def delete_user():
    id = request.args.get('id')

    with app.app_context():
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

    return render_template('delete.html', id=id)
```

El codigo funciona bien, pero obviamente se crashea cuando no exite tal id en la base de datos. Asi que le agrego funcionalidades para que incluso muestre *flashes*:

```py
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
```

## Creando login

Ahora que se ha creado el usuario de forma exitosa, tiene sentido una cada vez que se cree, se rediriga a una ruta de login.

Una vez creado *login.html* y una ruta basica. Es momento de crear la forma para el login:

Consulta la rama **deploy_heroku** en GitHub:

https://github.com/carlcri/2_CursoFlask/blob/deploy_heroku/documentation/2_Extensiones_Flask.md

1. Creamos la forma:

```py
class LoginForm(FlaskForm):
    username = StringField(label='tu usuario', validators=[DataRequired()])
    password = StringField(label='contraseña', validators=[DataRequired()])
    submit = SubmitField(label='Enviar')
```

2. La importamos:

        from market.forms import RegisterForm, LoginForm

3. A diferencia del la forma de *registro* donde la construimos con *html*, hay una forma mas rapida de hacerla, y es usando un        template de Bootstrap:

   *The bootstrap/wtf.html template contains macros to help you output forms quickly*

        {% import 'bootstrap/wtf.html' as wtf%}
        ...
        ...
        {{wtf.quick_form(loginform)}}

4. Implementarla simplemente para que la muestre:

```py
@app.route('/login')
def login_user():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }

    return render_template('login.html', **context)
```

![](https://i.imgur.com/pJSGkoP.png)

haciendo un pequeño *tunning* para que muestre un *placeholder*, se hace uso del argumento **render_kw**:

```py
class LoginForm(FlaskForm):
    username = StringField(label='Usuario', validators=[DataRequired()], render_kw={"placeholder": "Ingrese usuario"}) 👈
    password = StringField(label='Contraseña', validators=[DataRequired()], render_kw={"placeholder": "ingrese contraseña"}) 👈
    submit = SubmitField(label='Enviar')
```

## Mejorando el FrontEnd

Como practica en del curso de *Bootstrap*, se crea *base2.html* usando elementos de Bootstrap y de *flask-bootstrap*. Por ejemplo se usan estructuras {% block %} ... {% endblock %}, para definir bloques para ser sobrescritos en otras plantillas. Tambien se incluye en el *base2.html*, la bloque para manejar los *flashes*. Veamos parte por parte:

### Head

```html
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--Favicon-->
    <link rel="icon" type="image/x-icon" href="../static/images/fire.svg">👈
    <!-- Estilos -->
    <link rel="stylesheet" href="../static/estilos2.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">👈
    <!-- Iconos -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">👈

    <title>
        {% block title %} Market | {% endblock%}  👈
    </title>
```

1. Modifico el favicon con un icono que obtuve de Bootstrap 
2. Incluimos *Bootstrap* con un CDN, segun lo descrito en la documentacion.
3. Inclui *the icon fonts stylexsheet* para usar la oferta de icono de Bootstrap
4. Usando las plantillas de Jinja2, para incluir codigo reutilizable, como es el caso del *block title*

La estructura {% block %} ... {% endblock %} se utiliza para definir bloques que pueden ser sobrescritos en plantillas que extienden esta plantilla base.

### Body

Usando la sintaxis de jinja2, se incluye la bara de navegacion, la funcionalidad para mostrar flashes, e incluyendo el script de *js*, que segun la documentacion, se recomiendo usarla al final del body. 

```html
    {% block navbar %}
        {%include 'navbar2.html'%}
    {% endblock%}

    <!-- Display Flashes-->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %}
            <div class="alert alert-{{category}} alert-dismissible">
                <!-- <button type="button" data-dismiss="alert" class="close">&times;</button> -->
                <button type="button" data-dismiss="alert" class="btn-close" aria-label="Close"></button> 
                {{message}}
            </div>
        {% endfor %}
    {% endwith %}


    {% block content%}
        <!--Contenido-->
    {% endblock%}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script> 👈
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> 
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>  
```

#### Haciendo funcionar los flashes:

Como no estamos haciedno uso como lo veniamos haciendo de otros proyectos de *flask*, donde heredabamos del *base.html* de *Boostrap*

Si te fijas, esta sentencia no existe en nuestro *base*:

```html
{% extends 'bootstrap/base.html' %}
```

Asi, se veria el flash, un poco raro, y lo peor es que no se puede cerrar.

![](https://i.imgur.com/3rsb1cA.png)

Si inspeccionar un proyecto de los tantos que se han hecho en *flask*, y le indicamos al navegador nos deje ver el codigo fuente, entonces de ahi nos damos cuenta que lo que hace falta es incluir estos scripts:

```html
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> 
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script> 
```

Y veremos que ya se puede cerrar. Por otra parte seria bueno mejorar el diseño del mensaje. Obseravando la documentacion del *close button* como es:

https://getbootstrap.com/docs/5.0/components/close-button/

Encontramos esto:

```html
<button type="button" class="btn-close" aria-label="Close"></button>
```
Si agregamos *data-dismiss="alert"*, obtenemos: 

```html
<button type="button" data-dismiss="alert" class="btn-close" aria-label="Close"></button>
```

Que ya implementado, nos dara un diseño mas profesional:

![](https://i.imgur.com/9NSAsaI.png)

