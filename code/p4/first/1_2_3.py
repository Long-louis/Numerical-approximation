from one import *
from scipy.optimize import curve_fit


def func(x, a, b, c, d):
    return a + b * x + c * pow(x, 2) + d * pow(x, 3)


if __name__ == '__main__':
    k = np.arange(0, 10, 1)
    deltadelta = []
    for ki in k:
        a = get_amatrix(ki)
        b = get_bmatrix(multi_g, ki)
        cofficient = linalg.solve(a, b)

        x = np.linspace(-1, 1, 100)
        delta = delta_f(x, cofficient, ki)
        deltadelta.append(max(delta))

    # 非线性最小二乘法拟合
    popt, pcov = curve_fit(func, k, deltadelta)
    # 获取popt里面是拟合系数
    a = popt[0]
    b = popt[1]
    c = popt[2]
    d = popt[3]
    yvals = func(k, a, b, c, d)  # 拟合y值

    plot = plt.plot(k, yvals, 'r', label='拟合曲线')
    plt.show()
