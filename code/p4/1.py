import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import linalg


def multi_xk(x, k1, k2):
    return math.pow(x, k1) * math.pow(x, k2)


def multi_f(x, k):
    return math.exp(x) * math.pow(x, k)


def muti_g(x, k):
    return abs(x) * math.pow(x, k)


def get_amatrix(k):
    amatrix = np.zeros((k + 1, k + 1))
    for row in range(0, k + 1):
        for column in range(0, k + 1):
            amatrix[row][column], wucha = integrate.quad(multi_xk, -1, 1, args=(row, column))
    return amatrix


def get_bmatrix(function, k):
    bmatrix = np.zeros(k + 1)
    for column in range(0, k + 1):
        bmatrix[column], wucha = integrate.quad(function, -1, 1, args=column)
    return bmatrix


k=3
a = get_amatrix(k)
b = get_bmatrix(multi_f, k)

x = linalg.solve(a, b)

print(x)
