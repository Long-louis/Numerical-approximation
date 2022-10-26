import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *



def martix():
    X = np.linspace(0, 1, 7)
    M = np.zeros((2,2))
    for k in range(7):
        M[0][0] = M[0][0] + math.exp(X[k]) * math.exp(X[k])
        M[1][0] = M[1][0] + math.exp(X[k]) * math.exp(-X[k])
        M[0][1] = M[0][1] + math.exp(-X[k]) * math.exp(X[k])
        M[1][1] = M[1][1] + math.exp(-X[k]) * math.exp(-X[k])
    return M


def D_martix():
    X = np.linspace(0, 1, 7)
    Y = [1]*7
    a = 0.1 * np.random.rand(7, 1)
    for i in range(7):
        Y[i] = math.exp(X[i]) + math.exp(-X[i]) + a[i]
    D = np.zeros((2, 1))
    for j in range(7):
        D[0][0] = D[0][0] + math.exp(X[j]) * Y[j]
        D[1][0] = D[1][0] + math.exp(-X[j]) * Y[j]
    return D


def coefficient():
    M = martix()
    D = D_martix()
    A = np.linalg.solve(M,D)
    return A


X = np.linspace(0, 1, 7)
Y = [1]*7
a = 0.1 * np.random.rand(7, 1)
for i in range(7):
    Y[i] = math.exp(X[i]) + math.exp(-X[i]) + a[i][0]
A = coefficient()
YY = []
for i in range(7):
    c = A[0][0]*math.exp(X[i])+A[1][0]*math.exp(-X[i])
    YY.append(c)
plt.scatter(X,Y)
plt.plot(X,YY,'c-')
plt.show()
