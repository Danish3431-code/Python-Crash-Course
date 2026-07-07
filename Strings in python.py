#String in Python(PART:1)

# Operators   | Purpose

# concatination operator   (+)           | Used to join two or more strings
# repetation Operator      (*)           | Used to repeat a string multiple time.
# membership operator      (in)          | checks if a character or word present in a String.
# not  membership operator (not in)      | checks if a character or word is not present in a string.
# indexing Operator          []          | used to access a specific character.
# slicing Operator           [:]         | used to get part of a  string.


# EXAMPLE:
# name="Talha"
# print(name+ " Akram ") #concatination operator
# print(name * 2) #repetation operator
# print("Tal" in name) #membership operator
# print("Ali" not in name) # not membership operator
# print(name[0])#indexing operator
# print(name[0:5])#slicing operator


#String in Python(PART:2)

# String Indexing:
# Indexing means accessing one character from a string.
# python uses zero-based Indexing

# name="DANISH"
# D   A   N   I   S   H
# 0   1   2   3   4   5   


# Positive & Negative Index:

# name="DANISH"
#  D     A      N      I       S      H
#  0     1      2      3       4      5 -> Positive index
# -6    -5     -4     -3      -2     -1 -> Negative index

#  0 = first character
# -1 = last character

# String Slicing:
# slicing means taking a part of a string.

# string[start:end:step]

# start --> where to begin.
# end   --> where to stop (not include).
# step  --> how many positions to jump. 

name="Danish"
# print(name[0:2]) # D a
#                 #  0 1  
# # 2 is not included
# print(name[2:5]) # n i s
                 # 2 3 4
# 5 is not included


# print(name[:1]) # D      first  character
# print(name[:2]) # D a    first 2  character
# print(name[2:5])# n i s  third to fifth(not included) character
# print(name[-1:])#h       last character
# print(name[0::2])#Dns    every second character is not included.
# print(name[1:-1])#anis   exclude first & last character.
# print(name[::])#Danish   all characters
# print(name[::-1])#hsinaD reverse the string




# STRING METHODS:
# 1) len()
# return thr total number of characters in a string.
# name="Danish"
# print(len(name)) #6

# # spaces are also counted
# print(len("Hello world"))#11

# 2)Upper()
# convert all letters to UPPERCASE
# name="dansih"
# print(name.upper()) # DANISH

# 3) lower()
#  converts all letters tp lowercase
# name="TALHA"
# print(name.lower()) # talha

# 4)Strip()
# removes spaces from the beginning and end of a string.
# name="  Talha  "
# print(name.strip())#Talha

# 5) count()
# count how may times a character or word appears.
# text="banana"
# print(text.count("a"))#3
# print("Hello Hello".count("Hello"))#2

#6)find()
# finds the index(position) of a character or word.
# text="Python"
# print(text.find("h"))#3

# POSITION REFERENCE

# P   y   t   h   o   n
# 0```1```2```3```4```5`

# if not found:

# print("Python".find("z")) #-1 means not found


#7) title()
# Makes the first letter of each word capital\
# name="talha nadeem"
# print(name.title())#Talha Nadeem

# 8)Split()
# Converts a string into a list.
# text="Python  Java  C++"
# print(text.split())#['Python', 'Java', 'C++']

# EXAMPLE WITH COMMA.
# data="Ali, Ahmed, Talha"
# print(data.split(',')) #['Ali', ' Ahmed', ' Talha']


# 9)replace()
# replaces one word or character with another.

# text="I love Java"
# print(text.replace("Java","Python")) #I love Python