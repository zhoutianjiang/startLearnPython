import random
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
eta = 0.99
c = 5
step = 200
#step0 = 20
n = 1000
k = 20
#p = 0.05
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
        if rand<p:
            step = step0'''
        d = step / c
        dre = []
        for j in range(k):
            dre.append(-1 + 2*random.random())
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
        if fo < fbest:
            for j in range(k):
                xbest[j] = x[j]
            fbest = fo
            Count = i+1
        print(i+1, ': xbest =',xbest,' fbest =', fbest)
        best.append(fbest)
        step = step*eta


if __name__ == '__main__':
    run()
    x = [i for i in range(n+1)]
    xi = [i*100 for i in range(6)]
    y = best
    y1 = bb
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




