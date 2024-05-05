import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=5
f2=3
x=np.sin(2*np.pi*f*t)
y=np.sin(2*np.pi*f2*t)
z=x-y
plt.plot(t,z)
plt.show()

