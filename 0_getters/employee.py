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





    

        