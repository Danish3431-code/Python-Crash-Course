# Question / Problem Statement: Create a console-based Expense Tracker
# program in Python that allows the user to record daily expenses and view
# summaries like total spending. Use only the concepts learned till Chapter 6
# (loops, conditionals, lists, dictionaries, and basic input/output).

# Project Details / Description:
# You are required to build a simple personal finance management tool.
# The program should allow the user to:
# ● Add an expense with details like date, category, description, and amount.
# ● View all recorded expenses in a clean format.
# ● Calculate total spending so far.
# ● Exit the program gracefully when the user chooses to.

expenses_list=[] #list of expenses in form of dictionary.
print("Welcome to Expense Tracker Aap")

while True:
    print("=====MENU=====")
    print("1. Add Expenses")
    print("2. View all Exapenses")
    print("3. Calculate Total Spending")
    print("4. Exit The Program")

    choice= int(input("Please Enter Your choice:"))

#1)Add an expense with details like date, category, description, and amount.
    if (choice==1):
        date= input("Enter the date:")
        category=input("Enter the Category (food, dress, tour etc:")
        description=input("Enter the description:")
        amount=int(input("Enter the amount:"))
        
        expense={
            "date": date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenses_list.append(expense)
        print("\n Done Bro. Expense is added successfully")

#2)● View all recorded expenses in a clean format.
    elif(choice==2):
        if(len(expenses_list) ==0):
            print("No expenses occur Yet")
        else:
            print("====This is your all expenses====")
            count=1
            for item in expenses_list:
                print(f"{count}->{item['date']},{item['category']},{item['description']},{item['amount']}")
                count=count+1

#3)● Calculate total spending so far.
    elif (choice==3):
        total=0
        for item in expenses_list:
            total=total+item["amount"]
        print("\n Total expense = ",total)

#4)Exit    
    elif(choice==4):
        print("Thankyou for using our system")
        break
    else:
        print("invalid choice")