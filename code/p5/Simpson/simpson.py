import math
from scipy import integrate
import numpy as np


def gauss(x):
    return (200 / (0.1 * math.pi)) * math.exp(-math.pow(x - 1.7, 2) / (2 * 0.01))


def simpson(function, a, b):
    return ((b - a) / 6) * (function(a) + 4 * function((a + b) / 2) + function(b))


if __name__ == "__main__":
    n = 10
    h = 0.01
    x = np.arange(1.8, 1.905, 0.01)
    compound_simpson = 0
    '''
        for i in range(n):
        compound_simpson += 4 * gauss((x[i] + x[i + 1]) / 2)
    for i in range(n):
        compound_simpson += 2 * gauss(x[i])
    compound_simpson += gauss(1.8)
    compound_simpson += gauss(1.9)
    compound_simpson *= 0.01/6
    '''
    for i in range(n):
        compound_simpson += simpson(gauss, x[i], x[i + 1])

    print("复合simpson方法求得的积分为" + str(compound_simpson),
          "误差为" + str(compound_simpson - integrate.quad(gauss, 1.8, 1.9)[0]))
    print("simpson方法求得的积分为" + str(simpson(gauss, 1.8, 1.9)),
          "误差为" + str(simpson(gauss, 1.8, 1.9) - integrate.quad(gauss, 1.8, 1.9)[0]))
    print("标准数值积分为" + str(integrate.quad(gauss, 1.8, 1.9)[0]))
