# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries



# Create Dictionary
person = {
    'first_name': 'Tush',
    'last_name': 'Dave',
    'age': 22
}

# Use constructor
# person2 = dict(first_name='Tush', last_name='Dave', age=22)

# Get a value
print(person['first_name'])

print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dictionary keys
print(person.keys())

# Get dictionary items
print(person.items())

# Copy a dictionary
person2 = person.copy() # Similar to spread operator in js
person2['city'] = 'San Francisco'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])


# print(person, type(person))