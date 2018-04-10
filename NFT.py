import sys
import numpy as np

'''
Non-equidistan Fourier Transform
Uso: python3 Fourier.py "datos.dat" f0 ff step "output.dat"
el espacio de frecuencias será [f0,ff] con obvios pasos de step.
EL resultado se guardará en "output.dat"
'''

Vround=np.vectorize(round)

def DiscreteTransform(freq,x,y):
    N=len(y)
    s=[(y[i])*np.exp(-2*np.pi*1j*freq*x[i]) for i in range(N)]
    return np.sum(s)


filename=sys.argv[1]
f0=float(sys.argv[2])
ff=float(sys.argv[3])
step=float(sys.argv[4])
outname=sys.argv[5]

data=np.genfromtxt(filename)
X=data[:,0]
Y=data[:,1]
Y=Y-np.mean(Y)
fspace=np.arange(f0,ff+step,step)
sspace=[abs(DiscreteTransform(f,X,Y)) for f in fspace]

np.savetxt(outname,np.transpose(np.array([fspace,sspace])),delimiter="\t")
