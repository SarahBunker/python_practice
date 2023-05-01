"""
Are lists the same as arrays?
- Lists are part of Python
- Arrays are part of NumPy package
"""

countries = ["United Kingdom", "USA", "Gana", "Nigeria", "Switzerland"]
print(countries)
# print from index 1 to the end
print(countries[1:])

# print range
print(countries[1:3])
# the range is inclusive of the first number and exclusive of the second index

# type of list
print(type(countries))
# <class 'list'>

# negative indexes
print(countries[-1]) # Switzerland

# length of list
print(len(countries))

"""
use list constructor
"""

countries2 = list(("United Kingdom", "Nigeria", 34, False))

print(type(countries))
print(type(countries2))