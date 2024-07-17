# A Tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.
 
# Create Tuple
# numbers = (1, 2, 3, 4, 5)
fruits = ('Apples', 'Oranges', 'Grapes', 'Pears')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes', 'Pears'))

# print(numbers, fruits, fruits2)

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get a single value
print(fruits[1])

# Cannot change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# print(fruits2) # NameError: name 'fruits2' is not defined


# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. 
# No duplicate members.


# Create Set
fruits_set = {'Apples', 'Oranges', 'Grapes', 'Pears'}
# fruits_set = set(('Apples', 'Oranges', 'Grapes', 'Pears'))    # same as above

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Mangos')

# Remove from set
fruits_set.remove('Grapes')
fruits_set.discard('Pears')

# Clear set
fruits_set.clear()

# Delete
del fruits_set


print(fruits_set)
