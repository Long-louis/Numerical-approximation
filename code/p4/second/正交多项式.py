from basic_function import *
import numpy as np
from matplotlib.pyplot import *

'''避免中文乱码'''
rcParams['font.sans-serif'] = [u'SimHei']
rcParams['axes.unicode_minus'] = False


def value1(n):  # 返回第一问最佳平方逼近多项式的值
    A = solve_equation1(n, 3)
    x = np.linspace(0, 1, 100)
    y1 = 0
    for i in range(n):
        y1 += A[i] * (x ** (i))
    return y1


def draw1():
    k = [5, 10]
    for i in range(2):
        ax = subplot(1, 2, i + 1)
        x = np.linspace(0, 1, 100);
        y = f3(x)
        ax.plot(x, y, 'y', label='原函数')
        y1 = value1(k[i] + 1)
        ax.plot(x, y1, 'b', label='正交多项式')
        title('k = ' + str(k[i]))
        legend()
    show()


def value_Legendre(n):  # 返回第二问最佳平方逼近多项式的值
    A = solve_equation_Legendre(n)
    x = np.linspace(0, 1, 50)
    y1 = []
    for j in range(50):
        y2 = 0
        for i in range(n + 1):
            y2 += A[i] * (Legendre(i, x[j]))
        y1.append(y2)
    return y1


def draw_Legendre():
    k = 10
    ax = subplot(1, 1, 1)
    x = np.linspace(0, 1, 50);
    y = f3(x)
    ax.plot(x, y, '#F2FF2D', label='原函数')
    y1 = value_Legendre(k)
    ax.plot(x, y1, '#2E31FF', label='正交多项式')
    title('k = 10')
    legend()
    show()


def value_Chebyshev(n):  # 返回第二问最佳平方逼近多项式的值
    A = solve_equation_Chebyshev(n)
    x = np.linspace(0, 1, 50)
    y1 = []
    for j in range(50):
        y2 = 0
        for i in range(n + 1):
            y2 += A[i] * (Chebyshev(i, x[j]))
        y1.append(y2)
    return y1


def draw_Chebyshev():
    k = 5
    ax = subplot(1, 1, 1)
    x = np.linspace(0, 1, 50);
    y = f3(x)
    ax.plot(x, y, '#F2FF2D', label='原函数')
    y1 = value_Chebyshev(k)
    ax.plot(x, y1, '#2E31FF', label='正交多项式')
    title('k = 5')
    legend()
    show()


draw_Chebyshev()