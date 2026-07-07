# OOP(Object Oriented Programming) IN PYTHON:

# TWO WAYS TO WRITE PYTHON CODE

# 1)Procedural Programming:

# write code step by step.
        # Input
        #   |
        # Process
        #   |
        # Output

# 2)OOP(Object-Oriented Programming)

# OOP=A way of writing code using classes and object.

# Think of real-life things:

# Student
# Car
# Mobile
# Laptop

# What is a Class?
# A Class is a blueprint or template.
# It tells us:
# 🔘What data an object will have.
# 🔘What work an object can do.

# Example:
# class=Car
# It is only the design, not a real car.

# What is an Object?
# An Object is the real thing created from a class.

# Example:
# class=car

# objects:
# BMW
# Honda
# Toyota.

# All are different cars (objects),but all come from the same class.

# Easy Example:
# class=Student

# Objects:
# Ali
# Ahmed
# Usman

# Every Student has:
# Name
# Age
# Marks

# But every student has different values.

# Simple Formula

    # class
    #    | 
    # creates
    #    |
    # object


# WHY USE OOP?

# 1)Easy to understand
# Works like real life.
# 2)Reuse code
# Write one class.
# Create many objects.
# 3)Easy to update
# Change the class once.
# All objects get the update.
# 4)Organized Code
# Keeps related code together.

# Memory Trick

# class=Blueprint
# object=Real Thing

# or

# class=Design
# object=Product


# The Easiest Sentence to Remember:

# A class is the blueprint, and an object is the real thing made from that blueprint. One class can create many objects


# Write a Python program to: 
# 1.  Define a Student class with attributes name, grade, percentage, and team. 
# •  Include an __init__ method to initialize these attributes. 
# •  Add a method student_details that prints the student’s details in the format: 
# "<name> is in <grade> grade with <percentage>%, from team <team>". 
# 2.  Create two teams (team1 and team2) as string variables. 
# 3.  Create at least two student objects, each belonging to one of the teams. 
# 4.  Call the student_details method for each student to display their details.

                              
# class Student: #Class
#     def __init__(self,name,grade,percentage,team):#__init__ method (Constructor) to initialize these attributes
#          #functions in class is called methods 
#         self.name=name #attribute
#         self.grade=grade #attribute
#         self.percentage=percentage #attribute
#         self.team=team #attribute
    
#     def student_details(self): #functions in class is called methods 
#         print(f"{self.name} is in {self.grade} grade with {self.percentage}%, from team {self.team}")
# team_1="A"
# team_2="B"
# subject1=Student("Ali",12,90,team_1) #Objects
# subject1.student_details()
# subject2=Student("Ahmed",11,88,team_2) #Objects
# subject2.student_details()




# ABSTRACTION IN PYTON: 
# Hiding unnecessary details

# Abstraction hides implementation details and shows only the relevant functionality to the 
# user. 
                      
# class Student: #Class
#     def __init__(self,name,grade,percentage,team):#__init__ method (Constructor) to initialize these attributes
#          #functions in class is called methods 
#         self.name=name #attribute
#         self.grade=grade #attribute
#         self.percentage=percentage #attribute
#         self.team=team #attribute
    
#     # This is abstraction example: want to add 2% grace marks to each student but i didn't want that student know this so that i can use abstraction

#     def student_details(self): #functions in class is called methods 
#         print(f"{self.name} is in {self.grade} grade with {self.percentage+2}%, from team {self.team}") #this is abtraction hidden from user.
# team_1="A"
# team_2="B"
# subject1=Student("Ali",12,90,team_1) #Objects
# subject1.student_details()
# subject2=Student("Ahmed",11,88,team_2) #Objects
# subject2.student_details()

# ENCAPSULATION IN PYTHON:

# Encapsulation means keeping data safe by not allowing direct access to it. INstead of changing the data directly. we use methods(fucntions) to access or change it.

# Real life Example: Car

# steering
# Brake
# Accelerator

# You do not touch the engine directly. The engine is hidden and protected. This is Encapsulation. 

# Real life Example: TV

# you use remote to:
# change the channel
# Increase the volume

# you don't open the Tv and change things inside it.
# The inside is protected. This is Encapsulation.

# PYTHON EXAMPLE:

# Imagine:

# Student Marks = 90

# ❌ Without Encapsulation:

# Anyone can change it to:

# Marks = -50

# which is wrong.

# ✅ With Encapsulation:

# Want to change marks?
#         ↓
# Use a method
#         ↓
# Method checks if marks are correct
#         ↓
# If correct → Save
# If wrong → Don't save
# Why Use Encapsulation?
# ✔ Keeps data safe.
# ✔ Prevents wrong values.
# ✔ Gives controlled access to data.
# Memory Trick
# Encapsulation

# =

# Hide Data
# +
# Access through Methods

# One-Line Definition

# Encapsulation means hiding data and allowing it to be used only through methods.

# Mean's give control access to user.

# private attribute ko access kerna ka liya method bnate hen.

# private attribute ko access ker na ka liya jo method create karo ga us ka name get word sa start hona cahiya.


# class Student: #Class
#     def __init__(self,name,grade,percentage,team):#__init__ method (Constructor) to initialize these attributes
#          #functions in class is called methods 
#         self.name=name #attribute
#         self.grade=grade #attribute
#         self.__percentage=percentage #Private attribute
#         self.team=team #attribute
#     def get_percentage(self):
#         return self.__percentage

#     # This is abstraction example: want to add 2% grace marks to each student but i didn't want that student know this so that i can use abstraction

#     # def student_details(self): #functions in class is called methods 
#     #     print(f"{self.name} is in {self.grade} grade with {self.__percentage}%, from team {self.team}") #this is abtraction hidden from user.
# team_1="A"
# team_2="B"
# subject1=Student("Ali",12,90,team_1) #Objects
# # subject1.student_details()
# subject2=Student("Ahmed",11,88,team_2) #Objects
# # subject2.student_details()

# print(subject1.get_percentage()
# )
# print(subject2.get_percentage())

#INHERITANCE
# Allows one class (child) to reuse the prop and methods of another class (parent).

# # This is parent class
# class Student: 
#     def __init__(self,name,grade,percentage,team):
#         self.name=name 
#         self.grade=grade 
#         self.__percentage=percentage 
#         self.team=team 
#     def get_percentage(self):
#         return self.__percentage


#     def student_details(self): 
#         print(f"{self.name} is in {self.grade} grade with {self.__percentage}%, from team {self.team}") 
# team_1="A"
# team_2="B"
# subject1=Student("Ali",12,90,team_1) 
# # subject1.student_details()
# subject2=Student("Ahmed",11,88,team_2) 
# # subject2.student_details()

# print(subject1.get_percentage()
# )
# print(subject2.get_percentage())

# class GraduateStudent(Student): #GraduateStudent is a child class which inherit prop and methods from  Student parent class.
#     def __init__(self, name, grade, percentage, team,stream): #parameters from parent class and parameters in child class.
#         super().__init__(name, grade, percentage, team)
#      #super word iss liya use ker rha han kun ka iss ki jo parent class ha wahan sa muja detail cahiya.
#         self.stream=stream #new attribute in child class
    
#     def student_details(self):
#         super().student_details()#method inherit from parent class
#         print(f"stream is {self.stream}")
        
# #Object
# Grad_Student1=GraduateStudent("Usman",12,97,"C","CS")
# print(Grad_Student1.name)
# print(Grad_Student1.grade)
# print(Grad_Student1.get_percentage())
# print(Grad_Student1.team)
# print(Grad_Student1.stream)

# Grad_Student1.student_details()




#POLYMORPISM:

# Polymorphism = Same method , different work.

# SIMPLE LOGIC

# One Method
#     |
# Different objects
#     |
# Different output

# Example:

#      Dog
#       |
#     sound()
#       |
#      Bark

#     Cat
#      |
#    sound()
#      |
#     Meow

#      Cow
#       |
#    sound()
#       |
#      Moo

# Method name is the same: sound()
# Output is different

# This is Polymorphism


# REAL LIFE EXAMPLE:

# socho tumhare pass:

# CAR
# BIKE
# BUS

# Sab main ek function hai:
# start()

# CAR:
#    start()
#      |
#   Engine start

# BIKE:
#    start()
#      |
#   Bike start

# BUS:
#    start()
#      |
#   Bus start

# function ka name same hai:
#  start()

# lekin har vehicle apne hisaab se kaam karta hai.

# ya Polymorphism hai.

# MEMORY TRICK:

#     same method
#         |
#  Different objects
#         |
#  Different Behaviour


# One-line Definition:

# Polymorphism means the same method perform different actions for different objects.

# LOGIC BUILDER:


# whenever you hear Polymorphism, think:
#     sound()
#     Dog -> Bark
#     Cat -> Meow
#     Cow -> Moo

# Same method 
# Different objects
# Different output
# =Polymorphism


# PARENT CLASS:

# class Student: 
#     def __init__(self,name,grade,percentage,team):
#         self.name=name 
#         self.grade=grade 
#         self.__percentage=percentage 
#         self.team=team 
#     def get_percentage(self):
#         return self.__percentage


#     def student_details(self): 
#         print(f"{self.name} is in {self.grade} grade with {self.__percentage}%, from team {self.team}") 
# team_1="A"
# team_2="B"


# #CHILD CLASS:

# class GraduateStudent(Student): #GraduateStudent is a child class which inherit prop and methods from  Student parent class.
#     def __init__(self, name, grade, percentage, team,stream): #parameters from parent class and parameters in child class.
#         super().__init__(name, grade, percentage, team)
#      #super word iss liya use ker rha han kun ka iss ki jo parent class ha wahan sa muja detail cahiya.
#         self.stream=stream #new attribute in child class
    
#     def student_details(self): # this is method
#         print(f"{self.name} is in class {self.grade}, and in team {self.team} and from stream  {self.stream}")
#         print("same method with different output")
        
# #Object - student class
# subject1=Student("Ali",12,90,team_1) 

# #object - GraduateStudent class
# Grad_Student1=GraduateStudent("Usman",12,97,"C","CS")

# subject1.student_details()
# Grad_Student1.student_details()

