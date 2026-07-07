#Operators In Python

# 1.Arithmetic Operators

# Arithmetric operators are used with numeric values to perform mathmetical operations such as addition, 
# subtraction, multiplication and division

# a=5
# b=3
# print(a+b) #additional operator
# print(a-b) #subtraction operator
# print(a*b) #multiplication operator
# print(a/b) #division operator
# print(a%b) #modulus operator(give remainder)
# print(a//b) #floor division operator(give integer)
# print(a**b) #Exponentional operator


# 2.Comparison(Relational) Operators

# Comparison Operators are used to compare two values
# and return a Boolean result(True or False) 

# a=5
# b=3
# print(a==b) # Equal Operator
# print(a!=b) #not Equal
# print(a>b) #Greater than
# print(a<b) #Lesser than
# print(a>=b) #Greater than or equal to
# print(a<=b) #Lesser than or equal to


# 3. Assingment Operators

# Assignment operators are used to assign values to variables.

# a=5
# print("a value is: ",a) 

# a+=3
# print("a value is: ",a)

# a-=3
# print("a value is: ",a)

# a*=3
# print("a value is: ",a)

# a/=3
# print("a value is: ",a)

# a%=3
# print("a value is: ",a)

# a//=3
# print("a value is: ",a)

# a**=3
# print("a value is: ",a)

# a&=3    
# # because it is a bitwise & operator value of a=5 in bit=0101 and value of a&=3 is equal to 0011 in bit so it gives 0001  answer in bit because when both are 1 1 it give 1 otherwise it gives 0.
# # 5=0101
# # 3=0011
# # ------
# #   0001
# print("a value is: ",a)

#4. Logical Operators

# logical operators used to combine conditional statements.
# (Two statements ka dermayan comparison kerna ka liya use hota ha)

# 'and' operator
# Rules for and operator:
# 1.True+True=True
# 2.True+False=False
# 3.False+False=False

# a=10
# b=20
# print(a>10 and b<10)
# print(a==10 and b==20)

# 'or' operator
# Rules for or operator
# 1.True+False=True
# 2.False+True=True
# 3.False+False=False
# 4.True+True=True

# a=10
# b=20
# print(a>10 or b==20)


# 'not' operator

# Rules for 'not' operator
# 1. reverse the result
# 2. return false if the result is true
# 3. return true if the result is false

# a=10
# b=20
# print(not(a==10 and b==20))


# 5.Identity operator

# # 'is' operator
# x=[1,2,3]
# y=x
# z=[1,2,3]
# print(x is y) #first object ko hum na two names assign kiya han x and y is liya x =[1,2,3] and y=x and dono ka memory location same ha

# print(y is z) #z wala object ma values same han but object different ha and memroy location bi change ha.

# # 'is not' operator
# print(x is not z) #we check that the x and z are not same, if it gives true it means its memory location is different 
                  #and if it gives false then it means its memory location are same


# 6. 'membership' operator 

# 'in' operator checks value exist in the sequence

# my_list=['apple','mango','orange']
# # print('apple' in my_list) # return true if value is present in the sequence
# # print("apple2" in my_list) # return flase if value is not present in the sequence.


# # 'not in' operator checks value does not exist in the sequence

# print('cherry' not in my_list) # return ture if the value is not exist in the sequence.


# 7. 'Bitwise' operators
# (&) Operator:
# return True if both bits are True same as AND Operator

# 1=True
# 0=False

# a=5 # value of 5 in bit= 0 1 0 1
# b=3 # value of 3 in bit= 0 0 1 1
# print(a&b) #output is 1 in bit= 0 0 0 1


#(|)OR Operator:
# agar ek bhi True ho tou result True  ho ga.  
#sirf dono False hon tou result False ho ga.   
# 1=True
# 0=False



# a=7 #value of 7 in bit= 0 1 1 1
# b=4 #value of 4 in bit= 0 1 0 0
# print(a|b) #output is 7 in bit= 0 1 1 1



#(^) XOR Operator:
#same bit=0
#different bit=1
# 1=True
# 0=False


# a=6 #value of 6 in  bit is 0 1 1 0 
# b= 9 #value of 9 in bit is 1 0 0 1
# print(a^b)#output is 15 in bit 1 1 1 