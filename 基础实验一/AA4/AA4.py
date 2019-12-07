# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:06:56 2019

@author: LGF
"""
import numpy as np
import matplotlib.pylab as plt
"""
E1 = np.array([4.,6.,8.,10.,12.])
I1 = np.array([109.2,164.3,220.5,276.8,334.0])
I1 = I1*1e-6
R1 = E1/I1
R2 = R1-1000
print(R2)
print(np.mean(R2))
"""
"""
k = np.array([1.1,10.1,20.1,30.1,40.1,50.1,60.1,70.1,80.1,90.1])*1e-2
V1 = np.array([0.0238,0.1248,0.1997,0.2617,0.3168,0.3666,0.4135,0.4586,0.4981,0.5266])
R = (12-V1)/V1*1000
fig1 = plt.figure(dpi=150)
plt.xlabel('duty circle')
plt.ylabel('Resistance/$\Omega$')
plt.plot(k,R,'.')
plt.plot(k,R)
plt.show()
"""
lambda1 = np.array([535,630,695])
V1 = np.array([0.1244,0.6800,0.5561])
R = (12-V1)/V1*1000
fig1 = plt.figure(dpi=150)
plt.xlabel('$\lambda$/nm')
plt.ylabel('Resistance/$\Omega$')
plt.plot(lambda1,R,'.')
plt.plot(lambda1,R)
plt.show()













