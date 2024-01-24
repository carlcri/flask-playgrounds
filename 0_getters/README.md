# Repaso POO

https://realpython.com/python-property/

https://realpython.com/python-getter-setter/

## What Are Getter and Setter Methods?

Getter and setter methods are quite popular in many object-oriented programming languages. So, it’s pretty likely that you’ve heard about them already. As a rough definition, you can say that getters and setters are:

Getter: A method that allows you to access an attribute in a given class
Setter: A method that allows you to set or mutate the value of an attribute in a class

Por ejemplo aqui declare la clase *Truck*, donde el atributo *_model* es privado.

```py
class Truck:
    def __init__(self, model=None) -> None:
        self._model = model
    
    def get_model(self):
        print('returns model')
        return self._model
    
    def set_model(self, model):
        self._model = model
```

Si instanciamos un objeto de tipo Truck, y usamos los metodos para asignar y obtener el modelo:

```py
truck = Truck()
truck.set_model('Dodge')
print(truck.get_model())
```

Obtenemos el resultado esperado:

    returns model
    Dodge

## Usando la funcion property

La función *property* en Python se utiliza para crear propiedades de clase. Una propiedad permite que los métodos de una clase se utilicen como si fueran atributos. En otras palabras, proporciona una forma de encapsular la lógica de acceso y modificación de un atributo de manera más controlada.

La función property toma hasta tres funciones como argumentos: *fget* (función de obtención), *fset* (función de establecimiento) y *fdel* (función de eliminación). Estas funciones definen el comportamiento de la propiedad cuando se accede a ella, se le asigna un valor o se elimina, respectivamente.

```py
model = property(fget=get_model,
                fset=set_model,
                doc='manages model')
```
Observa que el atributo *_model* es diferente de *model*. Si bien pueden tener nombres parecidos, no deben ser iguales. 

```py
truck = Truck()
truck.model = 'Ford'
print(truck.model)
```
Y haria exactamente lo mismo:

    returns model
    Dodge

### Ejemplo 2

```py
class Employee:
    def __init__(self, name, lastname='', birth_date='') -> None:
        self.name = name
        self.lastname = lastname
        self.birth_date = birth_date

    def get_name(self):
        print('returns name')
        return self.name
    
    def set_name(self, name):
        self.name = name.upper()

    nombre = property(fget=get_name, fset=set_name, doc='manages name')

    def get_lastname(self):
        print('returns lastname')
        return self.lastname
    
    def set_lastname(self, lastname):
        self.lastname = lastname.upper()

    apellido = property(fget=get_lastname, fset=set_lastname, doc='manages lastname')
```

Tenemos una clase con tres atributos: name, lastname y birthdate. Observa que las funciones definidas con *property* se llaman *nombre* y *apellido*.

# Using property() as a Decorator

The decorator syntax consists of placing the name of the decorator function with a leading @ symbol right before the definition of the function you want to decorate.

Para colocar un ejemplo practico de porque y como usar esta encapsulacion, suponga que queremos guardar el *password* de forma encriptada usando el algoritmo *rsa*, donde se maneja una llave publica y una llave privada. 

```python
from market import encrypt_data, decrypt_data

class User():
    def __init__(self, username, password_hash=None) -> None:
        self.username = username
        self.password_hash = password_hash
    

    @property
    def password(self):
        print('get password')
        return decrypt_data(self.password_hash)
    

    @password.setter
    def password(self, value):
        print('Encrypting Password')
        self.password_hash = encrypt_data(value)
```

El primer paso seria codificar un password con una llave publica y luego decodificarlo con la llave privada.  

```py
from market.user import User

if __name__ == '__main__':
    user = User('Oscar')
    user.password = 'la gata antonia' 👈

    print(user.password)
```

https://pythonistaplanet.com/cryptography/

