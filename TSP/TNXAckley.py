import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


'''
测试 函数
使用天牛须算法测试后，效果不理想
维数越少越趋近最小值
测试Ackley函数，发现不收敛
'''


eta = 0.99      # 步长衰减
c = 5           # 步长度
step = 32       # 步长
k = 10          # 维数
n = 2000    # 迭代次数
bb = []         # 每一次迭代后的值
best = []       # 每一次迭代后的总体最佳值
p = 0.05


def f(x):       # 测试函数Ackley
    s1 = 0
    s2 = 0
    for i in x:
        s1 += i ** 2
        s2 += np.cos(2*np.pi*i)
    ss = -20*np.exp(-0.2*np.sqrt(1/k*s1)) - np.exp(1/k*s2) + 20 + np.e
    return ss

def run():
    global step
    x = []
    for i in range(k):
        x.append(-32 + 32*random.random())
    xbest = []
    for i in x:
        xbest.append(i)
    fbest = f(xbest)
    print("0 : xbest = ", xbest, "fbest = ", fbest)
    best.append(fbest)
    bb.append(fbest)

    for i in range(n):
        '''rand = random.random()
        if i>500 and rand<p:
            step = 5'''
        d = step / c
        dre = []
        for j in range(k):
            dre.append(-1 + 2*random.random())
        dre = dre / np.linalg.norm(dre)

        xleft = []
        xright = []
        for j,l in zip(x, dre):
            xleft.append(j + l*d)
            xright.append(j - l*d)
        fleft = f(xleft)
        fright = f(xright)

        for j in range(k):
            x[j] = x[j] - step*dre[j]*np.sign(fleft-fright)
        fx = f(x)
        bb.append(fx)
        if fx <= fbest:
            for j in range(k):
                xbest[j] = x[j]
            fbest = fx
        print(i+1, ": xbest = ",xbest ,"fbest = ", fbest)
        best.append(fbest)
        step = step*eta
    print(fbest)

def fun1(x,y):
    z = -20*np.exp(-0.2*np.sqrt(1/2*(x**2+y**2))) - np.exp(1/2*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y))) + 20 + np.e
    return z

fig = plt.figure(1)
ax = Axes3D(fig)
xx = np.arange(-1, 1, 0.01)
yy = np.arange(-1, 1, 0.01)
xx, yy = np.meshgrid(xx, yy)
zz = fun1(xx,yy)
ax.plot_surface(xx,yy,zz, cmap='Blues')


if __name__ == '__main__':
    run()
    x = [i for i in range(n+1)]
    xi = [i*200 for i in range(11)]
    y = best
    y1 = bb
    plt.figure('hello')
    plt.plot(x, y, marker='o', mec='r', mfc='w')
    plt.plot(x, y1)
    plt.xticks(xi)
    plt.show()
