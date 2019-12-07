# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:54:40 2019

@author: LGF
"""
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
# 解的方程是d^2f(x)/dt^2  = -f(x),df(x)/dt = g(x)
dt,f0,g0,n = (np.pi-0)/1000,0,0,1000
f = zeros((n,1),float)
g = zeros((n,1),float)
t = zeros((n,1),float)
d = zeros((n,1),float)
l = zeros((3,1),float)
g00, g01=0,1.5
x = np.linspace(0,np.pi,n)
f[0], g[0] = 0,g00   
for i in range(1,n):
    f[i] = g[i-1]*dt + f[i-1]
    g[i] = g[i-1] - f[i-1]*dt
    d[i] = np.sin(i*dt)
l[0] = d[999]-f[999]
f[0], g[0] = 0,g01  
for i in range(1,n):
    f[i] = g[i-1]*dt + f[i-1]
    g[i] = g[i-1] - f[i-1]*dt
k=0
l[1] = d[999]-f[999]
while np.abs(l[0])>3e-5 and np.abs(l[1])>3e-5 and k<100:
   
    if  l[0]*l[1]< 0:
        g02 = (g00+g01)/2
        k+=1
        f[0], g[0] = 0,g02
        for i in range(1,n):
            f[i] = g[i-1]*dt + f[i-1]
            g[i] = g[i-1] - f[i-1]*dt
        l[2]=d[999]-f[999]
        if  np.abs(l[2])>3e-5 and l[2]*l[1]< 0:
            l[0],g00=l[2],g02  
        elif  np.abs(l[2])>3e-5 and l[2]*l[0]< 0:
            l[1],g01=l[2],g02  
    elif l[0]==0 or l[1]==0 or np.abs(l[0])<=3e-5 or np.abs(l[1])<=3e-5:
        fig1 = plt.figure(dpi=300)
        plt.xlabel('Time/s')
        plt.ylabel('Displacement/m')
        plt.plot(x,d)
        plt.plot(x,f)
        print(g[0])
        plt.show()
        plt.tight_layout()
fig1 = plt.figure(dpi=300)
plt.xlabel('Time/s')
plt.ylabel('Displacement/m')
plt.plot(x,d,color='red')
plt.plot(x,f,color='blue')
print(g[0])
plt.show()
plt.tight_layout()
     
    








"""
fig1 = plt.figure(dpi=300)
plt.xlabel('Time/s')
plt.ylabel('Displacement/m')
plt.plot(x,d)
plt.plot(x,f)

plt.show()
plt.tight_layout()
np.abs(l[0])>3e-5 and np.abs(l[1])>3e-5 and l[0]*l[1]< 0
"""