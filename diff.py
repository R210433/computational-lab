import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def myODE(y, t):
    return -0.5 * y
t = np.linspace(0, 10, 100) 
y0 = 1
y = odeint(myODE, y0, t)
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the Differential Equation')
plt.show()
