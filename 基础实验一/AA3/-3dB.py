# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:47:17 2019

@author: LGF
"""
from scipy.optimize import curve_fit
from scipy import *
from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize 

x = [100,1e3,1e4,1e5,1e6,1e7,2*1e6,1.5*1e6,1.4*1e6,1.392*1e6]
Vrms = [3.63,3.59,3.60,3.64,3.67,4.33,3.60,3.58,3.58,3.58]
V_rms = [3.558,3.560,3.559,3.599,2.773,0.313,1.586,2.222,2.384,2.397]
n = len(x)
frac = []
for i in range(n):
    a1 = V_rms[i]/Vrms[i]
    frac.append(a1)
def func(x,r,R,c):
    return R/(((R+r)**2 + (R*r*c*2*pi*x)**2)**0.5)
xx = linspace(min(x)-20,max(x)+1e6,20000)
popt, pcov = curve_fit(func,x,frac)
r = popt[0]
R = popt[1]
c = popt[2]
fracvals = func(xx,r,R,c)
y1 = 20000*[0.707]

f = ((R**2/0.707**2-(R+r)**2)/((R*r*c*2*pi)**2))**0.5
f = format(f,'.6e')
f = str(f)
f = 'f='+ f +' Hz'
fig1 = plt.figure(dpi=300)

plt.ylabel('V\'rms/Vrms')
plt.xlabel('Frequency')
plot1=plt.semilogx(x,frac,'*',label='data points')
plot2=plt.semilogx(xx,fracvals,label='curve_fit')
plot3=plt.semilogx(xx,y1,'--',label='y=0.707')
legend(loc= 'upper right',fontsize= 'small')

plt.title('-3dB     ' + f)








