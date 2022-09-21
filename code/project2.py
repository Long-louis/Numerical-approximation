# -- coding:utf-8 -- #

"""
Project:numerical-approximation
File:project2.py
Author:halongbay
Date:2022/9/21 15:49

"""
import matplotlib.pyplot as plt
import numpy as np


def lagrange(X, Y, XX) -> list:
    ln = 0
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


n = 14  # 对n值进行修改即可
X = [(-5 + i * 10.0 / n) for i in range(0, n + 1)]
Y = [1 / (1 + i ** 2) for i in X]
XX = np.linspace(-5, 5, 1000)

plt.figure()
plt.plot(XX, lagrange(X, Y, XX), zorder=1)
plt.plot(XX, 1 / (1 + XX ** 2), zorder=1)
plt.scatter(X, Y, marker='.', color='r', zorder=2)
plt.show()
