import numpy as np
import math

def getResult(x, y):
    ax = np.sum(x)/len(x)
    ay = np.sum(y)/len(y)
    numerator = 0        #分子
    denominator = 0      #分母
    for i in range(len(x)):
        numerator += (x[i] - ax)*(y[i] - ay)
        denominator += math.pow((x[i]-ax), 2)
    w = numerator/denominator
    b = ay - w * ax
    return w, b
        

x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]

W, b = getResult(x, y)

print("W: {}\nb: {}".format(W,b))

