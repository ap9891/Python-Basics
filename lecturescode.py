# import os
#lists all the files in computer


# def mostimpfunction():
    # print("Arry is coder")

# print(__name__)
# this function prints main and indicates that the function below is called in main file in which it is declared 
# def main():
    # print(os.listdir("/"))
# this helps in printing 
# if(__name__=="__main__"):
    # print(os.listdir("/"))
    # main()

# def function(name,age,rollno):
#     print("name ",name," age ",age," roll no ",rollno)
# function("Arry",15,9)

# args

# def function(*args):
#     # list ki tarah stoe ho jaate func arguments in agrs
#     # class<'tuple'>
#     print(type(args))
#     if(len(args)==3):
#         print("name ",args[0]," age ",args[1]," roll no ",args[2])
#     else:
#         print("name ",args[0]," age ",args[1])
# # function("Arry",15)
# lis = ["ARRY",20]
# function(*lis)

# kwargs
# def printmarks(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key,value)
# marklist={"ARRY":100,"FAIRY":100,"MOHAN PYAARE":90,"GUDREGU":97,"DEENA NATH":99}

# printmarks(**marklist)

# def master(normal,*args,**kwargs):
#     print(normal)
#     for i in args:
#         print(i)
#     for key, value in kwargs.items():
#         print(key,value)
# lis = ["Arry",20,9604]
# marklist={"ARRY":100,"FAIRY":100,"MOHAN PYAARE":90,"GUDREGU":97,"DEENA NATH":99}

# master("normal arg",*lis,**marklist)

try:
    print("II will try code and throw exception only if there is prblm")
except Exception as e:
    print("I will riun only if try block fails")
else:
    print("I will run only if there is no exception. use this to run code what shloud only execute if there is no exception")
finally:
    print("this will be printed in every case")