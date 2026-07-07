#PROJECT:1
            #CALCULATER

# write a python program to build a simple calculator.
# Available Operations.
# 1. Addition(1): sum of two numbers.
# 2. Subtraction(2): subtraction between two numbers.
# 3. Multiplication(3): Product between two numbers.
# 4. Division(4): divide two number.
# 5. Average(5): Average of two numbers.

# This Project will done in 3 steps:

# step1: functions for operations.
# step2: user input.
# step3: print result.

#STEP1:functions for operations.

#add two numbers
def add_Two_numbers(num1,num2):
    return num1+num2
#Subtract two numbers
def sub_two_numbers(num1,num2):
    return num1-num2
#Multiply two numbers
def multiply_Two_numbers(num1,num2):
    return num1*num2
#Divide two numbers
def divide_two_numbers(num1,num2):
    return num1/num2
def average_two_number(num1,num2):
    return (num1+num2)/2

#STEP2: user input

print("Please select an operation:\n " "1. Addition \n" "2. Subtraction\n" "3. Muliplication\n" "4. Division\n" "5. Average\n")

select=int(input("Select an operation from 1,2,3,4,5: "))
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number: "))

#STEP 3:print result

if select==1:
    print(f"{number1} + {number2} =",add_Two_numbers(number1,number2))
elif select==2:
    print(f"{number1} - {number2} =",sub_two_numbers(number1,number2))
elif select==3:
    print(f"{number1} * {number2} =",multiply_Two_numbers(number1,number2))
elif select==4:
    print(f"{number1} / {number2} =",divide_two_numbers(number1,number2))
elif select==5:
    print(f"( {number1} + {number2} ) / 2 =",average_two_number(number1,number2)) #Average is also called mean.
else:
    print("Invalid operator")