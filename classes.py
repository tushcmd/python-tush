# A class is like a blueprint for creating objects. An object has properties and methods
# (functions) associated with it. Almost everything in Python is an object
 

# Create class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    # Methods
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1
        # return f'Happy {self.age}th birthday!'
        
# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
                
# Init user object
tush = User('Tush', 'tush@gmail.com', 22)

# Init customer object
janet = Customer('Janet Mimo', 'janet@gmail.com', 24)

janet.set_balance(500)
print(janet.greeting())

tush.has_birthday()
print(tush.greeting())


