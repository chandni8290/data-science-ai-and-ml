# print("hello")
# a = "hello"
# num = 10

# age = 23
# age = 24
# print(age)
# print(age)
# name = "chandni"
# print(name)
# print("my name is",name)
# print("name dtype:-",type(name))
# print("len of name:-",len(name))
# ###indexing
# print(name[0])  
# # print(name[1])
# print(name[len(name)-1])
# name = "chandni"

# ###slicing in python
# name = "chandni"
# print(name[0:3])

# ###operation

# name = "chandni"
# last = " sahu"
# upper_case = name.upper()
# print(upper_case)
# lower_last_name = last.lower()
# print(lower_last_name)
# print(name.count("n"))
# name = "chandni"
# last = " sahu"
# print(name.title())
# print(name.capitalize())
# print(name+last)


# reversed_name = name[::-1]
# print(reversed_name)

# # for line in reversed(name):
# #     exec(line)

#######>>>>>>>>>>>>List>>>>>>>>>>>>>
# list


# lst = [1,2,3,4,5,6,7,"rohit",2.3]

# 
# mutanble
# duplicated values
# order 
# herto

###array>>>>  lst = [1,2,3,4,5,6,7]
#array
# print("my first list:-",lst)
# print("len of list:-",len(lst))
# print("type of list:-",type(lst))
# print(lst[0])

# print(lst[0:5])
#lst = [1,2,3,4,5,6,7,2.3]
#lst.pop()
#print(lst)
# lst.append(100)
# print(lst)
# lst.insert(0,1000)
# print(lst)
# copy_lst = lst.copy()
# print(copy_list)
# lst.reversed()
# lst.remove(2.3)
# print(lst)
# lst.sort()
#########>>>>>>>>>>>tuple>>>>>>>>>>>>.


#tpl = (1,2,3,4,5,6,"chandni",2.3)
# print("my first tuple:-",tpl)
# print("len of tuple:-",len(tpl))
# print("type of tuple:-",type(tpl))
# print(tpl[0])
# print(tpl[2])
# print(tpl[0:8])
# #build
# a = 1,2,58,5,58,5,5,85,2
# print(a)
# print(len(a))
# print(type(a))

# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)


# lst = [1,2,3,4,[5,6],7]
# print(lst)
# print(lst[4][0])
# print(lst[4][1])

# tpl = (1,2,58,2,8)
# print("max of tuple",(tpl))
# print("min of tuple",tpl)
# sum(tpl)


#>>>>>>>>>dictionary>>>>>>>>>>>>>>>>>>


# my_dict = {
#     "name":"monika",
#     "class":"2nd year",
#     "roll number":"12345",
#     "adderss":"jaipur"##### name item h
# }
# print("my first dict:-",my_dict)
# print("len of dict:-",len(my_dict))
# print("type of dict:-",type(my_dict))

# print(my_dict['name'])
# print(my_dict['class'])
# print(my_dict['roll number'])
# print(my_dict['adderss'])

#my_dict['adderss'] = "beawar"
#print(my_dict)
# my_dict  {
#     "name":"monika",
#     "class":"2nd year",
#     "roll number":"12345",
#     "adderss":"jaipur"
# }
# my_dict['branch']="it"
# print(my_dict)


# tast1 >>>>>>>>>>> update funcion use
# get function >>>>>> 5 example or[]

# my_dict.keys()
# my_dict.values()
# my_dict.item()


# copy_dict=my_dict.copy()
# print(copy_dict)
# my_dict.clear()


# a=input("enter a number")
# b=input("enter second number")
# print(a)
# print(type(a))


#type casting
# a=int(input("enter a number"))
# b=int(input("enter second number"))
# print(a*b)

# lst = [1,2,3,4,5,6]
# print("this is my list:-",lst)
# print("type of list:-",type(lst))
# tpl = tuple(lst)
# print("this is my tuple:-",tpl)
# print("type of tuple:-",type(tpl))

#>>>>>>>>>set>>>>>>>>>>>>


# my_set ={1,2,3,4,5,6,"chandni"}
# print("this is my first ser:-",my_set)
# print("len of my set:-",len(my_set))
# print("type of set:-",type(my_set))

# tast
# my_set.union()
# my_set.intersection()
# my_set.difference()
#####operator
# lst=(my_lst)
# lst.append(1000)
# print(set(lst))


# color = input("enter the traffic light color (red,yellow,green):").lower()
# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("wait")
# elif color == "green":
#     print("go")
# else:
#     print("invalid color entered.")


# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# if a>b:
#     print("largest number is:",a)
# elif b>a:
#     print("largest number is:",b)
# else:
#     print("both number are equal.")


# year = int(input("\nEnter a year to check leap year:"))
# if(year % 4 == 0 and year % 100 != 0)or (year % 400 == 0):
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")



# num = int(input("\nEnter a number to check even and odd:"))
# if num % 2 == 0:
#     print(num,"is even")
# else:
#     print(num,"is add")


# marks = int(input("\nEnter your marks (0-100): "))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=60:
#     print("Grade C")
# else:
#     print("Grade D")


# while loop 

# a = 20
# while a>10:
#     print(a)
#     a = a+1


# while True:
#     print("hello")


# def function_name():
#     pass
# function_name()



# def display():
#     print("hello")
# display()


# def add():
#     a = 10
#     b = 20
#     print(a+b)
# add()

# argument and parameter

# def add (a,b):
#     print(a+b)
# add(a=10,b=20)


# def display(name, age ,address ="jaipur"):
#     print(f"msy name is {name}and my age  {age}and my addres {address}")
# display("chandni",19)


# function two type
# user define
# predefine function

#lambda fuctiom
# use small tasks

# lambda is anonymous function
# single license
# sfort function
# one line 


# add = lambda a,b:a+b
# add(10,20)

# square = lambda a : a**2
# square(10)

# oops concept in python


# global
# local variable


# ploymorphism
# inheritence
# encapsulation
# abstraction


# class Class_name:
#     pass
# class is keyword
# class Student:
#     name = "chandni"
#     age = 19
#     print(f"my name is{name} and my age ")

