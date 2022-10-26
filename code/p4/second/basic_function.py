# encoding:utf-8

import numpy as np
from sympy import *
from scipy.integrate import quad
from matplotlib.pyplot import *
from scipy import linalg
# from sympy import *


# n表示正交多项式个数

def f1(x):
    return exp(x)


def f2(x):
    return np.abs(x)


def f3(x):
    return (1 / (1 + 25 * (x ** 2)))


def dot_product1(k, l):  # 连续函数内积
    x = symbols('x')
    return (integrate(x ** (k + l), (x, -1, 1)))


def dot_product2(k, l, x, y):  # 离散内积
    result = 0
    for i in range(len(x)):
        result += (x[i]) ** k * (y[i]) ** l
    return result


def dot_product3(k, l):  # 练习二连续函数内积
    x = symbols('x')
    return (integrate(x ** (k + l), (x, 0, 1)))


def cal_law_martix(n, num):  # 建立法矩阵
    G = np.zeros((n, n))
    if num != 3:
        for i in range(n):
            for j in range(n):
                G[i][j] = dot_product1(i, j)
    else:
        for i in range(n):
            for j in range(n):
                G[i][j] = dot_product3(i, j)
    return G


def cal_vector(n, num):
    b = []
    if num == 1:
        for i in range(n):
            x = symbols('x')
            b.append(float(integrate(f1(x) * (x ** i), (x, -1, 1))))
    elif num == 2:
        for i in range(n):
            x = symbols('x')
            b.append(float(integrate(f2(x) * (x ** i), (x, -1, 1))))
    elif num == 3:
        for i in range(n):
            x = symbols('x')
            b.append(float(integrate(f3(x) * (x ** i), (x, 0, 1))))
    return b


def solve_equation1(n, num):
    G = cal_law_martix(n, num)
    b = cal_vector(n, num)
    A = linalg.solve(G, b)
    return A


def cal_least_square_method_martix(times, x):  # times次最小二乘法矩阵
    G = np.zeros((times + 1, times + 1))
    for i in range(times + 1):
        for j in range(times + 1):
            G[i][j] = dot_product2(i, j, x, x)
    return G


def cal_least_square_method_vector(times, x, y):
    b = []
    for i in range(times + 1):
        b.append(dot_product2(i, 1, x, y))
    return b


def solve_equation2(times, x, y):
    G = cal_least_square_method_martix(times, x)
    b = cal_least_square_method_vector(times, x, y)
    A = linalg.solve(G, b)
    return A


def Legendre(n, x):  # 返回k次Legendre多项式
    if n == 0:
        Ln = 1
    elif n == 1:
        Ln = 2 * x - 1
    else:
        Ln = (1 / n) * ((2 * n - 1) * (2 * x - 1) * Legendre(n - 1, x) - (n - 1) * Legendre(n - 2, x))
    return Ln


def Chebyshev(n, x):  # 返回k次Chebyshev多项式
    if n == 0:
        Cn = 1
    elif n == 1:
        Cn = 2 * x - 1
    else:
        Cn = (2 * (2 * x - 1) * Chebyshev(n - 1, x) - Chebyshev(n - 2, x))
    return Cn


def cal_vector_Legendre(n):
    b = []
    for i in range(n + 1):
        f = lambda x: f3(x) * (Legendre(i, x))
        b.append(float(quad(f, 0, 1)[0]))
    return b


def cal_vector_Chebyshev(n):
    b = []
    for i in range(n + 1):
        f = lambda x: (f3(x) * (Chebyshev(i, x))) * (1 / (1 - (2 * x - 1) ** 2) ** 0.5)
        b.append(float(quad(f, 0, 1)[0]))
    return b


def solve_equation_Legendre(n):
    A = []
    for i in range(n + 1):
        A.append(((2 * i + 1) * cal_vector_Legendre(n)[i]))
    return A


def solve_equation_Chebyshev(n):
    A = []
    A.append((cal_vector_Chebyshev(n)[0]) * (2 / np.pi))
    for i in range(1, n + 1):
        A.append((cal_vector_Chebyshev(n)[i]) / (np.pi / 4))
    return A
