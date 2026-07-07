#TUPLES IN PYTHON:
# A tuple is a collection of multiple value.
# Tuple is:
# ->ordered
# ->Allows duplicates
# ->Immutable (cannot be change)

# Example:
# fruits=("apple","banana","cherry","apple")

# Memory Trick:
# list=changeable
# tuple=not changeable

# Creating Tuples:
# 1) using():

# colors=("red","green","blue")
# print(colors)#('red', 'green', 'blue')

# 2)without():

# colors="red","green","blue"
# print(colors) #('red', 'green', 'blue')

# 3)using tuple():

# colors=tuple(["red","green","blue"])
# print(colors)#('red', 'green', 'blue')

# 4)single item tuple:

# item=("apple",)
# print(type(item))#<class 'tuple'>
# print(item)('apple',)

# ACCESSING ELEMENTS (INDEXING)

# how to access first  item?

# fruits=("apple","banana","cherry")
# print(fruits[0]) #apple

# how to access last item?

# fruits=("apple","banana","cherry")
# print(fruits[-1])#cherry

# Memory Trick:

# 0  -> first item
# -1 -> last item


# Slicing:
 # SYNTAX

# tuple[start:end:step]

# Example:

# numbers=(10,20,30,40,50,60)
# print(numbers[1:4])#(20, 30, 40)

# Reverse tuple:

# numbers=(10,20,30,40,50,60)
# print(numbers[::-1])#(60, 50, 40, 30, 20, 10)

# TUPLE OPERATIONS:

# 1)Join Tuples(+):

# TupleA=(1,2)
# TupleB=(3,4)
# TupleC=TupleA+TupleB
# print(TupleC)#(1, 2, 3, 4)

# 2) Repeat tuple(*):

# TupleA=("Hi ")
# print(TupleA*3)#Hi Hi Hi 

# 3)check item(in):

# TupleB=(10,20,30,40,50)
# print(20 in TupleB)#True

# LOOP ON TUPLE:

# for loop:

# fruits=("apple","orange","grape")
# for fruit in fruits:
#     print(fruit) #apple
                #orange
                #grape

# while loop:

# fruits=("apple","orange","grape")
# index=0
# while index<len(fruits):
#     print(fruits[index])
#     index=index+1 #apple
                    #orange
                    #grape


# TUPLE METHOD:
# Method          work

# count()         count occurrences
# index()         find position

# count():

# TupleD=("red","green","green")
# print(TupleD.count("green"))#2

# index():

# TupleE=("red","green","orange")
# print(TupleE.index("green")) #1

# TUPLE FUNCTIONS:

# Function        Work
# len()           check total items
# sum()           total sum
# min()           smallest Value
# max()           largest Value
# sorted()        sort values

# Example:

# numbers=(2,3,1,4)
# print(len(numbers))#4

# numbers=(2,3,1,4)
# print(sum(numbers))#10

# numbers=(2,3,1,4)
# print(min(numbers))#1

# numbers=(2,3,1,4)
# print(max(numbers))#4

# numbers=(2,3,1,4)
# print(sorted(numbers))#[1, 2, 3, 4]


# PACKING TUPLE:
# packing is the process of putting multiple values in a single tuple.

# name="Danish"
# age=25
# occupation="Student"
# Tuple_packing=name,age,occupation
# print(Tuple_packing)#('Danish', 25, 'Student')

# UNPACKING TUPLE:

# unpacking is extracting the values from a tuple into a separate values.

# tupleB=("Danish",25,"Student")
# name,age,occupation=tupleB
# print(name)#Danish
# print(age)#25
# print(occupation)#Student

# Memory Trick:

# packing:
# many->one

# unpacking;
# one->many

# we can't modify the tuple,but their is a trick to modify the tuple.

# TupleA=(1,2,3)
# y=list(TupleA)
# # print(y)#[1, 2, 3]
# y.append("Danish")
# TupleA=tuple(y)
# print(TupleA)#(1, 2, 3, 'Danish')

# REAL LIFE USE OF TUPLE:

# 1)coordinates:
# (40.7128, -74.0060)

# 2) RGB Colors:
# (255,0,0)

# because these values should not change


# TUPLE AS DICTIONARY KEY
# tuple can be a dictionary key.

# locations={
#     (40.7128, -74.0060):"New york"
# }

# Reason:
# Tuple is immutable
# List is mutable