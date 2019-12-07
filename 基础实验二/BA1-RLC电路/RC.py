#-*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:57:27 2019
@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt
f = np.array([100,300,600,1e3,3e3,6e3,1e4,3e4,6e4,1e5,3e5,6e5,1e6,3e6,6e6,1e7])
UR = np.array([0.23,0.64,1.08,1.41,1.81,1.96,1.96,1.96,1.97,1.97,1.98,1.97,
1.97,1.97,1.98,1.87])
U = np.array([2.02,2.01,1.97,1.95,1.92,1.92,1.94,1.94,1.94,1.94,1.94,1.94,1.94,
1.94,1.95,1.92])
L=1/f*1000
delta_L=np.array([2.1,0.66,0.27,0.11,0.018,4.0e-3,1.2e-3,0,0,0,0,0,0,0,0,0])
delta_phi=2*np.pi*delta_L/L
print(len(delta_L))
fig1=plt.figure(dpi=240)
plt.semilogx(f,UR,'*')
plt.semilogx(f,UR,label=r'$U_{R}$')
plt.semilogx(f,U-UR,'.')
plt.semilogx(f,U-UR,label=r'$U_{C}$')
plt.ylim(-0.05,2.02)
plt.xlabel('Frequency/Hz')
plt.ylabel('Voltage/V')
plt.legend(loc='center right',fontsize='small')
plt.title('Amplitude frequency characteristics of circuit')
plt.tight_layout()
plt.show()
fig2=plt.figure(dpi=300)
plt.semilogx(f,delta_phi,'-*')
plt.semilogx(f,delta_phi)
orginal=0.5*np.pi*np.ones(16)
plt.semilogx(f,orginal,'-.',label=r'$y=\frac{\pi}{2}$')
plt.xlabel('Frequency/Hz')
plt.ylabel('Phase/Rad')
plt.title('Phase frequency characteristics')
plt.legend(loc="center right",fontsize='small')
plt.tight_layout()
plt.show()