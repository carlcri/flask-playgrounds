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

