# import cv2
# import math

# print("hello world")
# print(math.gcd(3,6))

# print(3+8)
'''
this is a multiline comment
'''
# if(age<18):
#     print("hello")
a = 9
b = "jkl"
c = 45.2
# print(a+c)
# determines the datatype
# typeA = type(a)
# print(typeA)
str = "31"
#  type casting
# str = int(str) 
# str = float(str)
# print(type(str));

#  multiline string
# name = ''' Arry
# is a good girl'''
# print(name)

# name = "Arry"
#printing index at ith element
# print(name[0])
#printing the substring from 1 to 2
# print(name[1:3])

name = "Arry"
# print(name)
# cut spaces from start and end
# print(name.strip())
# length of name
# print(len(name))
#converting into lower and upper string
# var = name.lower()
# var = name.upper()
# as the name suggests it replaces the word
# var = name.replace("r","t")
# name = "arry, fairy"
# var = name.replace(","," is")
# print(var)

#concatenate two strings
# stri = "this is a "
# stri2 = "this is not a"
# print(stri+stri2)

#creating templates int string
# name1 = "Fairy"
# name2 = "Arry"
# temp = "Her name is a {} and she is a good girl named {}".format(name1,name2)
# # for adla badli
# temp = "Her name is a {1} and she is a good girl named {0}".format(name1,name2)
# #use of f string
# temp = f"Her name is a {name1} and she is a good girl named {name2}"
# print(temp)
'''
##operators
1.** exponenetiation operators
2.// floor division operators
3.% modulo operator 
'''
'''
python collectors:
1.List 
2.Tuple
3.Set
4.Dictionary
'''
#1.LIST
# ordered and changable collection
# lst = [1,2,34,5]
# var = type(lst)
# var = lst[2]
# lst[2]=9
# var = lst[2]
#add elements from back
# lst.append(99)
# for inserting element
# lst.insert(1,3)
# remove elements
# lst.remove(3)
#pop elemnet: to remove element from end
# lst.pop()
# delete element using index
# del lst[3]
#deletes the whole list
# del lst
# clearing elements from list
# lst.clear()
# var = lst
# var= len(lst)
#prints element from 1 to 3
# var = lst[1:4]
# print(var)

# 2.TUPLE

#cannot change tuple items

# a = ("arry","fairy","airy")
# var = a
# type casting
# a = list(a)
# var = type(a)
# a[0] = "lala" tupe value cannot be changed
# print(var)

#  Set

#does not repetittion of elements 
# s1 = {1,1,1,2,2,3,3,4,4,5,3,634}
#to add only 1 element
# s1.add(99)
#to add a list of elements
# s1.update([66,44,5,222])
#to print length
# print(len(s1))
# to remove elements
#if element not present it will give error
# s1.remove(1)
# this willl not give error if element ids not present
# s1.discard(33)
'''
# more functions 
# .pop,.clear,.del,.union.intersection
'''
# print(s1)

# 4. DICTIONARY
# key value pair

# ArryDict = {
#     "Name" : "Arry",
#     "Class" : "3rd",
#     "Marks" : 40,
#     "Hours in School" : 6,
# }
# ArryDict["Marks"] = 50 
# ArryDict.pop("Marks")
# more operators
# del,clear,pop,update
# print(ArryDict)
# print(ArryDict["Name"])

# eif elif ladder
# age = 34
# input function reads 
# age = input("enter your age\n")
# will give string as type
# print(type(age))
# to convert string into int
# age= int(age)
# will give int as type
# print(type(age))

# if(age>18):
    # print("you r eligible to vote")
# elif(age==18):
    # print("you are a responsible teenager")
# else:
    # print("not eligible to vote")

# Loops:
# ques :print numbers from 1 to 100
# wil start from 0 and end at 99
# for i in range(0,100):
#     print(i)

# iteration in list
# li = [1,42,"arry"]
# for i in li:
#     print(i)
# quiz: use loop to iterate dictionary, set and tuples

# while loop
# i = 0
# while(i<10):
#     i+=1
#     if(i==7):
#         # break
#         continue
#     print(i)

# Functions:
# def greet():
#     print("good morning sir")
# greet()

# def sum(a,b):
#     return a+b
# print(sum(1,2))

class Employee:
    # constructor to initialise
        def __init__(self,aname,asalary):
            self.name = aname
            self.salary = asalary
arry = Employee("Arry",7)
print(arry.name)
print(arry.salary)
