# -- coding:utf-8 -- #

# noinspection SpellCheckingInspection
"""
Project:numerical-approximation
File:project2_1.py
Author:halongbay
Date:2022/9/21 15:49

"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi


# X是已知节点
# Y是对应函数值
# XX是差值点
# YY是language插值法算出的函数值
'''
def lagrange(X, Y, XX) -> list:
    lin = 0
    YY = [0.0] * len(XX)
    for i in range(len(X)):
        lin = [1] * len(XX)
        for j in range(len(X)):
            if j != i:
                for k in range(len(XX)):
                    lin[k] *= (XX[k] - X[j]) / (X[i] - X[j])
        for k in range(len(XX)):
            YY[k] += lin[k] * Y[i]
    return YY


'''
n = 14  # 对n值进行修改即可
X = [(-5 + i * 10.0 / n) for i in range(0, n + 1)]
Y = [1 / (1 + i ** 2) for i in X]
XX = np.linspace(-5, 5, 1000)
'''


# 切比雪夫节点定义函数
def chebyshev_nodes(a, b, n):
    i = np.array(range(n + 1))
    z = np.cos((2 * i + 1) * pi / (2 * (n + 1)))
    return 0.5 * (b - a) * z + 0.5 * (b + a)


X = chebyshev_nodes(-5, 5, 10)  # 修改第三个参数改变差值点数量
Y = [1 / (1 + i ** 2) for i in X]
# 定义插值点
XX = np.linspace(-5, 5, 1000)
# 画图
plt.figure()
plt.plot(XX, lagrange(X, Y, XX), zorder=1)
plt.plot(XX, 1 / (1 + XX ** 2), zorder=1)
plt.scatter(X, Y, marker='.', color='r', zorder=2)
plt.show()
'''


#第四问
def Newton(x, y, xx):
    n = len(x)
    martix = np.ones((n, n))  # 差商矩阵
    for i in range(n):
        martix[i][0] = y[i]
    for i in range(1, n):
        for k in range(i, n):
            martix[k][i] = (martix[k][i - 1] - martix[k - 1][i - 1]) / (x[k] - x[k - i])
    yy = martix[0][0]
    newton = [1] * n
    for i in range(1, n):
        for k in range(i):
            newton[i] *= (xx - x[k])
    for i in range(1, n):
        yy += martix[i][i] * newton[i]

    return yy


def draw_x(n):
    return np.linspace(-5, 5, n)


def draw_y(n):
    x2 = np.linspace(-5, 5, n)
    x1 = np.linspace(-5, 5, 200)
    y1 = 1 / (1 + (pow(x1, 2)))  # 原函数
    y2 = []
    y = []
    for i in range(n):
        y.append(1 / (1 + (pow(x2[i], 2))))
    for i in range(200):
        y2.append(Newton(x2, y, x1[i]))
    return y2


x = np.linspace(-5, 5, 200)
y1 = 1 / (1 + (pow(x, 2)))
ax1 = plt.subplot(2, 2, 1)
ax1.plot(x, y1, 'y')
ax1.plot(x, draw_y(5), 'r')

ax2 = plt.subplot(2, 2, 2)
ax2.plot(x, y1, 'y')
ax2.plot(x, draw_y(11), 'r')

ax3 = plt.subplot(2, 2, 3)
ax3.plot(x, y1, 'y')
ax3.plot(x, draw_y(15), 'r')

ax4 = plt.subplot(2, 2, 4)
ax4.plot(x, y1, 'y')
ax4.plot(x, draw_y(21), 'r')
plt.show()