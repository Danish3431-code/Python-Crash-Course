# LAMBDA FUNCTION IN PYTHON:
# lambda function is also known as anonymous function ( mean without any name).

# SYNTAX:
# lambda arguments:expression

# lambda is a one-line anonymous function used for short tasks.

# EXAMPLES:
# 1)perform simple calculations:

# ADD
# add=lambda a,b:a+b
# print(add(2,3)) #5

# Subtract
# sub=lambda a,b:a-b
# print(sub(5,2))#3


# 2) Square Numbers:
# square=lambda a:a*a
# print(square(4))#16

# Cube Numbers:
# cube=lambda b:b*b*b
# print(cube(4))#64


# 3)Use with map() (Apply to all items)
# map()=change all items in a list one by one,apply one function to all items in a list.

# Why we use map()?
# it save Time.
# no need to write loop.
# works on all elements at once.
# clean and short code

# When we use map()?
# we want to change every item in a list.

# Why not use map()?
# when you want only some items(use filter instead)
# when no fucntion is needed

# QUESTION:
# Want to multiple each item in a list with 2.
# num=[2,3,4]
# result = list(map(lambda a:a*2 , num))
# print(result) #[4, 6, 8]

# 4)Filter():
# keep only items that match condition.

# num=[1,2,3,4,5,6,7,8,9,10]
# result=list(filter(lambda a: a%2==0, num))
# print(result)

# 5)Use with sorted()
# sorted() arranges items in order(ascending) or custom.
# num=[10,9,8,7,6,5,4,3,2,1]
# result=sorted(num,key=lambda a: a )
# print(result)


fruit=['mango','mango','grapes','grapes','orange']
print(list(set(fruit)))
print(type(list(set(fruit))))
