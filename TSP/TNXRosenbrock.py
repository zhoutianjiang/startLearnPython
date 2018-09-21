import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


'''
测试 函数
使用天牛须算法测试后，效果不理想
维数越少越趋近最小值
'''


eta = 0.99      # 步长衰减
c = 5           # 步长度
step = 20       # 步长
k = 20          # 维数
n = 2000    # 迭代次数
bb = []         # 每一次迭代后的值
best = []       # 每一次迭代后的总体最佳值
p = 0.005


'''def f(x):       # 测试函数Rosenbrock
    ss = 0
    for i in range(k-1):
        ss += 100*((x[i+1]-(x[i])**2)**2) + (x[i]-1)**2
    return ss'''


'''def f(x):      # 测试函数Rastrigin
    ss = 0
    for i in x:
        ss += i**2 - 10*np.cos(2*np.pi*i) + 10
    return ss'''


def f(x):      # 测试函数Griewank
    ss = 0
    sk = 1
    for i in range(k):
        ss += x[i] ** 2
        sk *= np.cos(x[i] / (np.sqrt(i+1)))
    return 1/4000*ss - sk + 1


def run():
    global step
    x = []
    for i in range(k):
        x.append(-10 + 20*random.random())
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


def fun1(x, y):      # Rosenbrock
    s = 100*((y-x**2)**2) + (x-1)**2
    return  s


def fun2(x, y):     # Rastrigin
    s = x**2-10*np.cos(2*np.pi*x)+10 + y**2-10*np.cos(2*np.pi*y)+10
    return s


def fun3(x, y):     # Griewank
    s = 1/4000*(x**2+y**2) - np.cos(x/np.sqrt(1))*np.cos(y/np.sqrt(2)) + 1
    return s


def getPic1():
    fig = plt.figure(1)
    ax = Axes3D(fig)
    xx = np.arange(-10, 10, 0.1)
    yy = np.arange(-10, 10, 0.1)
    xx, yy = np.meshgrid(xx, yy)
    zz = fun1(xx, yy)
    ax.plot_surface(xx, yy, zz, cmap='rainbow')
    return


if __name__ == '__main__':
    run()
    getPic1()
    x = [i for i in range(n+1)]
    xi = [i*200 for i in range(11)]
    y = best
    y1 = bb
    plt.figure(2)
    plt.plot(x, y, marker='o', mec='r', mfc='w')
    plt.plot(x, y1)
    plt.xticks(xi)
    plt.show()