
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig =plt.figure()
ax = Axes3D(fig)

data=np.loadtxt('Faradata.txt', delimiter='\t')

current=data[:,0]
bauss=data[:,1]
position=data[:,3]
#X,Y,Z=np.meshgrid(position,current,bauss)
#Z,Y=np.meshgrid(current,bauss)
X,Y=np.meshgrid(position,current)
#ax.plot(X,Y,Z)

mew=np.pi*4*10**-3
B=current*position

ax.scatter(position,current,bauss,cmap=cm.coolwarm)
#B=np.array((len(current)),(len(position)))







#ax.plot(X,Y,bauss)
ax.plot_trisurf(position,current,bauss,cmap=cm.coolwarm,linewidth=0,antialiased=True)
plt.ylabel("Current")
plt.xlabel("Position")
#plt.plot(6.5,[-1.5,3])
#plt.plot(current,bauss)
#plt.figure()
#plt.plot(current,bauss)



plt.show()
