# 7. Model Relations

En este modulo crearemos mas relaciones en las bases de datos. Pero antes, redistribuiremos las rutas para pasar de esto:

![](https://i.imgur.com/F2HVYMn.png)

A esto:

![](https://i.imgur.com/5G85l9C.png)

Crearemos una nueva clase para los datos de un usuario. Donde los campos username and email seran unicos, password, y una cantidad de dinero disponible para que compren. No almacenaremos passwords en plain text, por lo que reservaremos suficiente espacio.

```py
class User():
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    wallet = db.Column(db.Float(), nullable=False, default=1000)
```

## Haciendo Consulta a la base de datos

Haremos un query de insercion para un Item, teniendo en cuenta en el modulo anterior modificamos la estructura del proyecto. Desde el *Interprete de Python*, y habiendo activado el ambiente virtual obviamente:

```py
from market.models import Item, User
from market import app, db
item = Item(producto = 'sal', barcode = 'K12XFA-2', precio = '2.55')

with app.app_context():
    db.session.add(item)
    db.session.commit()
```

Y para consultar:

```py
with app.app_context():
    consulta = Item.query.all()
consulta
```

![](https://i.imgur.com/SyavXtJ.png)

Y haremos el mismo ejercicio para crear un usuario. Sin embargo cuando se intenta insertar un *User*, aparece un error que la tabla no esta creada. 

En realidad fue muy dificil encontrar una explicacion clara referente a como crear una table de manera individual. Por lo que me guiare por el instructor, quien va a borrar todo y empezar desde cero.

### Empezando la BD desde cero

Borrando la base de datos

```py
with app.app_context():
    db.drop_all()
```

Aprovecharemos para agregar las relaciones en la base de datos:

```py
class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    wallet = db.Column(db.Float(), nullable=False, default=1000)

    items = db.relationship('Item', backref='owned_user', lazy=True)
```

- items: Relación uno a muchos con la clase Item. Establece una relación entre la clase User y la clase Item. El argumento backref proporciona un atributo inverso en la clase Item para acceder fácilmente al usuario propietario.

#### Explicando backref

En SQLAlchemy, el argumento backref se utiliza para establecer automáticamente una relación inversa desde el otro lado de una relación. En tu caso, has establecido una relación entre la clase User y la clase Item utilizando backref='owned_user'.

Esto significa que, una vez que tienes un objeto User, puedes acceder a los elementos relacionados a través del atributo items. Además, debido a backref, tendrás un atributo inverso en la clase Item que te permite acceder al usuario propietario. En tu caso, este atributo inverso se llama owned_user.

Aquí hay un ejemplo para ilustrar cómo se puede usar:

```py
# Crear un usuario
usuario = User(username='ejemplo', email_address='ejemplo@email.com', password_hash='hashed_password')

# Crear un ítem relacionado
item = Item(nombre='Ejemplo Item', owned_user=usuario)

# Acceder a los elementos de un usuario
elementos_usuario = usuario.items

# Acceder al usuario propietario de un ítem
usuario_propietario = item.owned_user
```

En este ejemplo, después de crear un usuario (usuario), puedes acceder a los elementos relacionados con ese usuario a través del atributo items. También, si ya tienes un objeto Item (item), puedes acceder al usuario propietario a través del atributo inverso owned_user.

Este tipo de relación bidireccional puede *ser útil para navegar fácilmente entre objetos* relacionados en ambas direcciones.

#### Explicando lazy

En la relación, has especificado lazy=True en el argumento relationship. Cuando se utiliza lazy=True, SQLAlchemy carga los elementos relacionados solo cuando se accede a ellos por primera vez. Esto es conocido como "carga perezosa" o "lazy loading". Significa que, cuando obtienes un objeto User, los elementos relacionados (los elementos que pertenecen a ese usuario) no se cargarán de inmediato desde la base de datos. En su lugar, se cargarán solo cuando intentes acceder a ellos por primera vez.

Aquí hay un ejemplo de cómo podrías usar esta relación lazy loading:

```py
# Crear un usuario
usuario = User(username='ejemplo', email_address='ejemplo@email.com', password_hash='hashed_password')

# Agregar un elemento a la lista de elementos relacionados (esto no carga aún los elementos desde la base de datos)
item = Item(nombre='Ejemplo Item', owned_user=usuario)

# Ahora, cuando intentas acceder a los elementos, se cargan desde la base de datos
elementos_usuario = usuario.items
```

En este ejemplo, la relación items no se carga inmediatamente cuando se crea el usuario. Solo se carga cuando intentas acceder a la propiedad items por primera vez.

Este enfoque puede ser beneficioso en situaciones en las que no siempre necesitas cargar todos los elementos relacionados y deseas evitar la sobrecarga de recursos. Sin embargo, también puede haber casos en los que prefieras cargar los elementos relacionados de inmediato para evitar consultas adicionales a la base de datos. La elección entre lazy loading y eager loading depende de los requisitos específicos de tu aplicación.

#### Creando neuvamente todo

Incluidas las relaciones

```py
with app.app_context():
    db.create_all()
```
Y empezamos añadiedno un par de Items, observe no agregamos el campo de owner todavia.

```py
item = Item(producto='chocolate', barcode='C2002-2022-ha24', precio='13.24')
```
De igual manera creamos un par de usuarios

```py
 user = User(username='chambimbe', email_address='iguana@abc.com', password_hash='Qwwdefg1234')
```

#### Practicando SqlAlchemy

Por ejemplo si queremos saber cual es el precio del producto que es igual a *sal*:

![](https://i.imgur.com/95NNOet.png)

Ahora asignamermos el producto *sal* al usuario cuyo username es *chambimbe*. Empezaremos de nuevo:

![](https://i.imgur.com/wJCrhm9.png)

Y ahora asignaremos el producto *azucar* al usuario cuyo nombre es *maxr*:

![](https://i.imgur.com/yRroEbS.png)

Y con esto hemos terminado la session

