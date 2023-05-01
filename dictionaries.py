"""
hashtable is a subset of dictionary
dictionaries are mutable
keys must be unique
"""

my_dict = {
  "name": "Tim",
  "age": 34,
  "qualification": "college degree"
}

print(my_dict)

# getting values
print(my_dict["name"])

# duplicates not allowed
# second value is kept
my_dict = {
  "name": "Tim",
  "name": "John",
  "age": 34,
  "qualification": "college degree"
}

print(my_dict)

# length of dictionary
print(len(my_dict))

# can add list as key
my_dict = {
  "name": "Tim",
  "name": "John",
  "age": 34,
  "qualification": "college degree",
  "friends": ["Peter", "Paul", "Jim"]
}

print(my_dict)

# type

print(type(my_dict)) # <class 'dict'>