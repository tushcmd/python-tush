# A function is a block of code which only runs when it is called. 
# In Python, we do not use parentheses and curly brackets, we use a colon, indentation with tabs or spaces


# Create function
def sayHello(name='Tush'):
    print(f'Hello {name}')

# sayHello() # logger

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total


# num = getSum(2, 3)

# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have 
# one expression. Very similar to JS arrow functions


getSum2 = lambda num1, num2: num1 + num2

num = getSum2(2, 3)

print(num)
