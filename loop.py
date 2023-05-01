"""
While loop
"""

i = 1
while i < 6:
  print(i)
  i += 1


print()
"""
For loop
- loop through item in collection
- list
- characters in word
- dictionary
"""

for letter in "Hello":
  print(letter)

print()

mylist = ['ji', 'ju', 'jo']

for item in mylist:
  print(item)

print()

myDict = {
  "name": "Sarah",
  "age": 30
}

for key in myDict:
  print(key, myDict[key])

"""
Break statement
- exit loop early
"""

for value in mylist:
  if value == 'ju':
    break
  print(value)


"""
using range
one input 
- numbers from 0 to number provided exclusive
two inputs
- numbers from first number inclusive to second number exclusive

"""

for x in range(5):
  print(x)
# prints 0 1 2 3 4
# 5 not included

for x in range(3, 5):
  print(x)
# prints 3 4

"""
else statement with for loop
- printed after loop is down
"""

for x in range(3, 5):
  print(x)
else:
  print("Finished Looping")
# prints 3 4