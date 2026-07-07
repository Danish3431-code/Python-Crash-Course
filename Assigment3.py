#  Q1: write a simple program to determine if a given year is a leap 
 # year using user input.

# year=int(input("Enter the Year: "))
# if(year%4==0 and year%100 !=0) or (year%400==0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year")

#Q2.write a programm that prompts the users to enter a username and password and checks whether they match. 
# provide appropriate messages for the following cases:
# 1. Both username and password are correct.
# 2. username is correct but password is incorrect.
# 3. username is incorrect.

# predefine_username='Danish'
# predefine_password='danish3431'
# username=input("Enter the username: ")
# password=input("Enter the password: ")
# if(username==predefine_username):
#     if(password==predefine_password):
#         print("Login Successfull")
#     else:
#         print("Incorrect password")
# else:
#     print("username is Invalid")



#Q3.Admission Eligibility: A university has the following eligibility criteria for admissions.
#1. Marks in Mathematics >= 65.
#2. Marks in Pyhisics >= 50.
# 3. Marks in Chemitry >= 50.
# 4. Total Marks in all three subjects >=180 OR Total Marks in mathematics and phusics >= 140.

# write a program that takes marks in three subjects as input and prints whether the student is eligible for admission
# Total_marks=300
# print(f"Total_marks are {Total_marks}")
# Mathematics_marks=int(input("Enter the marks of mathematics:"))
# Physics_marks=int(input("Enter the marks of physics:"))
# Chemistry_marks=int(input("Enter the marks of chemistry:"))
# three_subject_marks=Mathematics_marks+Physics_marks+Chemistry_marks
# two_subject_marks=Mathematics_marks+Physics_marks

# if(Mathematics_marks>=65 and Physics_marks>=50 and Chemistry_marks>=50) and (three_subject_marks>=180 or two_subject_marks>=140):
#     print("Student is eligible")
# else:
#     print("student is not eligible")


