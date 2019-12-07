#-*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:57:27 2019
@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt
f = np.array([100,300,600,1e3,3e3,6e3,1e4,15e3,20e3,30e3,1.5e3,1.6e3,1.7e3,
1.8e3,1.9e3,2.0e3])
f=np.sort(f)
IR=np.array([1.3,1.6,2.9,5.7,14,15,16,16,16,11,6.3,2.9,1.6,1.1,0.9,0.68])*0.001
U = np.array([2.01,2.00,1.96,2.01,1.96,1.92,1.94,2.07,2.08,2.02,1.97,2.02,2.05,
2.06,2.07,2.06])
L=1/f*1000
delta_L=np.array([2.5,0.076,0.035,0.017,0.05,0.02,0.014,-0.006,-0.022,-0.03,
-0.052,-0.035,-0.023,-0.015,-0.012,-0.0076])
delta_phi=2*np.pi*delta_L/L
delta_phi1=360*delta_L/L
print(len(delta_L))
op=np.sqrt(0.5)*max(IR)*np.ones(16)
#A=np.vstack((f,UR,U,L,))
fig1=plt.figure(dpi=240)
plt.semilogx(f,IR,'*')
plt.semilogx(f,IR,label=r'$I_{R}$')
#plt.semilogx(f,U-UR,'.')
#plt.semilogx(f,U-UR,label=r'$U_{L}$')
plt.ylim(0.0,0.02)
plt.semilogx(f,op,'.-',label=r'$\frac{\sqrt{2}}{2}I_{R}$')
plt.xlabel('Frequency/Hz')
plt.ylabel('Current/A')
plt.legend(loc='center right',fontsize='small')
plt.title('Amplitude frequency characteristics of circuit')
plt.tight_layout()
plt.show()
fig2=plt.figure(dpi=240)
plt.semilogx(f,delta_phi,'-*')
plt.semilogx(f,delta_phi)
plt.xlabel('Frequency/Hz')
plt.ylabel('Phase/Rad')
orginal=-0.5*np.pi*np.ones(16)
plt.semilogx(f,orginal,'-.',label=r'$y=-\frac{\pi}{2}$')
plt.semilogx(f,-orginal,'.-',label=r'$y=\frac{\pi}{2}$')
plt.title('Phase frequency characteristics')
plt.legend(loc="center right",fontsize='small')
plt.tight_layout()
plt.show()




















