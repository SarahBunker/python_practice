'''
second param is r for read only
could also do w for write only
or a for appending to end of file
or r+ read and write both

make sure to close any file after opening it
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