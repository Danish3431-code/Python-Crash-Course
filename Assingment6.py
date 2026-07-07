#LOOP PRACTICE QUESTIONS

#QUESTION#1
# print the while loop outut in same line

# each function contain parameters print() is also a function with parameter sep="any sumbol" and end="\n" (\n) mean next line
# so to print output on same line we write end=" " so that output print in the same line.                                                                                                       

# i=1
# while i<4:
#     print(f"Hello Danish {i}", end=" ")
#     i=i+1

#QUESTION2 
# print star pattrens using loops

# a) Simple triangle Pattren

# *
# **
# ***
# ****
# *****
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# b) Inverted triangle Pattern
# n=5
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# c) Pyramid Pattern
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1))


#QUESTION#3
# write a program to find the factorial of the given number

# by simple code:

# n=5
# result=1
# for i in range(1, n+1):
#     result=result*i
#     print(result)

# by creating function:

# def factorial(n):
#     result=1
#     while n>0:
#         result=result*n #5*1, 5*4, 20*3, 60*2, 120*1
#         n=n-1
#     return result
# print(factorial(5))

#5! = 5 * 4 * 3 * 2 * 1


# QUESTION 4
# Count the number of vowels in a string

# aeiou
#QUESTION 4
# Find the given string contian any vowels or not?

# string1="Danish"
# if "a" in string1 or "e" in string1 or "i" in string1 or "o" in string1 or "u" in string1:
#     print(f"{string1} contain vowels")
# else:
#     print(f"{string1} doesn't contain any vowels")


# QUESTION 5
# Count the number of vowels in a string


# string2="Python by Rishab Mishra"
# vowels="aeiou"
# count=0
# for i in string2:
#     if i.lower() in vowels:
#         count=count+1
# print(count)


# string3="Hello My Name Is Danish"
# vowels="aeiou"
# count=0
# for i in string3:
#     if i in vowels:
#         count=count+1
# print(count)


#QUESTION 6
# find longest word in a string

# sentence="Hello My Name Is Danish"
# words=sentence.split() #split() is used to break a string into smaller parts (words) and store them in a list.
# longest_word=""
# for word in words:
#     if len(word)>len(longest_word):
#         longest_word=word
# print(longest_word)

#QUESTION 7 
# "do while" loop in the python
 
# In do while loop body executes at leat once before checking the condition.

# while True:
#     num=int(input("Enter the number greater than 10:"))
#     if num>10:
#         print(f"valid number enterd: {num}")
#         break #exist the loop when condition is true
#     else:
#         print("Number is not greater than 10, try again!")


#QUESTION 8
# write a program to print fibonnaci series

# def fibonacci(n):
#     a=0
#     b=1
#     count=0
#     while count<n:
#         print(a) #0
#         a,b=b,a+b 
#         count=count+1
# fibonacci(5)

# def fibonacci(n):
#     a=0
#     b=1
#     count=0
#     while count<n:
#         print(a)
#         a,b=b,a+b
#         count=count+1
# fibonacci(6)

# def fibonacci(n):
#     a=0
#     b=1
#     count=0
#     while count<n:
#         print(a)
#         a,b=b,a+b
#         count =count+1
# fibonacci(10)

