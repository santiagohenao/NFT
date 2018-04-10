import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

'''
python3 period.py "input.dat" percent
Lee la transformada de fourier "input.dat" y encuentra los máximos locales mayores a cierto porcentaje del máximo.
'''


try:
    data=np.genfromtxt(sys.argv[1])
except OSError:
    raise Exception("Archivo no encontrado.")

try:
    umbra=float(sys.argv[2])/100
except IndexError:
    umbra=0.5

ss=data[:,1]
fs=data[:,0]

smax=[]
fmax=[]

indexes=np.array(argrelextrema(ss, np.greater))[0]


for i in indexes:
    smax.append(ss[i])
    fmax.append(fs[i])

print("Frecuencia:\t Período:\t\t Intensidad(sobre 100):")
for i in range(len(smax)):
    if smax[i]>=max(ss)*umbra:
        print(fmax[i],1/fmax[i],100*smax[i]/max(smax),sep="\t\t")
