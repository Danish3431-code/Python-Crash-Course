# STUDENT MANAGEMENT SYSTEM:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        print(f"Name: {self.name} , Age: {self.age}")


class Student(Person):
    def __init__(self, name, age,rollnumber,marks):
        super().__init__(name, age)
        self.rollnumber=rollnumber
        self.marks=marks
    
    def show_student(self):
        self.display_info()
        print(f"Roll: {self.rollnumber}, marks: {self.marks}")

class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject=subject
        self.salary=salary
    
    def show_teacher(self):
        self.display_info()
        print(f"subject: {self.subject}, salary: {self.salary}")



s1=Student("Danish", 25, 3431, 750)
t1=Teacher("Sir Naeem", 42,"Math",50000)

print("Student detail")
s1.show_student()
print("Teacher detail")
t1.show_teacher()








