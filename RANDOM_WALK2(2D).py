# Random walk in 2D. mean , end-to end distance vs time

import numpy as np
import matplotlib.pyplot as plt
from random import choice
import numpy.polynomial.polynomial as poly

# Function to create walks

def walks(steps):
    x,y=0,0
    pos=[]
    for i in range(steps):
        dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
        x,y=x+dx,y+dy
        pos.append(np.sqrt(x**2+y**2))
    return pos
# To create a set of walks
steps,config=1000,1000
walks=np.array([walks(steps)for i in range(config)])

# Cummulative sum , mean
c_walk=np.cumsum(walks,axis=1)
m_walk=np.mean(c_walk,axis=0)
# Timescale ,mean distance in log scale
t=np.log(range(1,steps+1))
r=np.log(m_walk)

# To fit data in linear scale
coeffs=poly.polyfit(t,r,1)
rfit=poly.polyval(t,coeffs)
print (coeffs)
# Existence of fitted data for plot
t_ext=np.insert(t,0,0)
r_ext=np.insert(rfit,0,coeffs[0])

# To plot

plt.plot(t,r,'o')
plt.plot(t_ext,r_ext,'-')
plt.xlabel('log(time)',fontsize=18)
plt.ylabel('log($<R>$)',fontsize=18)
plt.title('Random walk in 2D',fontsize=20)
plt.show()



































