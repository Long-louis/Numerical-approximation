# -- coding:utf-8 -- #

"""
Project:numerical-approximation
File:project2.py
Author:halongbay
Date:2022/9/21 15:49

"""


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
n = 4
X = [(-5 +  ]