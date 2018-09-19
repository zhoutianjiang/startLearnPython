import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
测试 Spherical

当 eta=0.95 时，设置 rand 属性后能够有效的加快收敛速度
当 eta=0.99 时，设置 rand 属性效果不明显
                设置 step=100 效果比 step=200 显著，但貌似有时效果很差
                
说明，当值域过大时，有可能因为迭代后步长变短，达不到预期的收敛效果

当维数 k 增大时，步长并不是越大就好

eta=0.99 迭代次数越高能无限趋向于0
'''
eta = 0.99
c = 5
step = 50
#step0 = 20
n = 1000
k = 20
p = 0.05
best = []
bb=[]
Count = 0


def f(x):
    ss = 0
    for i in x:
        ss += i**2
    return ss


def run():
    global step
    global Count
    x = []
    for i in range(k):
        x.append(-100 + 200 * random.random())

    xbest = []
    for i in x:
        xbest.append(i)
    fbest = f(xbest)
    print('0: ', 'xbest =',xbest,' fbest =', fbest)
    bb.append(fbest)
    best.append(fbest)

    for i in range(n):
        '''rand = random.random()
        if i>100 and rand<p:
            step = 2'''
        d = step / c
        dre = []
        for j in range(k):
            dre.append(-1 + 2*random.random())
        dre = dre / np.linalg.norm(dre)
        xleft = []
        for j in range(k):
            xleft.append(x[j] + dre[j] * d)
        fleft = f(xleft)
        xright = []
        for j in range(k):
            xright.append(x[j] - dre[j] * d)
        fright = f(xright)
        for j in range(k):
            x[j] = x[j] - step*dre[j]*np.sign(fleft-fright)
        fo = f(x)
        bb.append(fo)
        if fo <= fbest:
            for j in range(k):
                xbest[j] = x[j]
            fbest = fo
            Count = i+1
        print(i+1, ': xbest =',xbest,' fbest =', fbest)
        best.append(fbest)
        step = step*eta


def fun(x, y):
    return  x**2+y**2


def getPic():
    fig = plt.figure(1)
    ax = Axes3D(fig)
    xx = np.arange(-100, 100, 1)
    yy = np.arange(-100, 100, 1)
    xx, yy = np.meshgrid(xx, yy)
    zz = fun(xx, yy)
    ax.plot_surface(xx, yy, zz, cmap='rainbow')
    return


if __name__ == '__main__':
    run()
    getPic()
    x = [i for i in range(n+1)]
    xi = [i*100 for i in range(11)]
    y = best
    y1 = bb
    plt.figure(2)
    plt.plot(x, y, marker='o', mec='r', mfc='w')
    plt.plot(x, y1)
    plt.xticks(xi)
    plt.show()
    '''x=0
    for  i in range(50):
        run()
        print(Count)
        x+=Count
    print(x/50)'''




