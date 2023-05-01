'''
second param is r for read only
could also do w for write only
or a for appending to end of file
or r+ read and write both

make sure to close any file after opening it
'''

# setting up file

file = open("countries.txt", "w")
file.write("Ghana\nArgentina\nSpain")

file.close()

'''
examples reading files
'''

file = open("countries.txt", "r")

print(file.readable()) # .readable() returns boolean if readable
print(file.readline()) # prints the first line with new line caracter
print(file.readline()) # prints the next line

file.close()

file = open("countries.txt", "r")

# print(file.readlines()) # prints file in list with items separated by \n
print(file.readlines()[0])

file.close()

'''
Writing to files
- completely replaces file
'''

file = open("countries.txt", "w")
file.write("This is the new text")

file.close()

# creating a new file

file = open("country.txt", "w")
file.write("This is a new file created")

file.close()

'''
Appending to file
'''

file = open("country.txt", "a")
file.write("\nThis is a new line")

file.close()

'''
Can create python files
'''
file = open("newpy.py", "w")
file.write("print('This is a new file')")

file.close()