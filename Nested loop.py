#NESTED LOOP
# A loop inside a loop is called a nested loop.

# -> inner loop runs completely  for evey single cycle of outer loop.

# jab outer loop ik dafa run ho ga tou us ka endar jo inner loop ha us ki all itreations run  hon gi pfhit dobara outer loop run ho ga phir inner loop ki all iterations run ho gi.

# WHY we use nested loops?
# 1) patterns: used to print shapes like stars.
# 2) Grid\Tables: Used for row and columns (like matrix)
# 3)Repeated structure: When one loop depends on another.

        # ----------BASIC IDEA-----------#
            # outer loop runs
            #        | 
            # Inner loop runs fully
            #        |
            # outer loop runs again

#QUESTION:  Print numbers from 1 to 3, for 3 times using for-for nested loop
# for i in range(3):
#     for j in range(1,4):
#         print('-----')
#         print(j)
#     print()

#QUESTION: Print numbers from 1 to 3, for 3 times using while for nested loop 

# i=1
# while i<4:
#     for j in range(1,4):
#         print(j)
#     print()
#     i=i+1


#QUESTION: Print prime numbers from 2 to 10 

# for num in range(2,10):
#     for j in range(2,num):
#         if num%j==0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")


#solve by using only if condition

# if user%2==0:
#     print("not prime number")
# elif user%2 !=0:
#     print("prime number")

