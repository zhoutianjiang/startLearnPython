import matplotlib.pyplot as plt


sta = 0.99
sta1 = 0.975
s = 4
z = 4
x = []
y = []
xx = []
for i in range(2001):
    s = s*sta1
    #s = s-i/10000
    z = z*sta
    x.append(i+1)
    y.append(s)
    xx.append(z)
print(y)
print(x)
plt.plot(x, y, color='red')
plt.plot(x, xx, color='blue')
plt.show()