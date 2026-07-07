#1. VARIABLES

#Q1)Create two variables to store your name and age, then print them.

# Name="Danish"
# Age=25
# print(Name)#Danish
# print(Age)#25

# Q2)Store the length and width of a rectangle in variables and print its area.

# Length=25
# Width=25
# Area=Length*Width
# print(f"lenght & width of rectangle is:",Area)#lenght & width of rectangle is: 625

#2. DATA TYPES

# Q1) Create variables of type:
# int
# float
# string
# bool
# Print the type of each variable.

# Integer=10
# Float=12.5
# String="Danish"
# Boolean=True
# print(type(Integer))#<class 'int'>
# print(type(Float))#<class 'float'>
# print(type(String))#<class 'str'>
# print(type(Boolean))#<class 'bool'>

#Q2)Check the data type of:

# 100
# "100"
# 100.5
# True

# a=100
# b="100"
# c=100.5
# d=True
# print(type(a))#<class 'int'>
# print(type(b))#<class 'str'>
# print(type(c))#<class 'float'>
# print(type(d))#<class 'bool'>

# 3. TYPE CASTING

# Q1)Convert the string "50" into an integer and add 20.



# 3. Type Casting

# Q1)Convert the string "50" into an integer and add 20.

# number="50"
# number1=int(number)
# print(number1+20)#70


# Q2)Convert the integer 25 into:

# float
# string
# Print both.

# number=25
# number1=float(number)
# number2=str(number)
# print(number1)#25.0
# print(number2)#25




# 4. INPUT FUNCTION

# Q1)Take the user's name and print:
# Hello Danish

# User_Name=input("Enter the name:")
# print(User_Name)#Enter the name:Danish
                  #Danish

# Q2)Take two numbers as input and print their sum.

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# sum=num1+num2
# print(f"sum of {num1} & {num2} is:", sum)#sum of 55 & 55 is: 110


# 5. OPERATORS

# Q1) Take two numbers and perform:
# Addition
# Subtraction
# Multiplication
# Division

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# sum=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# print(f"sum of {num1} & {num2} is:",sum)#sum of 10 & 5 is: 15
# print(f"sub of {num1} & {num2} is:",sub)#sub of 10 & 5 is: 5
# print(f"mul of {num1} & {num2} is:",mul)#mul of 10 & 5 is: 50
# print(f"div of {num1} & {num2} is:",div)#div of 10 & 5 is: 2.0


# Q2)Check whether a number is even or odd using the modulus (%) operator.


# number=int(input("Enter your number:"))
# if number%2==0:
#     print(f"{number} is a positive number.")#2 is a positive number.
# else:
#     print(f"{number} is a odd number.")#3 is a odd number.



# 6. CONDITIONAL STATEMENTS

# Q1)Take a number and check whether it is positive or negative.

# number=int(input("Enter your number:"))
# if number<0:
#     print(f"{number} is a negative number.")
# else:
#     print(f"{number} is a positive number.")



# Q2)Take marks as input and print:
# Pass (marks ≥ 40)
# Fail (marks < 40)

# Marks=int(input("Enter marks obtained from 100: "))
# if Marks>=40:
#     print(f"your marks are {Marks} and you are pass.")
# if Marks <40:
#     print(f"your marks are {Marks} and you are fail.")


# 7. FUNCTIONS

# Q1)Create a function that prints:
#  Welcome to Python

# def function():
#     print("Hello Python")
# function()#Hello Python

# Q2) Create a function that returns the square of a number.

# def square():
#     x=int(input("Enter the number:"))
#     return x*x
# print(f"square of the given number is:",square())


# 8. FUNCTION ARGUMENTS

# Q1)Create a function that accepts a name and prints:
# Hello Ali

# def name(yourname):
#     print("Hello",yourname)
# name("Ali")#Hello Ali

#Q2)Create a function that accepts two numbers and returns their product.

# def sum(num1,num2):
#     product=num1+num2
#     return product
# print(sum(3,3))#6

# 9. STRINGS

# Q1)Count the number of characters in a string.

# name="Danish"
# counted_characters=len(name)
# print(counted_characters)#6

# Q2) Reverse a string without using slicing.

# Text="Python"
# reverse=""
# for char in Text:
#     reverse=char+reverse
# print(reverse)#nohtyP

# name="Danish"
# reverse=""
# for char in name:
#     reverse=char+reverse
# print(reverse)#hsinaD


# 10. LOOPS

# Q1)Print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print(i)#1
              #2
              #3
              #4
              #5
              #6
              #7
              #8
              #9
              #10


# Q2)Print only even numbers from 1 to 20 using a while loop.

# number=0

# while number<=20:
#     if number % 2==0:
#         print(number)
#     number+=1 #2
                #4
                #6
                #8
                #10
                #12
                #14
                #16
                #18
                #20




# 11. NESTED LOOPS

# Q1)Print this pattern:
# *
# **
# ***
# ****

# for i in range(1,5):
#     print("*"*i)
# *
# **
# ***
# ****



# Q2)Print this pattern:
# 1
# 12
# 123
# 1234

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print() #1
#             #12
#             #123  
#             #1234
             
# 12. LISTS

# Q1)Find the largest element in a list.

# list1=[4,5,6,2,8,10,1,0]
# find_max=max(list1)
# print(find_max)#10

# Q2)Remove duplicate elements while keeping the original order.

# list1=[1,1,2,2,3,3,4,4,5,5]
# remove_duplicates=list(set(list1))
# print(remove_duplicates)#[1, 2, 3, 4, 5]


# 13. TUPLES

# Q1)Find the index of a given element in a tuple.

# tuple_1=(1,2,3,4,"Danish",6)
# element="Danish"
# index_of_given_element=tuple_1.index(element)
# print(index_of_given_element)#4


# Q2)Count how many times a specific element appears in a tuple.

# tuple2=("Danish",2,2,1,1,4,4,4,5)
# specific_element_appears=tuple2.count(4)
# print(specific_element_appears)#3



# 14. SETS

# Q1)Find the common elements between two sets.

# set1={1,2,3,4,5}
# set2={5,4,1,6,7}
# common_element=set1 & set2
# print(common_element) #{1, 4, 5}


# set1={1,2,3,4,5}
# set2={5,4,1,6,7}
# common=set1.intersection(set2)
# print(common)#{1, 4, 5}


# Q2)Remove duplicate values from a list using a set.

# list1={1,1,2,2,3,3,4,4,5,5}
# remove_dupicate=set(list1)
# print(remove_dupicate)#{1, 2, 3, 4, 5}


# 15.) DICTIONARIES

# Q1)Find the student with the highest marks.

# Example:

# marks = {
#     "Ali": 80,
#     "Ahmed": 90,
#     "Umer": 75
# }

# marks = {
#     "Ali": 80,
#     "Ahmed": 90,
#     "Umer": 75
# }
# highest_marks=0
# highest_student=""
# for key,value in marks.items():
#     if value>highest_marks:
#         highest_marks=value
#         highest_student=key

# print(highest_student)#Ahmed
# print(highest_marks)#90

# marks = {
#     "Ali": 80,
#     "Ahmed": 90,
#     "Umer": 75
# }

# highest_student= max(marks, key=marks.get)
# print(highest_student)#Ahmed
# print(marks[highest_student])#90


# Q2)Sort a dictionary by its values in ascending order.

# marks = {
#     "Ali": 80,
#     "Ahmed": 90,
#     "Umer": 75
# }
# sorted_marks= dict( sorted(marks.items(), key=lambda item:item[1]))
# print(sorted_marks)#{'Umer': 75, 'Ali': 80, 'Ahmed': 90}