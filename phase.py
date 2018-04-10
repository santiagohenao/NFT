import numpy as np
import matplotlib.pyplot as plt
import sys

Vround=np.vectorize(round)

def Phase(t):
    return ((t-t_0)/T)-(Vround((t-t_0)/T))

vPhase=np.vectorize(Phase)

try:
    data=np.genfromtxt(sys.argv[1])
except OSError:
    raise Exception("Archivo no encontrado.")

HJD=data[:,0]
Mag=data[:,1]

t_0=HJD[list(Mag).index(max(Mag))]
T=float(sys.argv[2])

Ph=vPhase(HJD)
Ph=list(Ph)+list(Ph+1)
Mag=list(Mag)*2

plt.scatter(Ph,Mag,s=10,c='k')
plt.show()
