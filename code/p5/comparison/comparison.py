import math
from scipy import integrate
import numpy as np


def f(x):
    return math.sqrt(1 + math.exp(x))


def simpson(function, a, b):
    return ((b - a) / 6) * (function(a) + 4 * function((a + b) / 2) + function(b))


# 复合梯形求积
def trapezium_integral(f, a, b, n):
    h = (b - a) / n
    x = np.arange(a, b + h, h)
    integral_sum = 0
    for i in range(n):
        integral_sum += (h / 2) * (f(x[i]) + f(x[i + 1]))
    return integral_sum


def func1(x):
    return 2 * (1 + np.exp(2 * x + 2)) ** (1 / 2)


def Guass_Integral(n):
    weight = np.array([0.417959184,
                       0.381830051,
                       0.381830051,
                       0.279705391,
                       0.279705391,
                       0.129484966,
                       0.129484966, ])
    xxxx = np.array([
        0,
        - 0.405845151,
        0.405845151,
        - 0.741531186,
        0.741531186,
        - 0.949107912,
        0.949107912,
    ])
    fxxxx = func1(xxxx)

    if n == 3:
        return 0.88888888 * func1(0) + 0.55555555 * func1(-0.775666924) + 0.55555555 * func1(0.774596669)
    elif n == 5:
        return 0.56888888 * func1(0) + 0.47862867 * func1(-0.538469310) + 0.47862867 * func1(
            0.538469130) + 0.23692688 * func1(-0.90617984) + 0.23692688 * func1(0.90617984)
    elif n == 7:
        return np.matmul(weight, np.transpose(fxxxx))


if __name__ == "__main__":
    compound_simpson = 0
    # 区间等分数
    n = 2
    x = np.linspace(0, 4, n + 1)
    for i in range(n):
        compound_simpson += simpson(f, x[i], x[i + 1])
    print('7点的高斯积分为' + str(Guass_Integral(7)))
    print('5点的高斯积分为' + str(Guass_Integral(5)))
    print('3点的高斯积分为' + str(Guass_Integral(3)))
    print("复合梯形积分为" + str(trapezium_integral(f, 0, 4, n)))
    print("复合simpson积分为" + str(compound_simpson))
    print("标准数值积分为" + str(integrate.quad(f, 0, 4)[0]))
