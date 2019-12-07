# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:58:00 2019

@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy import *


Time1 = np.array([0,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,
63,66,69,72,75,78,81,84,87,90,93,96,99])
Temperature = np.array([16.9,16.7,16.5,16.1,15.8,15.5,15.1,15.0,
14.8,14.7,14.6,14.3,14.2,13.9,13.8,13.6,13.3,13.0,12.9,12.7,12.6,12.5,12.4,12.3,
12.2,12.2,12.2,12.1,12.1,12.1,12.1])
a = [3]*31
a= np.array(a)
Time1 = Time1+a

fig1 = plt.figure(dpi=100)
plt.axis([0,120,9.9,19.0])
plt.xlabel('Time/s')
plt.ylabel('Temperature/$^\circ$C')
plt.plot(Time1,Temperature)
plt.plot(Time1,Temperature,'*')
plt.title('melting heat of ice ')
plt.show()
m = 11.68
m1 = 32.77
m0 = 99.39
c0 = 4.18
c1 = 0.9
m2c2 = 1.9*2
t0 = 17.4
t1 = 12.1
L = 1/m*((m0*c0+m1*c1+m2c2)*(t0-t1)-m*c0*t1)

# pure water 
Time2 = np.linspace(0,9,10)
Temperature10 = np.array([35.0,31.5,29.0,28.0,27.4,27.0,26.8,26.7,26.6,26.5])
Temperature11 = [26.2]*10
Temperature11 = np.array(Temperature11)
T1=np.log((Temperature10-Temperature11))
y1 = polyfit(Time2,T1,1)
xx = linspace(-0.5,9.5,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(Time2,T1)
y2 =str(y1)
y3 = str(r2[0])
y4 = 'y ='+ y2 + '\n r='+ y3
fig2 = plt.figure(dpi=1000)
plt.plot(xx,polyval(y1,xx),label = y4)
plt.xlabel('Time/s')
plt.ylabel('ln($\Theta$-$\Theta$0)')
plt.legend(loc='upper right',fontsize='small')
plt.title('Pure water')
plt.axis([-0.5,9.5,-1.6,2.3])
plt.plot(Time2,T1,'*')
Time2 = np.linspace(0,9,10)
Temperature20 = np.array([36.6,32.3,29.4,28.0,27.2,26.8,26.6,26.5,26.3,26.2])
Temperature21 = [25.6]*10
Temperature21 = np.array(Temperature21)
T2=np.log((Temperature20-Temperature21))
y1 = polyfit(Time2,T2,1)
xx = linspace(-0.5,9.5,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(Time2,T2)
y2 =str(y1)
y3 = str(r2[0])
y4 = 'y ='+ y2 + '\n r='+ y3
fig3 = plt.figure(dpi=1000)
plt.plot(xx,polyval(y1,xx),label = y4)
plt.xlabel('Time/s')
plt.ylabel('ln($\Theta$-$\Theta$0)')
plt.legend(loc='upper right',fontsize='small')
plt.title('Salt water')
plt.axis([-0.5,9.5,-1.6,2.3])
plt.plot(Time2,T2,'*')
m1 = 17.46;m2=23.78;m11=83.50;c1=4.18;c2=0.389;s1=-0.369;s2=-0.316;
cx=1/m2*((s1/s2)*(m1*c1+m11*c2)-(m11*c2))

T  = np.array([-20,17,42,94,127])
P  = np.array([65,75,85,95,105])
a  = T*P
b = sum(a)
P1 = P * P
c = sum(P1)
y1 = polyfit(T,P,1)


