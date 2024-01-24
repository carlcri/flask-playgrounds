# Flashes and Advanced Validations

Flashes o mensajes emergentes.

Es un banner que aparece abajo de la barra de navegacion. Estos mensajes son de informacion o ayuda al usuario, pueden ser de exito, fallo, o warning. Lo primero es importar:

    from flask import flash

En nuestro *base.html* implementaremos la logica necesaria para desplegarlos. Del curso de flask de Platzi, habiamos visto como desplegarlos.

## Primera Implementacion

Por ejemplo, cuando se crea un usuario con exito, y usando la funcion *get_flashed_messages()*

```html
{% block body %}

    {% block navbar %}
        {%include 'navbar.html'%}
    {% endblock %}

    {% for message in get_flashed_messages() %}
        {{message}}
    {% endfor %}

    {% block content%}
        <!--Contendio de los otros templates-->
    {% endblock%}

{% endblock %}
```

![](https://i.imgur.com/hZ0w7W9.png)

## Segunda Implementacion - Usando uso de clases de Bootstrap

```html
    {% for message in get_flashed_messages() %}
        <div class="alert alert-success">
            {{message}}
        </div>
    {% endfor %}
```

La clase alert y alert-success pertenece a Bootstrap, un popular framework de diseño de código abierto. Bootstrap proporciona una serie de estilos predefinidos para diferentes tipos de alertas y mensajes. En este caso, se está utilizando una alerta de éxito (alert-success), que generalmente se muestra con un fondo verde para indicar un mensaje exitoso.

![](https://i.imgur.com/e7qI8GT.png)

### Tercera - Cerrando las alertas

- Añadir la clase *alert-dismissible*.

- Añadir la clase *close* y data-dismiss="alert" a un elemento de tipo boton, para poder cerrarlo

```html
    {% for message in get_flashed_messages() %}
        <div class="alert alert-success alert-dismissible">
            <button type="button" data-dismiss="alert" class="close">&times;</button> 👈
            {{message}}
        </div>
    {% endfor %}
```
Ya aparece la cruzecita de cerrar, pero si le doy click, este no podra cerrar la alerta 😫

Para que esta funcionalidad de cierre dinámico funcione correctamente, se deben incluir los archivos de JavaScript de Bootstrap, ya que estos contienen el código necesario para manejar eventos como el clic en el botón de cierre y realizar las acciones correspondientes, como cerrar la alerta.

Al incluir {{ super() }} dentro del bloque scripts al final del documento, se está asegurando de que cualquier script JavaScript que ya esté incluido en la plantilla base ("bootstrap/base.html") también se cargue. Esto es esencial para que la funcionalidad de cierre dinámico de las alertas de Bootstrap funcione correctamente en tu aplicación.


```html
    <!-- importa los archivos javascript de bootstrap, y hereda, sin esto no se puede cerrar los flashes-->
    {% block scripts %}
        {{super()}}
    {% endblock%}
```
Al incluir los scripts, la alerta finalmente cierra. 😍

## Empezando de nuevo desde cero

Lo que hizimos esta muy bien, pero ahora desarrollaremos una nueva implementacion que permita mostrar los mensajes de error al momento de registrar un nuevo usuario. Borraremos lo hecho en la primera parte, y empezaremos desde cero. 

*register_form.errors* es un diccionario:

![](https://i.imgur.com/tjlEXBO.png)

Pero solo vamos a imprimir los valores, y de una vez los vamos a enviar como un flash:

```py
    else:
        click.echo(click.style('Something bad is happening', fg='red'))
        for error_msg in register_form.errors.values():
            flash(error_msg) 👈
```

La implementaremos un poco diferente en el base.html con un *context manager*:

```html
    {% with messages = get_flashed_messages() %}
        {% for message in messages %}
            {{message}}
        {% endfor %}
    {% endwith %}
```

![](https://i.imgur.com/nKosBpp.png)

## Segunda Implementacion

Necesitamos tal vez separar los mensajes por categorias, por eso en el context manager agregamos *with_categories=true*, y observamos el resultado:

```html
    {% with messages = get_flashed_messages(with_categories=true) %} 👈
        {% for message in messages %}
            {{message}}
        {% endfor %}
    {% endwith %}
```

Y ahora muestra, algo adicional que dice mensaje, que es la categoria:

![](https://i.imgur.com/voIcAEN.png)

Si en realidad le asignamos una categoria a nuestros mensajes, y aun mas le damos un nombre de una de las siguientes clases de bootstrap para renderizarlo con un color especifico:

![](https://i.imgur.com/z3boppP.png)

Vamos a categorizarlo como **danger**


Pero en realidad no lo queremos mostrar, porque esa no es su utilidad:

```html
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %} 👈
            {{message}}
        {% endfor %}
    {% endwith %}
```

### ¿Entonces para que vamos a usar la categoria?

la clave es darle el nombre a la categoria de las mismas clases de bootstrap asi:

```html
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% for category, message in messages %}
            <div class="alert alert-{{category}} alert-dismissible"> 👈
                <button type="button" data-dismiss="alert" class="close">&times;</button> 
                {{message}}
            </div>
        {% endfor %}
    {% endwith %}
```

Donde muy ingenionsamente alert-{{category}} sera igual a **alert-danger** 😊

![](https://i.imgur.com/0ssKYfN.png)

Igualmente añadimos la logica para crear un flash de registro exitoso de usuario:

```py
with app.app_context():
    db.session.add(new_user)
    db.session.commit()
    flash(f'usuario: {user_name} creado con exito', category="success") 👈
```

## ¿Que pasaria si se intenta crear un usuario que ya existe?

Intentaremos crear al usuario *chambimbe*:

![](https://i.imgur.com/ZUCSJRz.png)

Dado que en la tabla o clase *User* el campo *username* es un campo unico, este error tiene total sentido

### Intentando Consultar la BD desde la consola.

Despues de muchos intentos, donde al importar desde la consola

![](https://i.imgur.com/BQ0hf0C.png)

Decidi hacer estos cambios en el archivo *Config*, para que cargue las variables de entorno directamente, y no desde el archivo *.env*. Una vez termine la prueba, vuelvo a descomentarlos:

```py
import os
from dotenv import load_dotenv

def secret_key():
    load_dotenv()
    SECRET_KEY='miclavesecreta' 👈
#    SECRET_KEY = os.environ['SECRET_KEY']
    return SECRET_KEY


def sqlalchemy_uri():
    load_dotenv()
#    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_DATABASE_URI='sqlite:///data_base.db' 👈
    return SQLALCHEMY_DATABASE_URI


class Config():
    SECRET_KEY = secret_key()   
    SQLALCHEMY_DATABASE_URI = sqlalchemy_uri()
    
```

Volvemos a intentarlo, y esta vez funciona normalmente:

```py
from market.config import Config
from market.models import Item, User
from market import app, db

with app.app_context():
    consulta = User.query.filter_by(username='chambimbe').first()
```
Hemos consultado si existe el usuario *chambimbe* el cual existe. Ahora, ¿Si el usuario no exite que pasa?

![](https://i.imgur.com/zzzzKCu.png)

Observamos que es un *None*. De esta forma reversaremos los cambios en *config*, y ahora si implementaremos la logica para manejar el error. 

## Primera Implementacion

Vamos a *routes.py*, y desde alli implementamos la logica:

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
        
        with app.app_context():
            user_name_exists = User.query.filter_by(username=new_user.username).first() 👈

            if user_name_exists:
                print(f'usuario {user_name_exists.username} ya existe')
                flash(f'usuario: {user_name_exists.username} ya exite. Intente nuevamente', category='danger') 👈
            else:
                db.session.add(new_user)
                db.session.commit()
                flash(f'usuario: {user_name} creado con exito', category="success")
                return(redirect(url_for('groceries')))

        
    else:
        click.echo(click.style('Something bad is happening', fg='red'))
        for error_msg in register_form.errors.values():
            flash(error_msg, category="danger")
        
    return render_template('register.html', **context)
```

- Se consulta la BD y se guarda la consulta.
- Si la consulta no es un valor nulo, no realiza la transacion, y por el contrario, flashes un mensaje en color rojo.

![](https://i.imgur.com/UPsli98.png)


## Segunda Implementacion

Esta primera implementacion se podria seguir mejorando, hasta por ejemplo, que sea capaz de reconocer si ya hay un correo guardado, y lo descarte.

Sin embargo, hay una forma mas profesional, que en un principio puede parecer mas complicada, pero que al final, va resular mucho mas apropiada, y escalable.

Lo primero seria deshacer los cambios en *routes.py*. 

### Modificando forms.py

Escribir una validacion si el usuario que se esta intentando registrar ya existe:

1. Con la funcion validate_username
2. Se importa el modelo, y app:

        from market.models import User
        from market import app

3. Se importa *ValidationError*:

        from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

 Y asi quedaria, vamos a  ver si funciona:

 ```py
     def validate_username(self, username_to_validate):
        with app.app_context():
            consulta = User.query.filter_by(username=username_to_validate).first()
        
        if consulta is not None:
            raise ValidationError('Usuario ya existe, intente nuevamente') 
 ```

 ![](https://i.imgur.com/wAsKSiM.png)

#### Solucionando el error

Vamoa a examinar que hay dentro de *username_to_validate*:

```py
    def validate_username(self, username_to_validate):
        print(username_to_validate) 👈
        print(type(username_to_validate)) 👈
        print(username_to_validate.data) 👈
        with app.app_context():
            consulta = User.query.filter_by(username=username_to_validate).first()
        
        if consulta is not None:
            raise ValidationError('Usuario ya existe, intente nuevamente') 
```

![](https://i.imgur.com/F16hPTx.png)

Quien esta guardando el nombre del usuario en este caso *benitocamelas* es *username_to_validate.data*, asi que realizamos los cambios:

```py
    def validate_username(self, username_to_validate):
        print(username_to_validate)
        print(type(username_to_validate))
        print(username_to_validate.data)
        with app.app_context():
            consulta = User.query.filter_by(username=username_to_validate.data).first() 👈
            print(consulta)
        if consulta is not None:
            raise ValidationError(f'Usuario ya existe, intente nuevamente') 
```

Ahora mira lo que muestra en la consola, y tambien como se comporta:

![](https://i.imgur.com/kWVcjl8.png)

![](https://i.imgur.com/W3Ln2qc.png)

Te pretuntaras como es que la funcion *validate_username* va ser ejecutada en el proyecto. Lo que es especial acerca de la libreria *validators* es que podemos crear ciertas funciones de una manera muy especifica, y *FlaskForm* se encargara del resto. 

Al nombrar la funcion  *validate_username*, FlaskForm va a buscar a todas las funciones que con el prefijo *validate_*, y posteriormente va mirar que hay despues del underscore, y hay la palabra *username*, que a su vez, es un field de la forma.

Es importante entender porque la funcion para validar si el usuario es valido o no, se llamo de esta forma especifica, porque de otra forma no va a funcionar. 

### Mejorar el codigo anterior para que incluya la validacion del correo electronico

```py
    def validate_email_address(self, email_to_validate):
        with app.app_context():
            consulta = User.query.filter_by(email_address=email_to_validate.data).first()
            if consulta is not None:
                raise ValidationError(f'correo: {consulta} ya existe, intento otro correo')
```

Y aqui una variacion, las dos funcionan, solo que en la primera flashea el nombre del usuario, y en la de abajo si flashes el correo

```py
    def validate_email_address(self, email_to_validate):
        with app.app_context():
            consulta = User.query.filter_by(email_address=email_to_validate.data).first().email_address
            if consulta is not None:
                raise ValidationError(f'correo {consulta}: ya existe, intento otro correo')
```

![](https://i.imgur.com/AUQ9KdL.png)