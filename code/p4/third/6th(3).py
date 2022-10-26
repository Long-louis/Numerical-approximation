import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from scipy import integrate


def law_martix(n):
    X = [5, 10, 15, 20, 25, 30, 35, 40]
    M = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):

            for k in range(8):
                M[i][j] = M[i][j] + X[k] ** i * X[k] ** j
    return M


def zero_law_martix(n):
    X = [5, 10, 15, 20, 25, 30, 35, 40]
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):

            for k in range(8):
                M[i][j] = M[i][j] + X[k] ** (i + 1) * X[k] ** (j + 1)
    return M


def D_martix(n):
    X = [5, 10, 15, 20, 25, 30, 35, 40]
    Y = [3.42, 5.96, 31.14, 41.76, 74.54, 94.32, 133.78, 169.16]
    D = np.zeros((n + 1, 1))
    for i in range(n + 1):
        for j in range(8):
            D[i][0] = D[i][0] + X[j] ** i * Y[j]
    return D


def zero_D_martix(n):
    X = [5, 10, 15, 20, 25, 30, 35, 40]
    Y = [3.42, 5.96, 31.14, 41.76, 74.54, 94.32, 133.78, 169.16]
    D = np.zeros((n, 1))
    for i in range(n):
        for j in range(8):
            D[i][0] = D[i][0] + X[j] ** (i + 1) * Y[j]
    return D


def coefficient(n):
    M = law_martix(n)
    D = D_martix(n)
    A = np.linalg.solve(M, D)
    return A


def zero_coefficient(n):
    M = zero_law_martix(n)
    D = zero_D_martix(n)
    A = np.linalg.solve(M, D)
    return A


X = [5, 10, 15, 20, 25, 30, 35, 40]
Y = [3.42, 5.96, 31.14, 41.76, 74.54, 94.32, 133.78, 169.16]
A = coefficient(1)
Y1 = []
Y2 = []
Y3 = []
for i in range(8):
    c = A[0][0] + A[1][0] * X[i]
    Y1.append(c)
A = coefficient(2)
for i in range(8):
    c = A[0][0] + A[1][0] * X[i] + A[2][0] * X[i] ** 2
    Y2.append(c)
A = zero_coefficient(2)
for i in range(8):
    c = A[0][0] * X[i] + A[1][0] * X[i] ** 2
    Y3.append(c)
plt.scatter(X, Y, alpha=0.5, label='initial point')
plt.plot(X, Y1, 'r-', label='P1')
plt.plot(X, Y2, 'c-', label='P2')
plt.plot(X, Y3, 'g-', label='P3')
# plt.legend()
plt.show()
