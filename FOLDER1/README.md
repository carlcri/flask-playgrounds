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
