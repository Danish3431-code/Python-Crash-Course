
# Input Function 

# 1. input() takes input from the user.
# 2. input data type is always string.
# 3. convert data type before calculation.
# 4. "10" + "5" is "105"
# 5. 10 + 5 is 15


# Write a program to input student name and marks of 3 subjects. 
# print name and percentage. 

name=input("Enter the name: ")
math=90
urdu=79
English=80
totalmarks=300
percentage=(math+urdu+English)/totalmarks*100
print("name of student is ",name)
print("and his percentage is", percentage )
