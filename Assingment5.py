# String Practice Question

# Question:1
# Limit the decimal places to 2 digits using .format() method and print result, for the variable pi = 3.14159265359.

# pi=3.14159265359
# # print(round(pi,2))

# print("value of pi {:.2f}".format(pi))
# solve by using f-string method
# print(f"value of pi {pi:.2f} solve by using f-string method")


# Question 2

# Extract characters from the index 2 to 8 with a step of 2: Given my_string="Python Course", slice characters from index 2 to 8, skipping every other char.
              #012345678   
# my_string = "Python Course"
# #string[start:stop:step]
# print("outut after skipping evey 2nd charcter is:", my_string[2:8:2])


#Question 3
# slice to get only middle character(s): For string="Danish", use slicing to extract the middle character(s).

# string="Danish" #6 chars -even
# #index->012345
# string2="Wolverine" #9 chars-odd
# # index->012345678
# def extract_middle_character(word):
#     # find the length of word by using len() function
#     middle=int(len(word)/2)
#     if len(word)%2==0:         #even char len
#         return word[middle-1 : middle+1] #2:4
#     else:                      #odd char len   
#         return word[middle]
# print(extract_middle_character(string)) # even char 
# print(extract_middle_character(string2)) # odd char


#Question 4
# Remove the first 3 and last 3 characters: Given string="Regression Analysis", remove the first 3 and last 3 characters.

# string="Regression Analysis"
# # remove first 3 and last 3 characters
# print(string[3:-3])


#Question 5
# Get the substring that starts 4 characters from the end to the last character: for string="Classification", slice the string starting from the 4th character from the end to the last character
# string="Classification"
# print(string[-4:])

# also solve with this:
# print(string[10:])


#Question 6
# How to Reverse a String Using Python String Method?
# string="Python"
# # by using [start:end:step]
# print(string[::-1])


#Question 7
# write a Python function to check if a string  is a palindrome using string methods.

# string="madam"
# string2="Danish"
# def check_word_is_palindrome(word):
#     if word==word[::-1]:
#         print(f"{word} is a palindrome")
#     else:
#         print(f"{word} is not a palindrome")
# check_word_is_palindrome(string)
# check_word_is_palindrome(string2)

#Question 8
# Difference Between find() and index() in Python?

# Both are used to find the position(index) of a character or word in a string.

# => find(): returns the position if found.
#          : Returns -1 if not found

# text="Python"
# print(text.find("t")) #2
# print(text.find("z")) #-1

# =>index():return the position if found.
#          :Gives the error if not found.

# text="Python"
# print(text.index("t")) #2
# print(text.index("z")) #ValueError: substring not found


#Question 9
# Efficient String Concatenation method: Why is using join() often more efficient than using + for string concatenation in a loop? 
#  join()  is more efficient because it combines all strings in a single operation while + creates a new string every time in a loop, making its slower and less memory efficient.

# Easy real life Example:
# Imagine you want to join 100 papers

# using +

# 📃 + 📃 -> new stack

# 📃📃+📃-> new stack

# 📃📃📃+📃-> new stack

# again and again, lots of work.

# using join()

# 📃📃📃📃📃

# join all papers once less work,faster


