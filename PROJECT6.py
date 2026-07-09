#Library Managment system by using OOP concepts

# Create parent class

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

#Person object

# person1=Person("Danish",25)
# person1.show_info()

#Child class Student

class Student(Person):
    def __init__(self, name, age,roll_number):
        super().__init__(name, age)
        self.roll_number=roll_number
        self.issued_books=[]
    
    def student_info(self):
        self.show_info()
        print(f"RollNumber: {self.roll_number}")
        print(f"IssuedBook: {self.issued_books}")

#Student object

# student1=Student("Ali",25,3432)
# student1.student_info()

#Librarian Class

class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id=employee_id

    def librarian_info(self):
        self.show_info()
        print(f"EmployeeID: {self.employee_id}")

#librarian object

# librarian1=Librarian("Umer",35,101)
# librarian1.librarian_info()


#Book Class

class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.availability=True
    def book_info(self):
        print(f"BookID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {self.availability}")

#book object:

# book1=Book(100,"Python Basics","Rishab mishra")
# book1.book_info()

#library class

class Library:
    def __init__(self):
        self.books=[]
#add book

    def add_book(self):
        book_id=int(input("Enter the book id: "))
        title=input("Enter the book title: ")
        author=input("Enter author name: ")

        new_book=Book(book_id,title,author)

        self.books.append(new_book)

        print("Book added successfully!")

#View book

    def view_books(self):

        if len(self.books)==0:
            print("No books available.")
        else:
            print("=== Library Books===")

            for book in self.books:
                book.book_info()
                print("-" * 30)
# Issue Book
    def issue_book(self):

        book_id = int(input("Enter Book ID to issue: "))

        for book in self.books:

            if book.book_id == book_id:

                if book.availability:
                    book.availability = False
                    print("Book issued successfully!")

                else:
                    print("Book is already issued.")

                return

        print("Book not found.")


    # Return Book
    def return_book(self):

        book_id = int(input("Enter Book ID to return: "))

        for book in self.books:

            if book.book_id == book_id:

                if not book.availability:
                    book.availability = True
                    print("Book returned successfully!")

                else:
                    print("Book is already available.")

                return

        print("Book not found.")

#Menu
library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        library.issue_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")



