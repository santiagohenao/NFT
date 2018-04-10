import sys
import numpy as np
import matplotlib.pyplot as plt

'''

Graficar archivos .dat en python, cosas varias.

modo de uso: $ python3 graficar.py "input.dat" (mode) (width) (height)

mode (opcional): "scatter" por defecto, o "plot".

width y height (opcionales): tamaño de la imagen, horizontal y vertical respectivamente. De no darse, se usarán los tamaños por defecto.
De darse sólo uno, se usará para ambas cosas, alto y ancho.

'''

try:
    data=np.genfromtxt(sys.argv[1])
except OSError:
    raise Exception("Archivo no encontrado.")


try:
    w=float(sys.argv[4])
except IndexError:
    w=10.
try:
    h=float(sys.argv[5])
except IndexError:
    h=7.

if len(sys.argv)>2:
    if sys.argv[2]=="usual scatter":
        plt.figure(figsize=(w,h))
        plt.scatter(data[:,0],data[:,1],s=1,c='k')
        plt.grid("On")
        plt.savefig(sys.argv[1][:-3]+"png",bbox_inches='tight')
    elif sys.argv[2]=="usual plot":
        plt.figure(figsize=(w,h))
        plt.plot(data[:,0],data[:,1],c='k')
        plt.grid("On")
        plt.savefig(sys.argv[1][:-3]+"png",bbox_inches='tight')
else:
    plt.figure(figsize=(w,h))
    plt.scatter(data[:,0],data[:,1],s=1,c='k')
    plt.grid("On")
    plt.savefig(sys.argv[1][:-3]+"png",bbox_inches='tight')
