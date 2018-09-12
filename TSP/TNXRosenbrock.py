import random
import numpy as np
import matplotlib.pyplot as plt


'''
测试 Rosenbrock
使用天牛须算法测试后，效果不理想
维数越少越趋近最小值
'''


eta = 0.99      # 步长衰减
c = 5           # 步长度
step = 10       # 步长
k = 5          # 维数
n = 2000    # 迭代次数
bb = []         # 每一次迭代后的值
best = []       # 每一次迭代后的总体最佳值
p = 0.005


def f(x):       # 测试函数
    ss = 0
    for i in range(k-1):
        ss += 100*((x[i+1]-(x[i])**2)**2) + (x[i]-1)**2
    return ss


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
        rand = random.random()
        if  rand<p:
            step = 2
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



if __name__ == '__main__':
    run()
    x = [i for i in range(n+1)]
    xi = [i*200 for i in range(11)]
    y = best
    y1 = bb
    plt.plot(x, y, marker='o', mec='r', mfc='w')
    #plt.plot(x, y1)
    plt.xticks(xi)
    plt.show()