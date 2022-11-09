import math

import numpy as np
from scipy import integrate


def trapezium_integral(f, a, b, n):
    h = (b - a) / n
    x = np.arange(a, b + h, h)
    integral_sum = 0
    for i in range(n):
        integral_sum += (h / 2) * (f(x[i]) + f(x[i + 1]))
    return integral_sum


def romberg(f, a, b, tolenrance):
    t = []
    k = 1
    # t.append(((b - a) / 2) * (f(a) + f(b)))
    t.append(trapezium_integral(f, a, b, 1))
    t.append(
        [trapezium_integral(f, a, b, 2), (4 * trapezium_integral(f, a, b, 2) - trapezium_integral(f, a, b, 1)) / 3])
    while abs(t[k][k] - t[k][k - 1]) > tolenrance:
        k += 1
        tk = [trapezium_integral(f, a, b, 2 ** k)]
        for j in range(1, k + 1):
            tk.append((1 / (4 ** j - 1)) * (4 ** j * tk[j - 1] - t[k - 1][j - 1]))
        t.append(tk)

    return t[k][k]


def f(x):
    return math.log(x)


if __name__ == "__main__":
    print(trapezium_integral(math.cos, 0, 1, 1))
    epsilon = 10 ** (-6)
    solution = romberg(f, 1, 2, epsilon)
    solution2 = integrate.quad(f, 1, 2)
    print(solution, solution - solution2[0])

