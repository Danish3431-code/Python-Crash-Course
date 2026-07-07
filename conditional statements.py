#1. 'if' Condition
# if statement is used to test a condition and execut the block of code only if condition is True

# age=int(input("Enter the age: "))
# if age>19:
#     print("Your are an adult.")


# 2. if-else Condition
# The if-else statement provides an alternative block of code to execute if the condition is False.

# Temperature=int(input("Enter the Temperature: "))
# if Temperature>25:
#     print("It's a hot day.")
# else:
#     print("It's a cool day")


#3. 'if-elif-else' Condition
# The 'if-elif-else' statement allows to check multiple conditions and execute the different
# blocks of code based on which condition is True.

# let's write a code to classify the student's grade based on their total marks(out of 100)
# Marks=int(input("Enter the Marks: "))
# if Marks>=90:
#     print("Grade- A+")
# elif Marks>=80:
#     print("Grade- A")
# elif Marks>=70:
#     print("Grade- B")
# elif Marks>=60:
#     print("Grade- C")
# else:
#     print("Grade- D")


#4. 'Nested if-else Statement' 
# placing an if-else statement inside another if-else statement.
#  checking multiple conditions that depend on each other.
 
#Q. Number Classification: Let's say you want to classify a number as positive, 
# negative, or zero and further classify positive numbers as even or odd. 

# number=24
# if number > 0:
#     print("Number is positive")
#     print("Now check that number is even or odd")
#     if number % 2==0:
#         print ("Number is even")
#     else:
#         print("Number is odd")
# else:
#     if number == 0:
#         print("Number is Zero")
#     else:
#         print("Number is negative")

# 5. Conditional Expressions
# Conditional expressions provide a shorthand way to write simple if-else 
# statements. Also known as Ternary Operator.   

# age=int(input("Enter the age:"))
# status="married" if age>=18 else "minor"
# print(status)



# Conditional Statements- HW 
# Q1: what is expected output and reason? 

# value = None 
# if value: 
#     print("Value is True") 
# else: 
#     print("Value is False") 


# Q2: write a simple program to determine if a given year is a leap 
# year using user input. 

# year=int(input("Enter the year:"))
# if (year%4==0 and year%100 !=0)or(year%400==0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")