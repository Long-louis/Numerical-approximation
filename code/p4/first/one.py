import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import linalg


def multi_xk(x, k1, k2):
    return math.pow(x, k1) * math.pow(x, k2)


def multi_f(x, k):
    return math.exp(x) * math.pow(x, k)


def multi_g(x, k):
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

#将函数中math.exp(i)换为abs(i)
def delta_f(x, cofficient, k):
    delta = []

    for i in x:
        pk = np.array([])
        for j in range(0, k + 1):
           pk = np.append(pk, [math.pow(i, j)])
        pkplus = np.matmul(cofficient, np.transpose(pk))
        delta.append(abs(abs(i) - pkplus))
    return delta


if __name__ == '__main__':
    k = 10
    a = get_amatrix(k)
    b = get_bmatrix(multi_g, k)
    cofficient = linalg.solve(a, b)

    x = np.linspace(-1, 1, 100)
    delta = delta_f(x, cofficient, k)
    plt.plot(x, delta)
    plt.show()