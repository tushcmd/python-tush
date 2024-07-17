# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1  # int

# y = 2.5  # float

# name = 'Tush'  # str

# is_cool = True  # bool


# # More from codieum
# x = 1j  # complex
# x = ["a", "b", "c"]  # list
# x = ("a", "b", "c")  # tuple
# x = range(6)  # range
# x = {"a": 1, "b": 2}  # dict
# x = {"a", "b", "c"}  # set
# x = frozenset({"a", "b", "c"})  # frozenset

# x = b"Hello"  # bytes
# x = bytearray(5)  # bytearray
# x = memoryview(bytes(5))  # memoryview

# multiple assignment
x, y, is_cool, name = (1, 2.5, True, 'Tush')

# print(x, y, is_cool, name, a)


# Basic math 

a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
