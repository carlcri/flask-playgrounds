# FLASK FORMS

Añadimos una linea a *requirements.txt.:

- flask-wtf

Que instalara adicionalmente *WTForms*

Crearemos un nuevo archivo *forms.py*, 

```py
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='usuario')
    email_address = StringField(label='correo electronico')
    password1 = PasswordField(label='contraseña')
    password2 = PasswordField(label='confirmar contraseña')
    Submit = SubmitField('Enviar')
```
- RegisterForm hereda de FlaskForm
- Usamos PasswordField, StringField, SubmitField

## Creando una nueva ruta para el registro 

En *routes.py* importamos nuestra forma:

    from market.forms import RegisterForm 

Y creamos una nueva ruta:

```py
@app.route('/register')
def register_new_user():
    register_form = RegisterForm()
    context = {
        'register_form': register_form,
    }
    
    return render_template('register.html', **context)
```
Y realizamos una primera prueba, y falla 😫😫¿Que esta pasando?

![](https://i.imgur.com/0EmWhaR.png)

Las formas requieren una capa de seguridad adicional porque los clientes van a estar enviando informacion sensible, y *flask* requiere configurar una *llave secreta* que puede tener cualquier valor, pero que es absolutamente necesaria en este punto. Entonces vamos a nuestro archivo *init* y alli la configuramos:

```py
def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SECRET_KEY']='password' 👈
    return app
```

Una forma sencilla de generar una llave secreta es usando el modulo OS, para generar una llave de 12 caracteres y luego convertirla a hexadecimal:

    import os
    os.urandom(12).hex()

Probamos y funciona:

![](https://i.imgur.com/n0N8gET.png)

## Ejercicio

Modifica la barra de navegacion, para que aparezca la opcion de register. Ir a navbar.html y modificar el archivo usando la *built-in function* **url_for**

```html
<li><a href="{{url_for('register_new_user')}}">Registrarse</a></li>
```

## Visualizando la forma 

Hasta ahora solo visualizamos un titulo, pero ahora hay que trabajar en *register.html*, para visualizar la forma:

Hacemos una prueba super rapida donde podemos acceder la forma:

-   En el html:  {{ register_form }}

![](https://i.imgur.com/9l0no9E.png)

### Primera Version: Usando el form tag

Creemos la primera version:

```html
    <form action="" class="form-register">
        {{ register_form.username.label()}}
        {{ register_form.username(class="form-control", placeholder=" tu usuario")}}
    </form>
```

El atributo class="form-control" en el campo de entrada (input) dentro del formulario indica que se está utilizando la clase de estilo de Bootstrap llamada *form-control*. Esta clase es parte de *Bootstrap*, un marco de diseño front-end popular, y se utiliza para aplicar estilos específicos a los elementos de formulario, como campos de entrada (inputs), selectores y áreas de texto.

En este caso, al agregar class="form-control" a tu campo de entrada, estás aplicando los estilos de Bootstrap destinados a los campos de formulario, como el ajuste del ancho, el espaciado y otros estilos visuales que proporciona la clase "form-control". Esto es común en el desarrollo web cuando se utiliza Bootstrap para diseñar formularios de manera rápida y con un aspecto consistente.

En el archivo de estilos:

```css
.form-register{
    color: blue;
}
```
Y este es el resultado:

![](https://i.imgur.com/EvMqv0z.png)

### Segunda Version:

```html
    <div class="container"> 👈
        <form action="" class="form-register">
            {{ register_form.username.label()}}
            {{ register_form.username(class="form-control", placeholder=" tu usuario")}}
        </form>
    </div>
```

![](https://i.imgur.com/uj3MxxZ.png)

La línea de código *div class="container"* se refiere a un contenedor en HTML con la clase "container". En el contexto de Bootstrap, el uso de la clase "container" es parte del sistema de diseño responsivo que ofrece Bootstrap.

Bootstrap utiliza un sistema de rejilla (grid system) para organizar y estructurar el diseño de la página. Los elementos con la clase "container" se utilizan para envolver y contener el contenido de la página. Este contenedor ajusta automáticamente su ancho según el dispositivo en el que se visualiza la página, proporcionando así un diseño responsivo.

En resumen, el uso de *div class="container"* indica que el formulario y cualquier contenido dentro de este div estarán contenidos y se ajustarán adecuadamente dentro de un contenedor responsivo según las reglas de diseño proporcionadas por Bootstrap. Este enfoque ayuda a que la página se vea bien en diferentes tamaños de pantalla y dispositivos.

### Tercer version - añadiendo el submit botton

Añadiremos algunas clases de Bootstrap para mejorar la apariencia del *boton*:

```html
    <div class="container">
        <h2 class="titulo-1">Llena el Formulario</h2>
        <br> 👈
        <form action="" class="form-register">
            {{ register_form.username.label()}}
            {{ register_form.username(class="form-control", placeholder=" tu usuario")}}
            <br>
            {{ register_form.submit(class="btn btn-lg btn-block btn-primary" )}} 👈
        </form>
    </div>
```
- br: para un bracket espacio adicional

![](https://i.imgur.com/Rj3jScj.png)

### Version Final - añadiendo estilos adicionales, y los otros campos

```css
.container{
    padding-left: 100px;
    padding-right: 100px;
}

.form-register{
    color: rgb(122, 122, 155);
}

.form-register-field{
    padding-top: 5px; 👈 para que no se vea tan apeñuscado 
}

.titulo-1{
    text-align: center;
}
```

```html
    <div class="container">
        <h2 class="titulo-1">Llena el Formulario</h2>
        <br>
        <form action="" class="form-register">
            <div class="form-register-field">{{ register_form.username.label()}}</div>
            {{ register_form.username(class="form-control", placeholder=" tu usuario")}}

            <div class="form-register-field">{{ register_form.email_address.label()}}</div>
            {{ register_form.email_address(class="form-control", placeholder=" tu correo")}}

            <div class="form-register-field">{{ register_form.password1.label()}}</div>
            {{ register_form.password1(class="form-control", placeholder="contraseña")}}

            <div class="form-register-field">{{ register_form.password2.label()}}</div>
            {{ register_form.password2(class="form-control", placeholder="confirmar contraseña")}}

            <br>
            {{ register_form.submit(class="btn btn-lg btn-block btn-primary" )}}
        </form>
    </div>
```

![](https://i.imgur.com/YFoGv5b.png)

