from time import time

def func1(a,b):
    # 1
    return a+b

def func2(a,b):
    # 2
    num1 = a
    num2 = b
    if(a>b and a!=3):
        pass
    sum([4,3])
    return a+b

if __name__ == '__main__':
    init = time()
    for i in range(0,100000):
        func1(3,5)
    print("1: ", time()-init)
    init = time()
    for i in range(0,100000):
        func2(3,5)
    print("2: ", time() - init)