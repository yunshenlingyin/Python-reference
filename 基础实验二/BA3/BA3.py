# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 02:27:46 2019

@author: LGF
"""
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
# Experiment 1
I = np.arange(-300,350,50)  
# I is the current, whose unit is mA
V = np.array([1.500,1.268,1.027,0.773,0.517,0.260,0.001,-0.263,-0.522,
-0.772,-1.018,-1.254,-1.479])
# V is the output voltage, whose unit is V
B = np.arange(-6,7,1)
B = B[::-1]
#B is the magnetic induction intensity, whose unit is Gauss
# Linear fit
V1 = polyfit(B,V,1)
B1 = np.linspace(min(B),max(B),500)
V1 = np.poly1d(V1)
r1 = 'y = '+str(V1)
fig1 = plt.figure(dpi=250)
plt.plot(B1,polyval(V1,B1),label=r1)
plt.legend(loc='upper left',fontsize='small')
plt.plot(B,V)
plt.plot(B,V,'*')
plt.xlabel('Magnetic induction intensity/Gauss')
plt.ylabel('Output voltage/V')
plt.title('Magnetoelectric conversion characteristics of reluctance sensor')
plt.tight_layout()
plt.show()
# Experiment 2
alpha = np.arange(0,100,10)#Unit: degree
V2 = np.array([1.034,1.014,0.963,0.890,0.780,0.668,0.504,0.320,0.143,-0.020])
fig2 = plt.figure(dpi=250)
plt.plot(alpha,V2,'*')
plt.plot(alpha,V2)
plt.xlabel(r'$\alpha (\degree)$')
plt.ylabel('Output voltage/V')
plt.title('The characteristics of direction')
plt.tight_layout()
plt.show()
x = np.arange(-0.5,0.6,0.1)*0.14
V3 = np.array([1.035,1.035,1.035,1.035,1.035,1.034,1.035,1.035,1.035,1.035,
               1.035])
fig3 = plt.figure(dpi=250)
plt.plot(x,V3,'*')
plt.plot(x,V3)
plt.xlabel('x/m')
plt.ylabel('Output voltage /V')
plt.ylim(min(V3)-0.1,max(V3)+0.1)
plt.tight_layout()
plt.show()
b = np.arange(-0.070,0.083,0.014)
B1 = 5**1.5/16*((1/(1+(1/2+b/0.14)**2)**1.5)+(1/(1+(1/2-b/0.14)**2)**1.5))
B2 = (V3-0.002923)/(-0.2522)
