#SET IN PYTHON:

# A set is an unordered collection of unique values. It automatically removes the duplicates and does not support indexing.

#Features:
# -> No duplicates
# -> Unordered
# -> Mutable(can add / remove items)
# -> No indexing

# EXAMPLE:
# fruit={"apple","banana","cherry"}

# Memory Trick

# list= ordered + duplicates Allowed
# Tuple= ordered + cannot change
# Set= unique values only

# Creating a set:-
# 1) using {}:

# numbers={1,2,3,4,5}
# print(type(numbers))#<class 'set'>
# print(numbers) #{1, 2, 3, 4, 5}

# 2) using set():

# numbers=set([1,2,3,4,5])
# print(type(numbers))#<class 'set'>
# print(numbers)#{1, 2, 3, 4, 5}


# EMPTY SET:-

# x wrong:

# numbers={}
# print(tuple(numbers))#()
# print(numbers)#{}

# This creates  a dictionary


# ✔️ Correct:

# numbers=set()
# print(type(numbers))#<class 'set'>
# print(numbers)#set()


# ADDING ITEMS:-

# 1)add():
# Adds one item.

# fruits={"apple","banana"}
# fruits.add("cherry")
# print(fruits)#{'apple', 'cherry', 'banana'}

# REMOVING ITEMS:-

# 1) remove():

# fruits={"apple","cherry","banana"}
# # fruits.remove("banana")
# # print(fruits)#{'apple', 'cherry'}

# It gives the error if item not found.

# fruits.remove("orange")
# print(fruits)

# 2) discard():

# fruits={"apple","cherry","banana"}
# fruits.discard("cherry")
# print(fruits)#{'apple', 'banana'}

# It didn't give error if item not found

# fruits.discard("orange")
# print(fruits)

# Memory Trick:

# remove() = strict
# discard() = safe

#Set Operations:-

# 1)Union

# Combine both sets.

# A={1,2,3}
# B={3,4,5}
# print(A.union(B))#{1, 2, 3, 4, 5}

# SYMBOL(A|B)

# 2)Intersection

# Common values only.

# A={1,2,3}
# B={3,4,5}
# print(A.intersection(B))#{3}

# SYMBOL(A & B)


# 3) Difference:

# Values in A but not in B

# A={1,2,3}
# B={3,4,5}
# print(A.difference(B))#{1, 2}

# SYMBOL(A-B)

# 4)Symmetric Difference:

# keep unique items only and remove common items.

# A={1,2,3}
# B={3,4,5}
# print(A.symmetric_difference(B))#{1, 2, 4, 5}

# SYMBOL(A ^ B)

# LOOP ON SET:-
# For loop:

# numbers={1,2,3,4,5}
# for number in numbers:
#     print(number) #1
                    #2
                    #3
                    #4
                    #5

# While loop:

# numbers=[1,2,3,4,5]
# index=0
# while index < len(numbers):
#     print(numbers[index])
#     index=index+1 #1
                    #2
                    #3
                    #4
                    #5


# SET COMPREHESION:-
#syntax:
# {expression for item in iterable}

# Example:

# squares={x*x for x in range(1,6)}
# print(squares)#{1, 4, 9, 16, 25}

# MOST IMPORTANT USES OF SET:-
#1) Remove Duplicates:

# numbers={1,1,2,2,3,3,4,4,5,5}
# print(numbers)#{1, 2, 3, 4, 5}

# 2)Fast searching:

# if 5 in numbers:
# set checks very quickly.

# numbers={1,2,3,4,5}
# if 4 in numbers:
#     print("True") #True
# else:
#     print("False")

# numbers={1,2,3,4,5}
# if 6 in numbers:
#     print("True") 
# else:
#     print("False") #False

# set use in real life:-
# 1) unique data store kerna.
# 2) Fast searching kerna.
# 3) Duplicates remove kerna.