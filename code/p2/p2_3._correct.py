
'''
import numpy as np               #第三题第一问
import matplotlib.pyplot as plt
def lar(x1,y1,x2,y2):
    y = []
    x = np.linspace(x1, x2, 200)
    for i in range(0,200):
        a = (x[i]-x2)*y1/(x1-x2)+(x[i]-x1)*y2/(x2-x1)
        y.append(a)
    plt.plot(x,y,'c')
lar(0,0,1,2)
lar(1,2,4,4)
lar(4,4,3,1)
lar(3,1,0,0)
plt.show()
'''

import numpy as np
from matplotlib.pyplot import *
from scipy import linalg
t1 = [0,1,2,3,4]
x1 = [0,1,4,3,0]
y1 = [0,2,4,1,0]
ax = subplot(1,1,1)
ax.plot(x1,y1,'c')
def d2(x,y):
    n = len(x);d_1 = []
    martix = np.ones((n,n))#差商矩阵
    for i in range(n):
        martix[i][0] = y[i]
    for i in range(1,n):
        for k in range(i,n):
            martix[k][i] = (martix[k][i-1]-martix[k-1][i-1])/(x[k]-x[k-i])
    for i in range(n-2):
        d_1.append(martix[i+2][2])
    return d_1

def equation(x,y):
    n = len(x)
    mu = [];lamda = [];d = []
    for i in range(n-2):
        mu.append((x[i+1]-x[i])/(x[i+2]-x[i]))
    mu.append((x[n-1]-x[n-2])/(x[1]-x[0]+x[n-1]-x[n-2]))
    for i in range(n-2):
        lamda.append((x[i+2]-x[i+1])/(x[i+2]-x[i]))
    lamda.append((x[1]-x[0])/(x[1]-x[0]+x[n-1]-x[n-2]))
    d_1 = d2(x,y)
    for i in range(n-2):
        d.append(6*d_1[i])
    d.append(6*((((y[1]-y[0])/(x[1]-x[0]))-((y[n-1]-y[n-2])/(x[n-1]-x[n-2])))/(x[1]-x[0]+x[n-1]-x[n-2])))
    A=np.zeros((n-1,n-1))
    A[0][0] = 2;A[0][1] = lamda[0];A[0][n-2] = mu[0]
    for i in range(1,n-2):
        A[i][i-1] = mu[i];A[i][i] = 2;A[i][i+1] = lamda[i]
    A[n-2][0] = lamda[n-2];A[n-2][n-2] = 2;A[n-2][n-3] = mu[n-2]#构造行列式
    M1 = linalg.solve(A, d)#解方程
    M = []
    M.append(M1[0])
    for i in range(len(M1)):
        M.append(M1[i])
    return M

def S_i(x,y,M,xx,i):#在I_i区间上的插值函数
    if (xx < x[i+1]) and (xx > x[i]):
        return (((M[i]*(x[i+1]-xx)**3)/(6*(x[i+1]-x[i])))+((M[i+1]*(xx-x[i])**3)/(6*(x[i+1]-x[i])))+
            (y[i]-(M[i]/6)*(x[i+1]-x[i])**2)*((x[i+1]-xx)/(x[i+1]-x[i])) + (y[i+1]-(M[i+1]/6)*(x[i+1]-x[i])**2)*((xx-x[i])/(x[i+1]-x[i])))
    elif xx == x[i]:
        return y[i]
    else:
        return 0

def S(x,y,M,xx):
    n = len(x)
    sum = 0
    for i in range(n-1):
        sum += S_i(x,y,M,xx,i)
    if xx == x[n-1]:
        sum += y[n-1]
    else:
        sum += 0
    return sum

def draw_y(x,y):
    xx = np.linspace(0, 4, 200)
    y1 = []
    M = equation(x,y)
    for i in range(200):
        y1.append(S(x,y,M,xx[i]))
    return y1
ax.plot(draw_y(t1,x1),draw_y(t1,y1),'r')
legend()
show()
