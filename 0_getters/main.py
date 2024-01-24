#from employee import Employee
#from truck import Truck


from market.user import User

if __name__ == '__main__':
    user = User('Oscar')
    user.password = 'la gata antonia'

    print(user.password)

#    print(user.password_hash)
    
    User.password = '123'
    
    user = User(username='Pedro', password_hash='123')
   









