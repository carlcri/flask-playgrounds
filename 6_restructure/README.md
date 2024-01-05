# Flask Bootstrap

En este modulo hay dos rutas: home and test. En donde en cada una se renderiza una navbar de diseño diferente. 

Por ejemplo, el template test hereda de base1, quien a su vez hereda de bootstrap/base.html.

Tomado del curso: https://www.youtube.com/watch?v=Qr4QMBUPxWo&t=3669s 

Flask-Bootstrap es una extensión (o paquete de Python) que proporciona integración entre Flask (un marco de desarrollo web en Python) y Bootstrap (un marco de diseño para interfaces web). Permite utilizar las funcionalidades y estilos de Bootstrap de manera más fácil en una aplicación Flask.

Flask-Bootstrap facilita la creación de aplicaciones web con Flask que tienen una apariencia atractiva y moderna gracias a las capacidades de diseño y estilo que ofrece Bootstrap.

Algunas de las características de Flask-Bootstrap pueden incluir:

1. Formularios y Campos: Proporciona extensiones para crear formularios de manera sencilla y aprovechar los estilos y funcionalidades de Bootstrap.

2. Plantillas y Layouts: Ofrece plantillas base y layouts predefinidos que siguen las convenciones de diseño de Bootstrap.

3. Componentes de Bootstrap: Permite integrar fácilmente componentes de Bootstrap, como menús desplegables, botones, paneles, entre otros.

4. Integración con Jinja2: Flask-Bootstrap se integra sin problemas con el motor de plantillas Jinja2 que Flask utiliza de manera predeterminada.

Al usar Flask-Bootstrap, los desarrolladores pueden agilizar el proceso de creación de aplicaciones web al aprovechar las funcionalidades y estilos de Bootstrap dentro de sus proyectos Flask.

## Uso Basico

To get started, the first step is to import and load the extension:

```py
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app
```
After loading, new templates are available to derive from in your templates(base.html que veremos mas adelante).

## Bloques

Aprenderas a usar los bloques:

![](https://i.imgur.com/7gvFdgN.png)

- fijate el bloque *navbar* debe estar contenido en el bloque *body*, tal y como ocurre en *base.html* y *base1.html*

- el bloque *scripts* esta contenido dentro del bloque *body*. Estos son Java Scripts

## Usando glyphicon

*navbar.hmtl*

Los "glyphicons" eran una colección de iconos vectoriales que podían ser utilizados en tu aplicación web. Estos iconos eran representaciones gráficas de objetos, acciones y conceptos comunes, como por ejemplo una lupa para buscar, un sobre para correo, un corazón para "me gusta", etc.

Aqui un icono de fueguito en el boton Submit:

![](https://i.imgur.com/8D2owiC.png)

## Archivo de estilos

### Ruta home

En el bloque de *styles* dentro de *base.html* indicamos la ubicacion de nuestro archivo de stilos, sin sobreescribir, con la sentencia **super**

```html
{% block styles %}
    {{super()}}
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}">
{% endblock %}
```

### ruta test

En el base1.html se indican el archivo de estilos:

```html
        {% block styles %}
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        {% endblock %}
```

Y a su vez en el template test, le indicamos nuestro archivo de estilos, sin sobreescribir lo que ya venia con *super*:

```html
{% block styles %}
    {{super()}}
    <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}">
{% endblock %}
```
## Lecturas

Template Designer Documentation

https://jinja.palletsprojects.com/en/3.1.x/templates/#super-blocks

# Databases

Modificaremos la ruta *home* para renderizar una tabla para mostrar una lista de compras:

```py
@app.route('/')
@app.route('/home')
def home():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 1, 'precio unitario': 14}
    ]
    return render_template('home.html', items=items) 
```

y el el template:

```html
    <div class="main-table">
        <table class="table table-hover">
            <thead>
                <tr class="aux">
                    <th>id</th>
                    <th>producto</th>
                    <th>cantidad</th>
                    <th>precio unitario</th>
                    <th>subtotal</th>
                </tr>
            </thead>
            <tbody>
                {% for item in items %}
                <tr>
                    <td>{{ item.id }}</td>
                    <td>{{ item.producto }}</td>
                    <td>{{ item.cantidad }}</td> 👈
                    <td>{{ item["precio unitario"] }}</td> 👈
                    <td>{{ item.cantidad * item["precio unitario"] }}</td> 👈
                </tr>
                {% endfor%}
            </tbody>
        </table>      
    </div>
```
Note como se accede a un elemento por dos tipos de jinja sintaxis:

```html
<td>{{ item.cantidad }}</td> 
...
...
<td>{{ item["precio unitario"] }}</td> 
```
Y dando algunos estilos para una nueva clase llamada *main-table*

```css
.main-table{
    padding-left: 20px;
    padding-right: 40px;
}
```

### Configurando una base de datos SQlite3

Lo hecho hasta ahora esta bien, pero que tal si empezamos a usar una base de datos de verdad, y manipular las tablas como si fueran clases de python:

- agregar un nueva dependencia a requirementes: *flask-sqlalchemy*

- inicializar la base de datos: 

```py
db = SQLAlchemy(app)
```

- configure the SQLite database, relative to the app instance folder. URI stands for *Uniform Resorce Identifier*, nuestra base de datos se llamara *market.db*

```py
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_base.db"
```

- Definir una tabla SQL como una clase:

```py
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    producto = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    precio = db.Column(db.Float(), nullable=False)
```

### Creando la Base de datos

Desde el interprete de python:

```py
from main import db, app
with app.app_context():
    db.create_all()
```

Si esto esta bien debe aparecer la base de datos dentro del folder instance:

![](https://i.imgur.com/A9TQ0zM.png)

Para empezar agregar filas a la tabla, dentro del mismo interprete de python, se hace de esta manera:

```py
from main import Item
item = Item(producto = 'azucar', barcode = 'A12FA-1', precio = '10.50')

with app.app_context():
    db.session.add(item)
    db.session.commit()
```
En este punto deberia haber un registro en *data_base.db*

### Haciendo consultas a la base de datos 

Desde el interprete de python, y ya con algunas filas agregadas, hacemos una consulta:

![](https://i.imgur.com/Rr7K5BS.png)

Si quisieramos mejorar el codigo, modificamos la clase *Items* modificando un *magic method* llamado *repr*:

- Volvemos a importar todo:

```py
from main import db, Item, app

with app.app_context():
    Item.query.all()
```
Y ahora si es mas legible:

![](https://i.imgur.com/zNs7PQA.png)

#### Realizando algunas pruebas

Guardemolo en una variable:

```py
with app.app_context():
    consulta = Item.query.all()
```

![](https://i.imgur.com/jzyHnPz.png)

### Implementando la consulta en la ruta:

```py
@app.route('/')
@app.route('/home')
def home():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 2, 'precio unitario': 14}
    ]
    consulta = Item.query.all() 👈

    return render_template('home.html', items=items, consulta=consulta) 
```

Nota que he implementado algunos estilos, como el color del titulo y el padding:

![](https://i.imgur.com/Abh7b2n.png)

### Otras consultas

Usando la funcion *filer_by*

```py
@app.route('/')
@app.route('/home')
def home():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 2, 'precio unitario': 14}
    ]
    consulta = Item.query.filter_by(precio=10.5) 👈
    for item in consulta:
        click.echo(click.style(f'item_id:{item.id} precio:{item.precio}', fg='green')) 👈
        
    consulta = Item.query.all()

    return render_template('home.html', items=items, consulta=consulta) 
```

Resultado:

![](https://i.imgur.com/IN4Ofa5.png)

https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

#### DB Browser for SQLite

DB Browser for SQLite (DB4S) is a high quality, visual, open source tool to create, design, and edit database files compatible with SQLite.

Se descargo como una AppImage, click derecho para darle permisos de ejecucion. Pero no funciono.

## Reestructuracion del Proyecto

Por ahora todo el codigo esta en el archivo main.py, sin embargo, vamos por ejemplo a mover las clases a un nuevo archivo, llamado *models.py*:

```py
from flask_sqlalchemy import SQLAlchemy👈

db = SQLAlchemy(app)👈

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    producto = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    precio = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'{self.producto}'
```
- Fue necesario esas dos lineas de codigo, y sin embargo, ahora mismo hay que importar *app*

- para importar *app* hay que hacerlo de *main.py*, pero a su vez en *main.py*, hay que importar Item, y terminariamso con algo que se llama *circular imports* que es prohibido en Python. 😨

Y de la misma manera, las rutas las moveremos a *routes.py*


```py
@app.route('/')
@app.route('/home')
def home():
    items = [
        {'id':1, 'producto': 'cebolla', 'cantidad': 10, 'precio unitario': 2},
        {'id':2, 'producto': 'tomate', 'cantidad': 4, 'precio unitario': 5},
        {'id':3, 'producto': 'pechuga', 'cantidad': 2, 'precio unitario': 14}
    ]
    consulta = Item.query.filter_by(precio=10.5)
    for item in consulta:
        click.echo(click.style(f'item_id:{item.id} precio:{item.precio}', fg='green'))
        
    consulta = Item.query.all()

    return render_template('home.html', items=items, consulta=consulta) 


@app.route('/test')
def test():
    return render_template('test.html')
```

La estructura estara quedando parecida a:

![](https://i.imgur.com/ywaUkMC.png)


### Solucionando las importaciones circulares

Python soluciona este tema con algo que se llama *packages*. De esta forma vamos a empaquetar nuestra aplicacion dentro de un nuevo directorio. En otros ejercicios la hemos llamado *app*, la podemos llamar para este ejercicio *market* o el nombre que queramos.

- Moveremos todo a este nuevo directorio: templates, routes and models. 

- Apareceran errores de compilacion entre otros que iremos solucionando

- Desde el main.py importaremos todo lo que se necesite

### Configurando el archivo __init__

Cada paquete en python contendra un archivo especial llamado: 

```py
__init__
```
Cuando se importa el paquete, se ejecutara el contenido de este archivo.

#### Problemas 😫😫

El proceso no es muy straight-forward, en realidad me toco deshacer todos los cambios, e ir implementando poco a poco los cambios.

- creando el archivo init.py con una configuracion basica:

```py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
```

- En el main.py importo desde el modulo: *from market import app*

