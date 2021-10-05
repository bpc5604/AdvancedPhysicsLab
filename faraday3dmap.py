import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig =plt.figure()
ax = Axes3D(fig)

data=np.loadtxt('Faradata.txt', delimiter='\t')

current=data[:,0]
bauss=data[:,1]
position=data[:,3]*100

ax.scatter(position,current,bauss)
plt.ylabel("Current")
plt.xlabel("Position")

plt.show()
