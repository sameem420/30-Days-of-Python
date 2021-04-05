my_data = ["SaM", 22, "BSCS"]

random_list = ["Justin", "John", "Matt"]

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

new_fruits = fruits.copy()

my_data.append("GCUF")
my_data.insert(4, "PK")
# printing list after adding some data
print(my_data)

random_list.remove("Matt")
# printing list after removing data
print(random_list)

print(fruits)

fruits.pop()
fruits.pop(4)
# printing list after removing data
print(fruits)

# length of the list
print(len(fruits))

# deleting a complete list
del random_list

# emptying a list 
fruits.clear()

print(fruits)

print(new_fruits)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

keys = thisdict.keys()
# printing keys of dictionary
print(keys)

values = thisdict.values()
# printing keys of dictionary
print(values)

items = thisdict.items()
# printing all items of dictionary
print(items)

thisdict.popitem()
# printing after removing
print(thisdict)

# adding new key named year with value
thisdict.update({"year": 2020})

print(thisdict)

# removing key-value from dictionary
del thisdict["model"]

print(thisdict)

mytuple = ("apple", "banana", "cherry")
# destructring - separating values into each variable
(green, yellow, red) = mytuple
print(mytuple)

fruits_set = {"apple", "banana", "cherry"}

fruits_set.add("orange")

print(fruits_set)

fruits_set.discard("banana")

print(fruits_set)