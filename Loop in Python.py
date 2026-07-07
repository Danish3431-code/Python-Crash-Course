#LOOP IN PYTHON:
# A loop is used to repeat code again and again without writing it multiple times.

#     loop=Repeat work automatically

# Types of Loopa:
# 1) while Loop
# 2) for Loop
# 3) Nested loop(loop inside loop)


# while loop:
#     Runs code as long as condition is True.
#     syntax:
#      while condition:
#        code

# EXAMPLE:
# count=0
# while count<4:
#     print(count)
#     count += 1

# while loop ="Jab tak condition true ha tab tak repeat karo"



# 2) for loop
# used when you know how many times to repeat
# for i in range(5): # agar range ma 1 number ho tou wo stop ho ga and output ma wo include nahi ho ga
#     print(i)

# with range(start,stop,step)
# start: is include when output is shown
# stop: is not include when output is shown
# step: how many steps that skips 

# for i in range(1,10,2):
#     print(i)

# for loop = "fixed times repeat"

# while-Loop         |  for loop
#                    |
# condition-based    | range/ sequence-based
# unknown repeats    | known repeats


# LOOP Control Statements:

# break: stops the loop completely
# for i in range(5):
#     if i==3:
#         break
#     print(i)


# continue:skips current step and moves to next.
# for i in range(5):
#     if i==3:
#         continue
#     print(i)

# continue = SKIP current Value


# pass:Does noting(placeholder)

# for i in range(5):
#     pass

# pass = EMPTY code (no action)


# while True loop (important concept)
# infinite loop (run forever) until stopped manually.

# while True:
#     user=input("Enter 'exist' to stop:")
#     if user=='exist':
#         break
#     print("You entered:", user)



# QUESTION:
# Write a program for an ATM system using loops where the user can check balance, deposit money, witdraw money, and exit. The program should keep running until the user chooses to exit.

# # step:1 set balance
# balance=1000
# # step:2 Infinite loop
# while True:
# # step:3 show menu
#     print("=== ATM MENU===")
#     print("1. Check Balance")
#     print("2. Deposite Money")
#     print("3. Withdraw Money")
#     print("4. Exist")
#  #step:4 Take input from user

#     choice=input("Enter your choice(1-4): ")
#     if choice=='1':
#         print("Your current balance is: ", balance  )
#     elif choice=='2':
#         deposit=int(input("Enter amout to deposit: "))
#         if deposit>0:
#             balance=balance+deposit
#             print("deposit successfull and updated balance is: ", balance)
#         else:
#             print("Invalid depoit amount!")
#     elif choice == "3":
#         withdraw = int(input("Enter the amount to withdraw: "))
#         if withdraw<=balance:
#             balance = balance-withdraw
#             print("Withdrawal successful! and remaining balance is: ", balance)
#         else:
#             print("Insufficient balance!")
#     elif choice == '4':
#         print("Thank you for using ATM. Goodbye!")
#         break
#     else:
#         print("Invalid choice Please select 1-4.")




# for my practice

# balance=2000
# while True:
#     print("===ATM MENU===")
#     print("1. Check Balance:")
#     print("2. Deposite Amout")
#     print("3. Withdrawl Amount")
#     print("4: Exit")
#     choice=int(input("Select the numbers (1-4) to perform Operations:"))
#     if choice==1:
#         print("Your current balance is: ",balance )
#     elif choice==2:
#         deposite=int(input("Enter the deposite amount:"))
#         if deposite>0:
#             balance=balance+deposite
#             print("deposite successful and upgraded balance is: ",balance)
#         else:
#             print("Invalid deposite amount")
#     elif choice==3:
#         withdrawl=int(input("Enter the withdrawl amount: "))
#         if withdrawl<=balance:
#             balance=balance-withdrawl
#             print("Withdrawl successfull and upgraded balance is: ",balance)
#         else:
#             print("Insufficient amount")
#     elif choice==4:
#         print("Thankyou for using ATM.")
#         break
#     else:
#         print("Invalid choice select from(1-4)")



#CALCULATOR:
#Write a Python program for a Calculator System using loops and conditional statements.

# #  step:1 Start a loop
# while True:
#     #step:2 Show Menu
#     print("===MENU===")p0
#     print("1. Addition ")
#     print("2. Subtraction ")
#     print("3. Multiplication ")
#     print("4. Division ")
#     print("5. Exit ")
#     #step:3 Take user choice
#     choice=int(input("Which operation do you want: "))
#     #step:4 Decision Making
#     if choice==1:
#         print("Enter the numbers")
#         firstNumber=int(input("Enter first number:"))
#         secondNumber=int(input("Enter the second number:"))
#         Result=firstNumber+secondNumber
#         print("Addition of two numbers is: ", Result)
#     elif choice==2:
#         print("Enter the numbers")
#         firstNumber=int(input("Enter first number:"))
#         secondNumber=int(input("Enter the second number:"))
#         Result=firstNumber-secondNumber
#         print("Subtract of two numbers is: ",Result)
#     elif choice==3:
#         print("Enter the numbers")
#         firstNumber=int(input("Enter first number: "))
#         secondNumber=int(input("Enter the second number:"))
#         Result=firstNumber*secondNumber
#         print("Multiplication of Two numbers is: ",Result)
#     elif choice==4:
#        print("Enter the numbers:")
#        firstNumber= int(input("Enter the number: "))
#        secondNumber=int(input("Enter the number: "))
#        if secondNumber !=0:
#            Result=firstNumber/secondNumber
#            print("Division of two numbers is: ",Result)
#        else:
#            print("Cannot divide by zero")
#     elif choice==5:
#         print("Goodbye ")
#         print("--------")
#         break
#     #Step:5 User enter wrong menu
#     else:
#         print("Invalid choice")



#NUMBER GUSSEING GAME:

# Write a Python number guessing game using a loop where the user keeps guessing until the correct number is found.
# Give hints “Too High” or “Too Low” after each wrong guess and stop when correct.


# Number=7
# while True:
#     print("===NUMBER GUESSING===")
#     print("Enter the number")
#     User_Number=int(input("Now user enter the number:"))
#     if User_Number==Number:
#         print("Correct! You won 🎉")
#         break
#     elif User_Number > Number:
#         print("Too high! Try Again")
#     elif User_Number < Number:
#         print("Too low! Try Again")
