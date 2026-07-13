# file Handling
 
# mode: r - read, w - write, a - append


# WORKING ON R--READ: 

# Open file

# file= open("example.txt" , "r")

# Read entire file

# file=open("example.txt","r")
# content=file.read() # read entire data
# print(content)  #Hello Danish!
#                 #kaise ho?
#                 #Acha hon.

# file.close() # best practice


#Read one line

# file=open("example.txt",'r')
# content=file.readline()
# print(content) #Hello Danish!
# file.close()


#Read lines give data in the list format.
 
# file=open("example.txt","r")
# content=file.readlines() #list entire data
# print(content) #['Hello Danish!\n', 'kaise ho?\n', 'Acha hon.']
# file.close()

# give error if file doesn;t exist


# WORKING ON W--WRITE:
# create the new file if file doesn't exist
# like:

# file=open("example2.txt",'w') #create a new file

# #append(add) data into the file that you created

# file.write("Aslamualikum! kesa ho tum?") # w mode overwrite the data.

# #to avoid overwrite we use 'a'  append mode value ok incremental add kerta ha.

# file.write("\nTheek hon ma tum kesa ho!")

# file.close()


#CLOSE A FILE 
# USING 'with' STATEMENT: help you jo bi oeration perform karo wo successfully close ho jaye.

# with open('example2.txt','r') as file:
    # content=file.read()
    # print(content) Aslamualikum! kesa ho tum?
    #                Theek hon ma tum kesa ho!

    # content=file.readline()
    # print(content) Aslamualikum! kesa ho tum?

    # content=file.readlines() 
    # print(content) ##['Aslamualikum! kesa ho tum?\n', 'Theek hon ma tum kesa ho!']


#Working with Difft Format Files 

# csv - Using csv module  

# import csv  
# file = open('file.csv', mode='r')  
# reader = csv.reader(file) 

# csv - Using pandas library
 
# import pandas as pd  
# df = pd.read_csv('file.csv') 

# excel - Using pandas library 

# import pandas as pd  
# df = pd.read_excel('file.xlsx') 


# PDF Using PyPDF2 library:  

# import PyPDF2  
# file = open('file.pdf', 'b')  
# pdf_reader = PyPDF2.PdfReader(file)