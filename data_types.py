"""
Booleans are capitalalized
"""

filled_cart = True
print(type(filled_cart))


"""
implicit data type conversion
"""

plates = 5 / 2
print(type(plates)) # float type

forks = 4 + 5.0
print(type(forks)) # float type

"""
explict conversion

- input is always a string
"""

note = input("note: ")
print (type(note)) # string
number = input("number: ")
print (type(number))
#convert to int
number = int(input("number again: "))
print (type(number))

"""
concatenation
""""

# can add two strings
print("Welcome " + "John")

# no automatic conversion when adding numbers and strings
print(3 + int("3"))