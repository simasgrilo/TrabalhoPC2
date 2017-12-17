import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags

def diffusion_Crank_Nicolson(dy,ny,dt,nt,D,V,ntout):
    Vout = [] # list for storing V arrays at certain time steps
    V0 = V[0] # boundary condition on left side
    V1 = V[-1] # boundary condition on right side
    s = D*dt/dy**2  # diffusion number
    # create coefficient matrix:
    A = diags([-0.5*s, 1+s, -0.5*s], [-1, 0, 1], 
          shape=(ny-2, ny-2)).toarray() 
    B1 = diags([0.5*s, 1-s, 0.5*s],[-1, 0, 1], shape=(ny-2, ny-2)).toarray()
    for n in range(1,nt): # time is going from second time step to last
        Vn = V
        B = np.dot(Vn[1:-1],B1) 
        B[0] = B[0]+0.5*s*(V0+V0)
        B[-1] = B[-1]+0.5*s*(V1+V1)
        V[1:-1] = np.linalg.solve(A,B)
        if n % int(nt/float(ntout)) == 0 or n==nt-1:
            Vout.append(V.copy()) # numpy arrays are mutable, 
            #so we need to write out a copy of V, not V itself
    return Vout,s
 
dt = 0.001 # grid size for time (s)
dy = 0.001 # grid size for space (m)
viscosity = 2*10**(-4) # kinematic viscosity of oil (m2/s)
y_max = 0.04 # in m
y = np.arange(0,y_max+dy,dy) 
ny = len(y)
nt = 1000
plt.figure(figsize=(7,5))
V = np.zeros((ny,)) # initial condition
V[0] = 10
Vout,s = diffusion_Crank_Nicolson(dy,ny,dt,nt,viscosity,V,10)
 
for V in Vout:
    plt.plot(y,V,'k')
plt.xlabel('distance from wall (m)',fontsize=12)
plt.ylabel('velocity (m/s)',fontsize=12)
plt.axis([0,y_max,0,V[0]])
plt.title('Crank-Nicolson scheme',fontsize=14)
plt.show()