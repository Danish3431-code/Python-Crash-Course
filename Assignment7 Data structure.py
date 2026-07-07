#ASSIGNMENT # 7:
#DATA STRUCTURES IN PYTHON(LIST,TUPE,SET,DICT)

# Q1) Find the Intersection(commom elementss) of Two lists.

# Method:1

# list1=[2,4,6,8,3,1]
# list2=[5,4,1,3,7,6]
# blank_list=[]
# for num in list1:
#     if num in list2:
#         blank_list.append(num)
# print(blank_list)#[4, 6, 3, 1]

# Method:2

# list1=[2,3,5,6,7,8]
# list2=[3,4,6,7,2,1]
# list3= list(set(list1)&set(list2))
# print(list3)#[2, 3, 6, 7]


# Q2) Find the most frequent Element in a list?

# Method:1

# list1=[1,2,2,3,3,3,4]
# max_count=0
# max_freq=None
# for num in list1:
#     count=list1.count(num)
#     if count>max_count:
#         max_count=count
#         max_freq=num
# print(list1)#[1, 2, 2, 3, 3, 3, 4]
# print(max_freq)#3


# Method:2

# list2=[1,2,2,3,3,3,4,4,4,4]
# max_frequent_number=max(set(list2),key=list2.count)
# print(max_frequent_number)#4


# Q3) Find Cummulative sum of a list?

# Method:1(Best method is this)

# list3=[1,3,4,5,7]
# total=0
# result=[]
# for num in list3:
#     total=total+num
#     result.append(total)
# print(result) #[1, 4, 8, 13, 20]


# Method:2

# list2=[1,3,4,5,7]
# result=[sum(list2[:i+1]) for i in range(len(list2))]
# print(result)#[1, 4, 8, 13, 20]


# Q4) Remove duplicates from a list.

# Method:1

# list1=[1,1,2,2,3,3,3,4,4,4,4]
# duplicate_remove= list(set(list1))
# print(duplicate_remove)

# Method:2

# list2={1,1,2,2,3,3,4,4,5,5}
# result=[]
# for item in list2:
#     if item not in result:
#         result.append(item)
# print(result)


# Q5) Find index of an element in a tuple.

# Method:1

# typle_1=(1,2,3,4,5)
# find_index=typle_1.index(2)
# print(find_index)

#Method:2 (by using function)

# my_tuple=(6,7,8,9,10)
# def find_index(tup,elem):
#     return tup.index(elem) if elem in tup else -1
# print(find_index(my_tuple,100))


# Q6  Find the most frequent value in the dictionary 

# marks = {
#     "A": 10,
#     "B": 20,
#     "C": 10,
#     "D": 30,
#     "E": 10
# }
# freq={}
# for value in marks.values():
#     if value in freq:
#         freq[value]+=1 #freq[10]=1+1=2, freq[10]=1+1+1=3
#     else:
#         freq[value]=1 #freq[20]=1,  freq[30]=1, 
# print(freq)


# Q7) Merge dictionaries with summition.

# Mehtod:1

# dict_1={"a":10,
#         "b":20,
#         "c":30}

# dict_2={
#     "b":15,
#     "c":35,
#     "d":25
# }

# result=dict_1.copy()
# for key, value in dict_2.items():
#     if key in result:
#         result[key]+=value
#     else:
#         result[key]= value

# print(result)


# Method:2

# dict_1={"a":10,
#         "b":20,
#         "c":30
# }
# dict_2={
#     "b":30,
#     "c":35,
#     "d":40
# }

# def merge_dict(dict_1,dict_2):
#     result=dict_1.copy()
#     for key,value in dict_2.items():
#         if key in result:
#             result[key]+=value
#         else:
#             result[key]=value
#     return result
# print(merge_dict(dict_1,dict_2))



# Q8) Flatten a nested ditionary?

# Example:1

# data={
#     "name":"ali",
#     "marks":{
#         "math":90,
#         "english":80
#     }
# }

# result={}
# for key,value in data.items():
#     if type(value)==dict:
#         for inner_key,inner_value in value.items():
#             result[inner_key]=inner_value
#     else:
#         result[key]=value

# print(data)
# print(result)


# Example:2

# data={
#     "a":{
#         "b":{
#             "c":42
#         },
#         "d":7
#     },
#     "e":10
# }

# def flatten_dict(data,path=""):
#     for key,value in data.items():
#         if isinstance(value,dict):
#             flatten_dict(value,path+key+".")
#         else:
#             print(path+key,"=",value)
# flatten_dict(data) #a.b.c = 42
#                    #a.d = 7
#                    #e = 10

# Q9) Sort the dictionary by values.

# Example:1

# marks={"Ali":65,"Ahmed":70,"Umer":80}
# sorted_marks= dict(sorted(marks.items(),key=lambda item:item[1]))
# print(sorted_marks)#{'Ali': 65, 'Ahmed': 70, 'Umer': 80}


# Example:2   reverse=True

# marks={"Danish":89,"Talha":85,"Haider":84}
# sorted_marks= dict(sorted(marks.items(),key=lambda item:item[1], reverse=True))
# print(sorted_marks) #{'Danish': 89, 'Talha': 85, 'Haider': 84}