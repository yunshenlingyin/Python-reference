# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:16:14 2019

@author: LGF
"""
"""
log plotting;resistance,capacitance,inductance.
"""
from scipy.optimize import curve_fit
from scipy import *
from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt

resistance_AC = [1.994,1.999,1.999,1.999,1.998,1.996]
resistance_x  = [1.445,1.447,1.446,1.457,1.454]
capacitance_AC = [2.000,1.998,2.000,2.002,2.004]
capacitance_x  = [1.984,1.706,0.3659,0.04007,0.003021]
inductance_AC = [1.999,2.002,2.003,2.005,2.007]
inductance_x = [0.8823,1.859,1.954,2.044,2.028]
x_AC1 = []
x_AC2 = []
x_AC3 = []
for i in range(5):
    a1 = resistance_x[i]/resistance_AC[i]
    a2 = capacitance_x[i]/capacitance_AC[i]
    a3 = inductance_x[i]/inductance_AC[i]
    x_AC1.append(a1)
    x_AC2.append(a2)
    x_AC3.append(a3)

x = [1e2,1e3,1e4,1e5,1e6]
x_AC11 = polyfit(x,x_AC1,1)
m1 = np.poly1d(x_AC11)
m1 = str(m1)
def capacitance_fit(x,k1):
    return 1/(((k1*x)**2+1)**0.5)
# C = k1/400pi
xx = linspace(1e2,1e6,200000)
popt, pcov = curve_fit(capacitance_fit, x,x_AC2)
k1 = popt[0]
k1 = round (k1,6)
x_AC2vals = capacitance_fit(xx,k1)
def inductance_fit(x,k2):
    return k2*x/(((k2*x)**2+200**2)**0.5)
# L = k2/2pi
popt,pcov = curve_fit(inductance_fit,x,x_AC3)
k2 = popt[0]
x_AC3vals = inductance_fit(xx,k2)
k2 = round (k2,6)
fig1 = plt.figure(dpi=300)
plt.semilogx(xx,polyval(x_AC11,xx),label=m1)
plt.semilogx(x,x_AC1,'*',label='data points')
legend(loc='upper left',fontsize='small')
plt.title('resistance')
fig2 = plt.figure(dpi=300)
k1 = str(k1)
k1 = '1/((('+k1+'*x)**2+1)**0.5)'
plt.xlabel('Frequency/(s^-1)')
plt.ylabel('U_x/U_AC')
plt.semilogx(xx,x_AC2vals,label=k1)
plt.semilogx(x,x_AC2,'*',label='data points')
legend(loc='upper right',fontsize='small')
plt.title('capacitance')
fig3 = plt.figure(dpi=300)
k2 = str(k2)
k2 = k2+'*x/((('+k2+'*x)**2+200**2)**0.5)'
plt.semilogx(xx,x_AC3vals,label=k2)
plt.semilogx(x,x_AC3,'*',label= 'data points')
axis([50,1e5+1e4,-0.03,1.2])
legend(loc='upper left',fontsize='small')
plt.xlabel('Frequency/(s^-1)')
plt.ylabel('U_x/U_AC')
plt.title('inductance')