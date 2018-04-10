import numpy as np

l=101

def cuerda(t,d,L,h):
    if t<=d:
        return (h/d)*t
    elif d<t<=L:
        return (-h/(L - d))*t + ((h*L)/(L - d))

cuerda_ejemplo=lambda t: cuerda(t,3.3333333,10,1)

def make_periodic(f,T,a=0,b=0):
    '''
    This make a "saw" function with the function f and a period T;
    makes the function repeats itself on intervals from b to b+T, with displacement a
    '''
    def p(x):
        return f((x-a)-T*np.floor((x-a)/T)+b)
    return p



f=make_periodic(cuerda_ejemplo,10)
vf=np.vectorize(f)

x=np.linspace(5000,10000,l)+80*np.random.rand(l)
y=(np.sin(x*2*np.pi*0.5)+np.sin(x*2*np.pi*0.3)+3*np.random.rand(l))/4+17

x=x+np.random.rand(l)/10

xf=list(x)[:int(round(l/3))]+list(x)[int(round(2*l/3)):]
yf=list(y)[:int(round(l/3))]+list(y)[int(round(2*l/3)):]

for i in range(len(xf)):
    print(xf[i],yf[i],sep="\t")
