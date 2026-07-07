#List in python

# A list is used to store multiple values in one variable. Lists are mutable (can be changed) and can store different data types.

# marks=[87,64,33,95,76]
# foods=["samosa","pizza","burger"]
# student=["Danish Nadeem",21,"Gujranwala"]

# #Accessing Elements (Indexing)
# Each item in a list has an index starting from 0.

# foods=["samosa","pizza","burger"]

#find the size of the list
# print(len(foods))#3

#Indexing:

# print(foods[0])
# print(foods[2])

#Modifing Elements(mutable)
# lists are changeable

# foods[0]="Fries"
# print(foods)#['Fries', 'pizza', 'burger']


#List slicing
# you can extract parts of a list using slicing.

# marks=[87,64,33,95,76]
# print(marks[1:4]) #[64, 33, 95]
# print(marks[:3]) #[87, 64, 33]
# print(marks[-3:-1]) #[33, 95]
# print(max(marks)) #95
# print(min(marks)) #33

#we use append() method to add element in the list.
# marks.append(74) #[87, 64, 33, 95, 76, 74]
# print(marks)

#we use insert() method to insert element at specifice index
# marks.insert(6,42)
# print(marks)

#we use remove( ) method to remove the first occurrence of the element.

# list1=["mango","apple","orange","banana","banana"]
# list1.remove("banana") #['mango', 'apple', 'orange', 'banana']
# print(list1)

# #we use pop() method to remove element at specific index.
# list1.pop(0)
# print(list1)


#we use sort() method to sort elements in ascending order.

# list3=[3,5,7,9,3,1,2,3,5,7,9,10]
# list3.sort()
# print(list3) #[1, 2, 3, 3, 3, 5, 5, 7, 7, 9, 9, 10]

# list4=[3,5,7,9,3,1,2,3,5,7,9,10]
# list4.sort(reverse=True) #[10, 9, 9, 7, 7, 5, 5, 3, 3, 3, 2, 1]
# print(list4)

#we use reverse () method to reverse the list 

# list5=[1,4,6,7,8,9,0,10,11]
# list5.reverse() #[11, 10, 0, 9, 8, 7, 6, 4, 1]
# print(list5)


#QUESTION 
# write a program that takes names of 4 favorite foods from the user and stores them in list . Then print list and its length.

# first way:

# favorite_food_1=input("Enter the food_1:")
# favorite_food_2=input("Enter the food_2:")
# favorite_food_3=input("Enter the food_3:")
# favorite_food_4=input("Enter the food _4:")
# print(favorite_food_1,favorite_food_2,favorite_food_3,favorite_food_4)
# print(type(favorite_food_1),type(favorite_food_2),type(favorite_food_3),type(favorite_food_4))

#second way:

# favorite_food1=input("Enter thr food 1:")
# favorite_food2=input("Enter the food2:")
# favorite_food3=input("Enter the food3:")
# favorite_food4=input("Enter the food4:")

# food_list=[]
# food_list.append(favorite_food1)
# food_list.append(favorite_food2)
# food_list.append(favorite_food3)
# food_list.append(favorite_food4)
# print(food_list) # ['pizza', 'burger', 'mutton', 'mango']


#List Methods in Python

# data=["Danish",21,"Pizza","Mango"]
# # 1)append(): Add one item at the end.
# data.append("Ice-cream")
# print(data)#['Danish', 21, 'Pizza', 'Mango', 'Ice-cream']

# # 2)extend():Add multiple items from another list.
# list=[10,20,30]
# data.extend(list)
# print(data)#['Danish', 21, 'Pizza', 'Mango', 'Ice-cream', 10, 20, 30]

# # 3)insert():Add item at a specific position.
# data.insert(8,"Nadeem")
# print(data)#['Danish', 21, 'Pizza', 'Mango', 'Ice-cream', 10, 20, 30, 'Nadeem']

# # 4)remove(): remove item by value.
# data.remove("Mango")
# print(data)#['Danish', 21, 'Pizza', 'Ice-cream', 10, 20, 30, 'Nadeem']

# # 5)pop(): remove item by index. and if index is not give it remove last element in the list.

# data.pop(2)
# print(data)#['Danish', 21, 'Ice-cream', 10, 20, 30, 'Nadeem']

# # if index is not given it remove last element from the list.

# data.pop()
# print(data)#['Danish', 21, 'Ice-cream', 10, 20, 30]

# 6)clear(): delete all items from the list. 
# data.clear()
# print(data)#[]

# 7)index() find position of an item from the list.

# my_list=[21,"Danish","Ice-cream","Mutton",18.90,"Reacher","Mutton"]
# print(my_list)#[21, 'Danish', 'Ice-cream', 'Mutton', 18.9, 'Reacher']
# print(my_list.index("Reacher"))#5

# # 8)count(): count how many times an item appears
# print(my_list.count("Mutton"))#2

# 9)sort():Arrange items in order. sort() method apply only on the list which contain same type of data.

# item=[2,5,7,1,3,6,4]
# item.sort()
# print(item)#[1, 2, 3, 4, 5, 6, 7]

# item1=["Danish","Ali","Hamad","Talha","Reacher"]
# item1.sort()
# print(item1)#['Ali', 'Danish', 'Hamad', 'Reacher', 'Talha']


# 10)reverse():reverse the list.
# numbers=[1,2,3,4,5,6,7,8,9,10]
# numbers.reverse()
# print(numbers)#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 11)copy():make a duplicate list.
# list=[10,3,0,4,7]
# print(list) #original list [10, 3, 0, 4, 7]
# my_list=list.copy() #[10, 3, 0, 4, 7]
# print(my_list) #copy list
# my_list.append("orange")
# print(my_list)#copy list [10, 3, 0, 4, 7, 'orange']
# print(list) #[10, 3, 0, 4, 7]


# How to join lists in python? 
# joining= combining two or more lists into one list.

# Method 1: using + (most easy)
# list1=[1,2]
# list2=[3,4]
# list3=list1+list2
# print(list3)#[1, 2, 3, 4]

# logic: list1+list2
#             |
#        one new list

#Method 2: using extend()
# list1=[1,2]
# list2=[3,4]
# list1.extend(list2)
# print(list1)#[1, 2, 3, 4]

# logic: take  all items from list2
#                     |
#             Add them into list1



# What is list Comprehension?
# list comprehension=Quik way to create a list in one line.

# SYNTAX:
# 

# Example 1(Numbers)
# nums=[i for i in range(5)]
# print(nums)#[0, 1, 2, 3, 4]


#Examle 2(square)
# square=[num*num for num in range(1,6)]
# print(square) #[1, 4, 9, 16, 25]

# Example 3(even numbers)
# evens=[num for num in range(1,11) if num % 2==0]
# print(evens) #[2, 4, 6, 8, 10]


#Example 4 find word start from "a"
# list2=["ali","hassan","amir","ahmed","ans"]
# a=[word for word in list2 if word.startswith("a") ]
# print(a) #['ali', 'amir', 'ahmed', 'ans']

#Example 5 to find odd numbers
# list3=[0,1,2,3,4,5,6,7,8,9,10,11]
# odd=[number for number in list3 if number%2 !=0]
# print(odd)#[1, 3, 5, 7, 9, 11]


#Example 6

# nums=[x for x in "python"]
# print(nums)#['p', 'y', 't', 'h', 'o', 'n']


#NESTED LIST
# list inside another list

# list1=["hello",1,[2,3,10.9],["world","Ali"]]
# print(list1)#['hello', 1, [2, 3, 10.9], ['world', 'Ali']]


#List Comprehesion:
# list comprehesion provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause, and optionally if clauses.
 
#  SYNTAX: 
# new_list=[expression for item in iterable if condition]


# Question: creating a list of squares?
# square=[x**2 for x in range(1,6)]
# print(square)#[1, 4, 9, 16, 25]

#Question:Write a Python program using List Comprehension to create a list where each number is raised to the power of itself for numbers from 1 to 5, and then print the resulting list?

# memory trick:
# Base = x
# Power = x

# number=[x**x for x in range(1,6)]
# print(number) #[1, 4, 27, 256, 3125]

# Question: filtering even numbers?
# even=[x for x in range(1,11) if x % 2 ==0]
# print(even) #[2, 4, 6, 8, 10]

#Question: filtering odd numbers?
# odd=[x for x in range(1,11) if x % 2 !=0]
# print(odd) #[1, 3, 5, 7, 9]

# Question: Applying a function to each element.
# fruits=["apple","banana","orange","grape","danish"]
# upper_case=[fruit.upper() for fruit in fruits]
# print(upper_case) #['APPLE', 'BANANA', 'ORANGE', 'GRAPE', 'DANISH']

# Question: flatten a nested list using list comprehesion.
# classA=[["ali","ahmed"],[2,4],[3.06,"banana"]]
# nested_list=[item for sublist in classA for item in sublist]
# print(nested_list) #['ali', 'ahmed', 2, 4, 3.06, 'banana']

# Another way to flatten a nested list by using simple for loop:

# classB=[[1,2,],[3,4],[5,6],[7,8],[9,10]]
# result=[]
# for sublist in classB:
#     for item in sublist:
#         result.append(item)
# print(result) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Question: Remove dupicates from the list by using for and if statement?

# list1=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
# result=[]
# for item in list1:
#     if item not in result:
#         result.append(item)
# print(list1)#[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
# print(result)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Another and simle way to remove duplicate from the list?
# list2=["Danish","Danish","Ali","Ali",2,2,5,5,6,6,7,7,8,8,9,9,10,10]
# print(list(set(list2))) #[2, 5, 6, 7, 8, 9, 10, 'Danish', 'Ali']


# Iterating Over Lists:

# Iterating allows you to traverse each element in a list, typically using loops.

# Example:
# fruits=["apple","banana","cherry"]
# #using for loop:
# for fruit in fruits:
#     print(fruit)#apple
                #banana
                #cherry

# Example1 using while loop :
# fruits=['apple','banana',"cherry"]
# index=0
# while index<len(fruits):
#     print(fruits[index])
#     index=index+1 #apple
                  #banana
                  #cherry


#Example2 using while loop:
# list2=["Danish","Ahmed","Ali",1,2,3,4.5]
# i=0
# while i < len(list2):
#     print(list2[i])
#     i=i+1 #Danish
            #Ahmed
            #Ali
            #1
            #2
            #3
            #4.5

#Example 3 using while loop:

# even=[0,1,2,3,4,5,6,7,8,9,10]

# index=0

# while index<len(even):
#     if even[index] % 2==0:
#         print(even[index])
#     index=index+1 #0
                    #2
                    #4
                    #6
                    #8
                    #10


