# Practicando Query argumets and post method

Basado en: *https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask*


## Using Query Arguments

```py
@app.route('/query-example')
def query_example():

    name = request.args.get('name')
    lastname = request.args.get('lastname')
    age = request.args.get('age')

    return '''
              <h2>my name is: {}</h2>
              <h2>my last name is: {}</h2>
              <h2>I am {} years old'''.format(name, lastname, age)
```

name, lastname y age son *argumentos tipo querry*: ingresa las siguientes URLs, en donde si no colocas alguno de los argumentos, retornara NONE.

*http://127.0.0.1:5000/query-example?name=oscar&lastname=perez&age=20*
*http://127.0.0.1:5000/query-example?lastname=perez&age=20*

![](https://i.imgur.com/oAL3jyR.png)

### Mejorando el script

No es buena idea mexclar en el mismo archivo codigo *python* y *html*. Podriamos entonces remplazarlo con una sola linea de codigo:

```py
@app.route('/query-example')
def query_example():

    name = request.args.get('name')
    lastname = request.args.get('lastname')
    age = request.args.get('age')

    return f'my name is {name} {lastname}, and I am {age} years old' 👈
```

### Colocando el codigo html en otro archivo:

- Importo *render template*, y devuelvo un template en lugar de texto plano:

```py
    return render_template('query_example.html', **context)👈
```
*context* es un diccionario.

```html
<h2> my name is {{name}} {{lastname}}, and I am {{age}} years old</h2>
```

### Primera implementacion basica de GET and POST

Me dio mucha tarea, pero finalmente lo pude lograr. 

Creo una nueva ruta *form-example* donde se recibe un formulario muy basico que pide tu nombre:

![](https://i.imgur.com/2RXNiU3.png)

```py
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():

    if request.method == 'POST':
        name = request.form.get('name')
        return f'Your name is {name}'
    
    return render_template('form_example.html')
```

Y al momento de enviarlo, sobre la misma ruta

![](https://i.imgur.com/Odq1nSg.png)

Y el codigo *html* de la forma:

```html
    <form action = "http://127.0.0.1:5000/form-example" method="post">
        <label for="name">
            <span>Nombre</span>
            <input type="text" id="name" name="name">
        </label>
        <input type="submit" value="Enviar">
    </form>
```

### Implementando estructuras de control 

Puedes utilizar la sintaxis de Jinja2, que es el motor de plantillas que Flask utiliza por defecto:

```html
    {% if not name %}
        <form action = "http://127.0.0.1:5000/form-example" method="post">
            <h3>Llena el formulario</h3>
            <label for="name">
                <span>Nombre</span>
                <input type="text" id="name" name="name">
            </label>
            <input type="submit" value="Enviar">
        </form>
    {% else %}
        <p>Welcome: {{name}}</p> 👈
    {% endif %}
```

Y en el main.py, fijate estamos renderizando el mismo template para los dos metodos:

```py
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():

    if request.method == 'POST':
        name = request.form.get('name')
        context = {
            'name': name
            }

        return render_template('form_example.html', **context) 👈

    return render_template('form_example.html')
```