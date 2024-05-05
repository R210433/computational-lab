import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
plt.xlabel('time')
plt.ylabel('amplitute')
plt.title('sine wave')
k=input("enter your wave:")
dic={'s1':[2,5],'s2':[5,10],'s3':[3,7],'s4':[10,12],'s5':[1,2]}
if dic[k]:
	x=dic[k][0]*np.sin(2*np.pi*dic[k][1]*t)
	plt.plot(t,x)
	plt.show()

