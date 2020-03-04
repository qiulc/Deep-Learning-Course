import math

def result(a, b, c):
    temp = b*b-4*a*c
    t=set()
    if temp >= 0:
        x1 = (-1 * b + pow(temp, 0.5)) / (2*a)
        x2 = (-1 * b - pow(temp, 0.5)) / (2*a)
        t.add(x1)
        t.add(x2)
    return t

def dataInput():
    while(True):
        try :
            a = int (input("Please input a : "))
            b = int (input("Please input b : "))
            c = int (input("Please input c : "))
            break
        except: 
            print("Input ERROR !!! Please input again !")
            continue
      
    return a, b, c

def outSet(t):      #t是一个集合
    for i in t:
        print(i)

print("*************************求 ax + bx + c 的解************************")
while(True):
    a, b, c = dataInput();
    if a == 0:
        print("不是二次函数")
    else :
        results = result(a, b, c)
        length = len(results)
        print("该二次函数有{}个解：".format(length))
        if length != 0:
            outSet(results)
    print("*******************************************************************")
        
        

    




