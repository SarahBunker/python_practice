list1 = [1, 2, 3, 4, 5]
list2 = ["banana", "apricot", "melon", "apples", "mangos", "strawberries", "oranges", "melon"]

# extend mutating method
list1.extend(list2)
print (list1)

# add single item?
list2.append("cherry")
print(list2)

# add item to middle of list
# index place to insert
# value to insert

list1.insert(0, "start")
print(list1)

# removing value from list

list2.remove("banana")
print(list2)

# remove all values from list
list2.clear()
print(list2)

# get index of value
index = list1.index("melon")
print(index)

# count occurances of value
print(list1.count("melon"))

# sort list
# mutating
list3 = [4, 3, 5, 1, 2]
list3.sort()
print(list3)

# sort list in reverse
# mutating
list3.reverse()
print(list3)

# can also sort lists with words
list4 = ["Me", "Myself", "I"]
list4.sort()
print(list4)

# duplicate list
list5 = list3.copy()
print(list5 == list3)

# remove last value
# mutating
print(list3)
item = list3.pop()
print(list3)
print(item)

# can use remove
list3.remove(2)
print(list3)

# or the index
list3.pop(1)
print(list3)

# another way using del and the index
del list3[0]
print(list3)

# delete list
# different from .clear() which empties list
# removes reference to list
del list3
list3 = []
print(list3)

