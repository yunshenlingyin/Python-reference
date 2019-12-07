# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:21:03 2019

@author: LGF
"""
import numpy as np
import scipy.stats as stats

import matplotlib.pyplot as plt

x = np.array([0.0,500.0,1000.0,1500.0,2000.0,2500.0,3000.0,3500.0])*1e-6
y = np.array([0.28,0.41,0.54,0.65,0.77,0.87,0.99,1.10])
y1 = polyfit(x,y,1)
xx = linspace(min(x)-1e-8,max(x)+1e-8,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
y2 =str(y1)
y3 = str(r2[0])
y4 = ' y=%s'%y1 + '\n R^2='+ y3
fig1 = plt.figure(dpi=300)
plt.plot(xx,polyval(y1,xx),label = y4)
plt.plot(x,y,'*')
plt.xlabel('Mass/Kg')
plt.ylabel('Voltage/V')
plt.axis([min(x)-1e-8,max(x)+1e-8,min(y)-0.1,max(y)+0.1])
print('R^2 = :\n',r2[0])
print('y is :\n',y1)
plt.legend(loc='upper left',fontsize='small')
plt.title('Coefficient of surface tension')
plt.tight_layout(pad=2.68, h_pad=None, w_pad=None, rect=None)
plt.show()
print(np.std(x))