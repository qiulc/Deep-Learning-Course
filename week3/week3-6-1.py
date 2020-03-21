'''
2020/03/12
第三周任务1：mooc第六讲单元作业1
'''
import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x = [137.97, 104.50, 100, 124.32, 79.2, 99, 124, 114,
    106.69, 138.05, 53.75, 46.91, 68, 63.02, 81.26, 86.21]

y = [145, 110, 93, 116, 65.32, 104, 118, 91,
    62, 133, 51, 45, 78.5, 69.65, 75.69, 95.30]

plt.scatter(x, y, c="red" )
plt.title("商品房销售记录", fontsize="16", c="b")
plt.xlabel("面积(平方米)", fontsize="14")
plt.ylabel("价格(万元)", fontsize="14")
plt.show()


