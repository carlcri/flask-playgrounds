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

Igualmente añadimos la logica para crear un flask de registro exitoso de usuario:

```py
with app.app_context():
    db.session.add(new_user)
    db.session.commit()
    flash(f'usuario: {user_name} creado con exito', category="success") 👈
```