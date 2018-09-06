import random
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
eta = 0.9999999
c = 5
step = 10
n = 1000
k = 8
D = [[0, 10, 20, 30, 40, 50, 60, 10],
     [10, 0, 10, 20, 30, 40, 50, 60],
     [20, 10, 0, 10, 20, 30, 40, 50],
     [30, 20, 10, 0, 10, 20, 30, 40],
     [40, 30, 20, 10, 0, 10, 20, 30],
     [50, 40, 30, 20, 10, 0, 10, 20],
     [60, 50, 40, 30, 20, 10, 0, 10],
     [10, 60, 50, 40, 30, 20, 10, 0]]
best = []


def fit(x, y):
    return D[x][y]


def f(x):
    s = 0
    for i in range(k-1):
        s += fit(x[i], x[i+1])
    s += fit(x[k-1], x[0])
    return s


def mod(x):
    for i in range(k):
        x[i] = int(round(x[i]))
    for i in range(k):
        if x[i]>k-1:
            x[i]=0
        if x[i]<0:
            x[i]=k-1
    lx = [i for i in range(k)]
    lx = random.sample(lx, k)
    ll=[]
    for i in x:
        if i not in ll:
            ll.append(i)
            a=i
        else:
            a = random.choice(lx)
            ll.append(a)
        lx.remove(a)
    return ll


def run():
    global step
    x = [i for i in range(k)]
    x = random.sample(x, k)
    xbest = []
    for i in x:
        xbest.append(i)
    fbest = f(xbest)
    print('0: ', 'xbest =',xbest,' fbest =', fbest)
    best.append(fbest)

    for i in range(n):
        d = step / c
        dre = []
        for j in range(k):
            dre.append(-1 + 2*random.random())
        xleft = []
        for j in range(k):
            xleft.append(x[j] + dre[j] * d)
        xleft = mod(xleft)
        fleft = f(xleft)
        xright = []
        for j in range(k):
            xright.append(x[j] - dre[j] * d)
        xright = mod(xright)
        fright = f(xright)
        for j in range(k):
            x[j] = x[j] - step*dre[j]*np.sign(fleft-fright)
        x = mod(x)
        fo = f(x)
        if fo <= fbest:
            for j in range(len(x)):
                xbest[j] = x[j]
            fbest = fo
        print(i+1, ': xbest =',xbest,' fbest =', fbest)
        best.append(fbest)
        step = step*eta


if __name__ == '__main__':
    run()
    x = [i for i in range(n+1)]
    xi = [i*100 for i in range(11)]
    y = best
    plt.figure()
    plt.plot(x, y, marker='o', mec='r', mfc='w' )
    plt.legend()
    plt.xlabel("Generation")
    plt.ylabel("fitness")
    plt.xticks(xi)
    plt.title("TNX SOLVE TSP")
    plt.show()

