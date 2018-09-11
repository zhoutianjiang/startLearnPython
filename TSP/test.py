import matplotlib.pyplot as plt


sta = 0.95
sta1 = 0.975
s = 20
z = 20
x = []
y = []
xx = []
for i in range(201):
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