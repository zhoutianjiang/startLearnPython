import random
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
eta = 0.95
c = 3
step = 200
step0 = 200
n = 10000
k = 20
p = 0.05
DD = []
'''D = [[0, 1, 52, 73, 15, 45, 37, 34, 70, 1],
     [1, 0, 1, 27, 32, 96, 39, 33, 43, 74],
     [52, 1, 0, 1, 36, 52, 52, 69, 13, 63],
     [73, 27, 1, 0, 1, 79, 48, 88, 8, 14],
     [15, 32, 36, 1, 0, 1, 69, 6, 94, 67],
     [45, 96, 52, 79, 1, 0, 1, 97, 22, 86],
     [37, 39, 52, 48, 69, 1, 0, 1, 87, 69],
     [34, 33, 69, 88, 6, 97, 1, 0, 1, 22],
     [70, 43, 13, 8, 94, 22, 87, 1, 0, 1],
     [1, 74, 63, 14, 67, 86, 69, 22, 1, 0]]'''
'''D = [[0, 1, 52, 73, 15, 45, 37, 1],
     [1, 0, 1, 27, 32, 96, 39, 33],
     [52, 1, 0, 1, 36, 52, 52, 69],
     [73, 27, 1, 0, 1, 79, 48, 88],
     [15, 32, 36, 1, 0, 1, 69, 6],
     [45, 96, 52, 79, 1, 0, 1, 97],
     [37, 39, 52, 48, 69, 1, 0, 1],
     [1, 33, 69, 88, 6, 97, 1, 0]]'''
best = []
bb=[]
Count = 0


def fit(x, y):
    return DD[x][y]


def f(x):
    s = 0
    for i in range(k-1):
        s += fit(x[i], x[i+1])
    s += fit(x[k-1], x[0])
    return s


'''def mod(x):
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
    flag=[]
    t=0
    for i in x:
        if i not in ll:
            ll.append(i)
            lx.remove(i)
        else:
            flag.append(t)
        t+=1
    for i in flag:
        a = random.choice(lx)
        ll.insert(i, a)
        lx.remove(a)
    return ll'''




def mod(x):
    for i in range(k):
        x[i] = int(round(x[i]))
    for i in range(k):
        if x[i]>k-1:
            x[i]=0
        if x[i]<0:
            x[i]=k-1
    lx = [i for i in range(k)]
    ll=[]
    flag=[]
    t=0
    for i in x:
        if i not in ll:
            ll.append(i)
            lx.remove(i)
        else:
            flag.append(t)
        t+=1
    for i in flag:
        minf = fit(ll[i-1], lx[0])
        t=lx[0]
        for j in lx:
            if fit(ll[i-1], j) < minf:
                minf = fit(ll[i-1], j)
                t = j
        ll.insert(i, t)
        lx.remove(t)
    return ll


'''def mod(x):
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
    return ll'''


def readData(name):
    with open(name, 'r') as f:
        f.seek(128)
        lf = f.readlines()
        ll=[]
        for line in lf:
            ll.append(line.strip().split(' '))
        data = []
        for i in ll:
            d = []
            for j in i:
                if j == 'EOF' or j=='':
                    break
                d.append(float(j))
            data.append(d)
        print(data)
        YY=[]

        for i in range(52):
            YLine = []
            for j in range(52):
                xd = data[i][1]-data[j][1]
                yd = data[i][2]-data[j][2]
                YLine.append(int(np.sqrt(xd**2+yd**2)))
            YY.append(YLine)
        return YY

def run():
    global step
    global Count
    x = [i for i in range(k)]
    x = random.sample(x, k)
    xbest = []
    for i in x:
        xbest.append(i)
    fbest = f(xbest)
    print('0: ', 'xbest =',xbest,' fbest =', fbest)
    bb.append(fbest)
    best.append(fbest)

    for i in range(n):
        rand = random.random()
        if rand<p:
            step = step0
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
        bb.append(fo)
        if fo < fbest:
            for j in range(len(x)):
                xbest[j] = x[j]
            fbest = fo
            Count = i+1
        print(i+1, ': xbest =',xbest,' fbest =', fbest)
        best.append(fbest)
        step = step*eta


if __name__ == '__main__':
    DD = readData('berlin52.tsp')
    run()
    print(Count)
    x = [i for i in range(n+1)]
    xi = [i*500 for i in range(11)]
    y = best
    y1 = bb
    plt.figure()
    plt.plot(x, y, marker='o', mec='r', mfc='w' )
    plt.plot(x, y1)
    plt.xlabel("Generation")
    plt.ylabel("fitness")
    plt.xticks(xi)
    plt.title("TNX SOLVE TSP")
    plt.show()
    '''x=0
    for  i in range(50):
        run()
        print(Count)
        x+=Count
    print(x/50)'''



