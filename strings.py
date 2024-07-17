# Strings in python are surrounded by either single or double quotation marks. 
# Let's look at string formatting and some string methods

name = 'Tush'
age = 22

# String Concatenation - to insert  variable into a string
# print('Hello, my name is ' + name + ' and I am ' + str(age) + ' years old.')
# str(age) - convert age to string - casting


# String Formatting

# Arguments by position
# print('My name is {name} and I am {age} years old.'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'My name is {name} and I am {age} years old.')

# String Methods

s = 'hello world'

# Capitalize String
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# Is all upper
print(s.isupper())
