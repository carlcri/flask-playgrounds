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

    
    