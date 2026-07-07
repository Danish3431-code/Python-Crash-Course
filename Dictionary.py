# DICTIONARY IN PYTHON:
# A dictionary is a collection of key-value pairs where each key is unique and is used to access its value.

# A dictionary stores data in key:value pairs.

# Example:
# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student"
# }
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student'}

# idea:
# name -> Danish
# age -> 25
# occupation -> student

# Memory Trick:
# key->Label
# value->Data

# FEATURES:
# 1) Key-value pairs.
# 2) ordered.
# 3) changeable(mutable).
# 4) No duplicate keys.
# 5) values can be duplicated.

# CREATE A DICTIONARY:

# Method:1

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student"
# }
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student'}

# Method:2

# student=dict(name="Danish", age=25, occupation="student")
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student'}


# HOW TO ACCESS VALUES IN DICTIONARY:
# use the key to access it's values.

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student"
# }
# print(student["name"])#Danish
# print(student["age"])#25
# print(student["occupation"])#student

# Memory Trick:
# Dictioanry = key -> value

# MOST IMPORTANT METHODS:-

# METHOD                PURPOSE

# key()                   Get all keys.
# values()                Get all values.
# items()                 Get key-value pairs.
# get()                   safely get a value.
# update()                update dictionary.
# pop()                   Remove an item.
# clear()                 remove all items.
# copy()                  copy dictionary.     

# 1)keys():

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"Student"
# }
# print(student.keys())#dict_keys(['name', 'age', 'occupation'])

# logic
# Returns only the key(labels)

# 2)values():

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
#     "city":"Gujranwala"
# }
# print(student.values())#dict_values(['Danish', 25, 'student', 'Gujranwala'])

# logic
# Returns only the values(data).

# 3) items():

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
#     "city":"Gujranwala"
# }
# print(student.items())#dict_items([('name', 'Danish'), ('age', 25), ('occupation', 'student'), ('city', 'Gujranwala')])

# logic
# Returns both key and value together.

# 4)get():

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
#     "city":"Gujranwala"
# }
# print(student.get("name"))#Danish
# print(student.get("age"))#25
# print(student.get("occupation"))#student
# print(student.get("city"))#Gujranwala

# logic
# Gets value using the key.

# memory Trick:
# get("name")
#        |
#     Danish

# 5)Add item:

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
# }
# student["city"]="Gujranwala"
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student', 'city': 'Gujranwala'}

# logic
# New key + value added

# 6)Modify Item:

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
#     "city":"Gujranwala"
# }
# print(student) #{'name': 'Danish', 'age': 25, 'occupation': 'student', 'city': 'Gujranwala'}

# student["age"]=26
# print(student)#{'name': 'Danish', 'age': 26, 'occupation': 'student', 'city': 'Gujranwala'}

# logic
# existing value changed.

# Memory trick:
# 25->26

# 7)pop():

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
#     "city":"Gujranwala"
# }
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student', 'city': 'Gujranwala'}
# print(student.pop("city"))#Gujranwala
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student'}

# logic 
# removes a specific key -value pair and show it as an output.

# memory:
# pop("city")
    #     |
    #   city removed from the dictionary


# 8) del.

# student={
#     "name":"Danish",
#     "age":25,
#     "occupation":"student",
#     "city":"Gujranwala"
# }
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student', 'city': 'Gujranwala'}
# del student["city"]
# print(student)#{'name': 'Danish', 'age': 25, 'occupation': 'student'}

# logic
# deletes the specific key-value pair and didn't show on the terminal