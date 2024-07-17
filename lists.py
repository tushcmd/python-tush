# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# # Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# print(numbers)
# print(fruits)
# print(numbers2)

# Get a single value
print(fruits[1])

# Get length of list
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove with pop
fruits.pop(2)

# Reverse
fruits.reverse()

# Sort
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Change a value
fruits[0] = 'Blueberries'

# Clear
fruits.clear()

print(fruits)