import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y =[6,5,4,3,2,1]
z=[7,7,7,7,7,7]
N = 6
n = np.arange(N)
l=len(x)
q= np.linspace(-np.pi, np.pi, 1000)
for i in range(0,l-1):
  X = np.array([np.sum(x[i] * np.exp(-1j * w * n)) for w in q])
for i in range(0,l-1):
  Y = np.array([np.sum(y[i] * np.exp(-1j * w * n)) for w in q])
for i in range(0,l-1):
  Z = np.array([np.sum(z[i] * np.exp(-1j * w * n)) for w in q])
#x
plt.subplot(2, 1, 1)
plt.plot(q, np.abs(X+Y))
#y
plt.subplot(2, 1, 2)
plt.plot(q, np.abs(Z))

plt.show()
