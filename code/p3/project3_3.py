import numpy as np
import matplotlib.pyplot as plt


# 输入control points画出bezier曲线(随便画一个形状)

# B = (1-t)*P0+t*P1
def one_bezier_curve(a, b, t):
    return (1 - t) * a + t * b


# 使用de Casteljau算法求解曲线
# Bn(P0,...,Pn)=(1-t)*Pn-1(P0,...,Pn-1)+t*(P1,...,Pn)
def n_bezier_curve(controlPointCoordinate, n, k, t):
    """
    :param controlPointCoordinate: 控制点的x坐标或y坐标
    :param n: n阶bezier曲线
    :param k: 设置控制点下标
    :param t:计算参数为t处的x,y坐标
    :return:参数为t处的x,y坐标
    """
    # 当且仅当为一阶时，递归结束
    if n == 1:
        return one_bezier_curve(controlPointCoordinate[k], controlPointCoordinate[k + 1], t)
    else:
        return (1 - t) * n_bezier_curve(controlPointCoordinate, n - 1, k, t) + t * n_bezier_curve(
            controlPointCoordinate, n - 1, k + 1, t)


def bezier_curve(x, y):
    """
    :param x: bezier曲线控制点x坐标数组
    :param y: bezier曲线控制点y坐标数组
    """
    # pyplot作图点
    b_x = []
    b_y = []
    n = len(x) - 1  # n阶bezier曲线
    t_step = 1.0 / 1000
    t = np.arange(0.0, 1 + t_step, t_step)
    for each in t:
        b_x.append(n_bezier_curve(x, n, 0, each))
        b_y.append(n_bezier_curve(y, n, 0, each))
    return b_x, b_y


def get_subdivision_points(t, controlPointCoordinate: set):
    num_triangle = []
    n = len(controlPointCoordinate)
    for row in range
    for row in range(1, n):
        for column in range(0, n - row):
            num_triangle[row][column] = (1-t)*


if __name__ == "__main__":
    # x = [int(n) for n in input('x:').split()]
    # y = [int(n) for n in input('y:').split()]
    x = np.linspace(0, 0.2, 7)
    y = [-10, 10, 10, -20, 10, 10, -10]
    # plt.plot(x, y)

    bezier_x, bezier_y = bezier_curve(x, y)
    plt.plot(bezier_x, bezier_y)

    plt.show()
