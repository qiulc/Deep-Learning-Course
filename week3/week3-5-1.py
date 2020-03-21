import numpy as np

def Datainput():
    while(True):
        try :
            number = int (input("请输入一个1-100之间的整数：\n"))
            if 0<number & number<=100:
                break
            else:
                print("输入1-100之间的整数！！")
                continue
        except: 
            print("输入的数字有误！！")
            continue
    return number

np.random.seed(612)
array = np.random.rand(1000)
num = Datainput()
key = 1
print("序号\t索引值\t随机数")
for i in range(len(array)):
    tem = key*num
    if tem >= len(array):
        break
    print(key, end="\t")
    print(tem, end="\t")
    print(array[tem])
    key = key + 1

