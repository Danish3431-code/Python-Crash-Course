# #Function in Python:
# # A function is a reusable block of code that perform a specfic task.

# # Benefits.

# # 🔘 Improves readability.

# # 🔘 Reduces repeated code.

# # 🔘 Makes program reusable.

# Basic Concepts:

# 🔘 Create: function use def keyword
#     def greet():
#         print("Hello")
# 🔘 Call: function use function parentheses.
#     def student(name):
    
#     name=parameter

# 🔘 Argument: Actual value passed during function call.
#         student('Ali')
# 'Ali'=argument.

# Types of Functions:

# There are two types of functions in python.

# 1.Built-in library function:

#     These are standard functions in python that are available to use.
#     Examples: print(),input(),type(),sum(),max() etc.

# 2.User-defined function:

#     We can Create our own functions based on our requirements.
#     Examples:Create your own function().


# SYNTAX:
#     def my_function(param):
#         instruction-1
#         instruction-2
#     return result


# EXAMPLE:1
# Function without parameter

# Create or Define Function 
# def greeting():
#     print("Welcome to Python tutorial ")

# # Use or call this Function 
# greeting()

#EXAMPLE:2
#Function with Parameters

# function to adds two numbers & print result.

# def add_two_numbers(a,b):
#     result=a+b
#     print(result)
# add_two_numbers(4,5) #Function with two arguments
    

# The Return Statement:

# The return statement is used inside a function to send a result back to where the function was called. when return is executed, 
# the function stops running and immediately return the specified  value.

# def add(a,b):
#     return a+b
# result=add(5,4)
# print(result)


# Function with a Return value:

# Function to convert Celsius to Fahrenhiet.

# function to convert Celsius to Fahrenheit 
# def celsius_to_fahrenhiet(celsius):
#     fahrenhiet=(celsius*9/5)+32
#     return fahrenhiet
# # Calling this function to return a value
# temp_f=celsius_to_fahrenhiet(25)
# print(f"temperature in fahrenhiet:{temp_f}")

#Pass Statement

# The pass statement is a placeholder in a function or loop. It does nothing and is 
# used when you need to write code that will be added later or to define an empty 
# function. 

