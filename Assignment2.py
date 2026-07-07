
# Assingment # 2

# Question 1: Write  a program to input student name and marks of 3 subjects. 
# Print name and percentage in output.

# Student_Name=input("Enter the Name: ")
# Total_Marks=300
# Sub_Urdu= 79
# Sub_English= 85
# Sub_Math= 70
# Percentage=((Sub_Urdu+Sub_English+Sub_Math)/Total_Marks)*100
# print(f"Student Name is: {Student_Name}")
# print(f"Your percentage is: {int(Percentage)}%")

#Question 2: Write a program that collects multiple types of data(eg. name, age, height and student status).
# from user input, stores data into the dictionary, and then prints out the collected data.

User_Data={}
User_Data['name']=input("Enter your Name: ")
User_Data['age']=int(input("Enter your age: "))
User_Data['height']= float(input("Enter your height:"))
User_Data['student']=input("Are you a student (Yes/No)")
print(User_Data)
