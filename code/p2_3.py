from scipy.interpolate import interp1d, PchipInterpolator
import matplotlib.pyplot as plt
import numpy as np

n = 20  # 对n值进行修改即可
X = [0, 1, 4, 3]
Y = [0, 2, 4, 1]
f_cubic = interp1d(X, Y, kind='cubic')
f_linear = interp1d(X, Y, kind='linear')
x_new = np.linspace(0, 4, 100)


plt.plot(X, Y, "o", label="data")
plt.plot(x_new, f_cubic(x_new), label="pchip")
plt.show()