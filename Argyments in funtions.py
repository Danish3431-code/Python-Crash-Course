#Arguments in Functions
#What are Arguments?
#Arguments are values passed into a function when calling it.

# def greeting(name):
#     print("Hello",name)
# greeting('Danish')

# name=parameter
# 'Danish'=arguemnt

# #IMPORTANT RULE:
# Number of arguments should match number of parameter.

# Types of Function Arguments:
# 1. Required Arguments
# 2. Default Arguments
# 3. Keyword Arguments
# 4. Arbitrary Arguments(*args, **kwargs)

# 1. Required Arguments.
# Values must be passed in correct order.

# def add(a,b):
#     print(a+b)
# add(5,3)

# 2.Default Arguments.
# Default value is used if no argument is given

# def greet(name="World"):
#     print("Hello",name)
# greet() #output: Hello World
# greet("Ali") #output: Hello Ali

# 3.Keyword Arguments
# Arguments are passed using parameter names.

# def divide(a,b):
#     return a/b
# print(divide(a=20,b=10))

# order does not matter here.

# 4. Arbitrary Arguments.
# used when number of arguments are unknown and their are two types of Arbitrary argument.

    # a) Arbitrary Positional Arguments(*args)
        # used to pass multiple values .
        # values are stored as a (tuples).
#  SYNTAX:
                
# def test(*args):
#     print(args)


# EXAMPLE 1:

# def add_numbers(*args):
#     return sum(args)
# print(add_numbers(1,2,3,4,5))

# EXAMPLE 2:
# def greet(*args):
#     print(type(args))
#     print("Hello",args)

# greet("Ali","Ahmed","Danish")

# EASY MEMORY TRICK
# *args = many values
# stored as tuple()


        # b) Arbitrary Keyword Arguments(**kwargs)

            # used to pass multiple named values.
            # values are stored as a dictionary. dictionary ma data key and value ki forma ma store hota ha.

#SYNTAX:
# def test(**kwargs):
#     print(kwargs)

# EXAMPLE 1:
# def details(**kwargs):
#     for key, value in kwargs.items():
#         print(key,value)
# details(name="Ali", age=20)

# # EXAMPLE 2:
# def shopping(**products):
#     total=0
#     for item, price in products.items():
#         print(item,price)
#         total+=price
#         print("Total=",total)
# shopping(apple=10, mango=20)

# DIFFERENCE B/W (*args) and (**kwargs)
# *args                            |       **kwargs
#  positional values               |   named values
# tuple                            |   dictionary
# no names                         |   key,value

