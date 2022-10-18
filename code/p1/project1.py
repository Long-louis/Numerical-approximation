# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import matplotlib.pyplot as plt

# x = 10 ** (-16)
#
# y = ((1 + x) - 1) / x
#
# print(y)


# 1(2)
for n in range(101, 0, -1):
    if (0.5 + 2 ** (-n)) > 0.5:
        print(n)
        break


# 2(1)


def s_n(x, n):
    y = 0
    for i in range(0, n + 1):
        y += x ** i / math.factorial(i)
    return y


# print(s_n(-10, 20))
# print(math.exp(-10))

def E_r(x, n):
    return abs((s_n(x, n) - math.exp(x)) / math.exp(x))


# print(E_r(-10, 20))

N = [i for i in range(1, 21)]

X1 = [E_r(-10, n) for n in N]
X2 = [E_r(10, n) for n in N]

plt.plot(N, X1)

plt.show()

# 3(2)
i = 0
for n in range(0, 21):
    i += 1 / (math.factorial(n) * (21 + n))

print(i)
