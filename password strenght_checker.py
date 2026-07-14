# Password Strengthen Checker

import re

#password strength check conditions:
#min 8 characters, digit, uppercase, lowercase, special char

def password_check(password):
    if len(password) < 8: #length of password
        return "Weak: password must be at least 8 chars"
    
    if not any(char.isdigit() for char in password): # check is their any digit in it.
        return "Weak: password must contain a digit"
    
    if not any(char.isupper() for char in password): # check is their any uppercase in it.
        return "Weak: password must contain upper char"
    
    if not any(char.islower() for char in password): # check is their any lowercase in it.
        return "Weak: password must contain lower char"
    if not re.search(r"[!@#$%^&*()_\-+=\[\]{}\\|;:'\",.<>/?~`]", password): # check is their special charater in it.

        return "Password must contain at least one special character."
    
    return "Strong: your password is secured!" # show that password is strong.



def password_checker(): # check password until it match all conditions and become strong.
    print("Welcome to the password strength checker")


    while True:

        password=input("Enter your password (or type 'exit' to quit:)")

        if password.lower()=='exit':
            print("Thank you for using this tool")
            break

        result=password_check(password)
        print(result) #print the final strong password.

#Run the password checker tool

if __name__=="__main__":
    password_checker()
