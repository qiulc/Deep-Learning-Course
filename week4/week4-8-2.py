import tensorflow as tf
import numpy as np


x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

n = len(x)

Numerator = tf.constant(0.)
Denominator = tf.constant(0.)

N_tem1 = tf.constant(0.)
N_tem2 = tf.constant(0.)
D_tem1 = tf.constant(0.)
D_tem2 = tf.constant(0.)

y_sum = tf.reduce_sum(y)
x_sum = tf.reduce_sum(x)

D_tem2 = tf.pow(x_sum, 2)

for i in range(n):
    N_tem1 += x[i] * y[i]
    N_tem2 += x[i] * y_sum
    D_tem1 += tf.pow(x[i], 2)
    
N_tem1 = N_tem1 * n
D_tem1 = D_tem1 * n

Numerator = N_tem1 - N_tem2
Denominator = D_tem1 - D_tem2
w = Numerator / Denominator

b = (y_sum - w * tf.reduce_sum(x)) / n

print("w: {}".format(w))
print("b: {}".format(b))
