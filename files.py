# Python has functions for creating, reading, updating, and deleting files.

# Open a file for reading and writing
# with open('test.txt', mode='r+') as file:
#     content = file.read()
#     print(content)

myFile = open('test.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write('\nI love JavaScript')
myFile.close()


# Append to file
myFile = open('test.txt', 'a')
myFile.write('\nI also like C')
myFile.close()

# Read from file
myFile = open('test.txt', 'r+')
text = myFile.read(100)
print(text)
myFile.close()