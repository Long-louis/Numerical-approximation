from scipy.interpolate import interp1d, PchipInterpolator

import matplotlib.pyplot as plt
import numpy as np
import math

# （1）
'''
x, y = [], []

ns = [4, 10, 14, 20]
for i in range(len(ns)):
    n = ns[i]
    x.append([(-5 + j * 10.0 / n) for j in range(0, n + 1)])
    y.append([1 / (1 + j ** 2) for j in x[i]])
    plt.subplot(2, 2, i + 1)
    plt.plot(x[i], y[i], x[i], y[i], 'r+')

plt.show()
'''

# (2)

'''
n = 20  # 对n值进行修改即可
X = [(-5 + i * 10.0 / n) for i in range(0, n + 1)]
Y = [1 / (1 + i ** 2) for i in X]
f_pchip = PchipInterpolator(X, Y)

x_new = np.linspace(-5, 5, 100)
y_2 = [1 / (1 + i ** 2) for i in x_new]


plt.plot(X, Y, "o", label="data")

plt.plot(x_new, y_2, label="f")

plt.plot(x_new, f_pchip(x_new), label="pchip")
plt.show()
'''

# (3)
n = 20  # 对n值进行修改即可
X = [(-5 + i * 10.0 / n) for i in range(0, n + 1)]
Y = [1 / (1 + i ** 2) for i in X]
f_cubic = interp1d(X, Y, kind='cubic')

x_new = np.linspace(-5, 5, 100)
y_2 = [1 / (1 + i ** 2) for i in x_new]

plt.plot(X, Y, "o", label="data")
plt.plot(x_new, y_2, label="f")
plt.plot(x_new, f_cubic(x_new), label="pchip")
plt.show()