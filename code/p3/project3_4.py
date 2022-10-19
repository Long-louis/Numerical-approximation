import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 0.2, 7)
y = [-10, 10, 10, -20, 10, 10, -10]
n = len(x) - 1
# 升一阶
px, py = [x[0]], [y[0]]
for i in range(1, n):
    a = ((n + 1 - i) * x[i] / (n + 1)) + (i * x[i - 1] / (n + 1))
    px.append(a)
    b = ((n + 1 - i) * y[i] / (n + 1)) + (i * y[i - 1] / (n + 1))
    py.append(b)
px.append(x[n])
py.append(y[n])
# 升两阶
for i in range(1, n):
    px[i] = ((n + 1 - i) * px[i] / (n + 1)) + (i * px[i - 1] / (n + 1))
    py[i] = ((n + 1 - i) * py[i] / (n + 1)) + (i * py[i - 1] / (n + 1))

plt.scatter(px, py)
plt.show()
