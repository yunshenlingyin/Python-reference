
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:21:03 2019

@author: LGF
"""
from scipy import *
from matplotlib.pyplot import *
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
x = linspace(0.04,0.32,8)
y = [0.16,0.57,0.94,1.33,1.73,2.01,2.67,2.74]
y1 = polyfit(x,y,1)
xx = linspace(min(x)-0.01,max(x)+0.01,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
y2 =str(y1)
y3 = str(r2[0])
y4 = 'y ='+ y2 + '\n R='+ y3
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['figure.dpi'] = 300
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('Time/s')
ylabel('Velocity/(m/s)')
axis([min(x)-0.01,max(x)+0.01,min(y)-0.5,max(y)+0.5])
print('r^2 = :\n',r2[0])
print('y1 is :\n',y1)
legend(loc='upper left',fontsize='small')
title('Free falling 1')

