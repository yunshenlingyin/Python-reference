#-*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:57:27 2019
@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt
f = np.array([100,300,600,1e3,3e3,6e3,1e4,3e4,6e4,1e5,3e5,6e5,1e6,3e6,6e6,1e7])
UR = np.array([1.53,1.53,1.52,1.51,1.30,0.91,0.71,0.32,0.14,7.0e-3,7.1e-3,
2.6e-3,4.7e-3,0.013,0.019,0.033])
U = np.array([2.02,1.91,2.04,2.03,2.01,2.02,2.11,2.07,2.09,2.01,2.02,2.04,2.01,
2.12,2.23,2.51])
L=1/f*1000
delta_L=-1*np.array([1.2,0.60,0.036,0.029,0.024,0.020,0.017,0.007,0.004,2.3e-3,
7.4e-4,3.0e-4,1.96e-4,4.9e-5,1.9e-5,4.4e-6])
delta_phi=2*np.pi*delta_L/L
print(len(delta_L))
fig1=plt.figure(dpi=300)
plt.semilogx(f,UR,'*')
plt.semilogx(f,UR,label=r'$U_{R}$')
plt.semilogx(f,U-UR,'.')
plt.semilogx(f,U-UR,label=r'$U_{L}$')
plt.ylim(-0.05,2.3)
plt.xlabel('Frequency/Hz')
plt.ylabel('Voltage/V')
plt.legend(loc='center right',fontsize='small')
plt.title('Amplitude frequency characteristics of circuit')
fig2=plt.figure(dpi=300)
plt.semilogx(f,delta_phi,'-*')
plt.semilogx(f,delta_phi)
plt.xlabel('Frequency/Hz')
plt.ylabel('Phase/Rad')
orginal=-0.5*np.pi*np.ones(16)
plt.semilogx(f,orginal,'-.',label=r'$y=-\frac{\pi}{2}$')
plt.title('Phase frequency characteristics')
plt.legend(loc="upper right",fontsize='small')
