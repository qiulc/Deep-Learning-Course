'''
2020/03/12

第三周任务2：下载波士顿数据集，按照用户输入属性，输出的对应波士顿数据集中属性的散点图

'''

import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def Datainput():
    while(True):
        try :
            number = int (input("请选择属性:\n"))
            if 0<number & number<=13:
                break
            else:
                print("输入1-13之间的整数！！")
                continue
        except: 
            print("输入的数字有误！！")
            continue
    return number


def displayTitle(title):
    for i in range(len(title)):
        print("{}---{}".format(i+1,title[i]))

boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (test_x, test_y) = boston_housing.load_data(test_split=0)

title = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]

displayTitle(title)

number = Datainput()

plt.figure()
plt.scatter(train_x[:, number-1], train_y)
plt.xlabel(title[number-1])
plt.ylabel("Price($1000/s)")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.title(title[number-1] + " -- 散点图", x=0.5, y=1.02, fontsize=16)
plt.show()