"""
tuples are similar to lists
- immutable

"""

three_numbers = (1, 2, 3)

print(three_numbers)

# Bracket access
print(three_numbers[0])

# Immutable, following would cause error
# three_numbers[1] = 23

# allows repetition 
three_numbers = (1, 2, 3, 1)

# length
print(len(three_numbers))

# type
print(type(three_numbers)) # <class 'tuple'>

# can have other data types
stuff = (True, "a string of characters", 3.0)

print(stuff)

# tuples good for data you want to be immutable like cordinates