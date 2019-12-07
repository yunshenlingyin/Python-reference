
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
x = linspace(0.05,0.1*13,13)
y = [0.02,0.04,0.06,0.07,0.11,0.14,0.16,0.17,0.18,0.20,0.25,0.29,0.32]

y1 = polyfit(x,y,1)
xx = linspace(min(x)-0.01,max(x)+0.01,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
k = y1[1]
y2 =str(y1)
y2 = 'y ='+y2

y4 = y2 + '\n R='+ y3 
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['figure.dpi'] = 300
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('Time/s')
ylabel('Velocity/(m/s)')
axis([min(x)-0.01,max(x)+0.01,min(y)-0.1,max(y)+0.1])
print('r^2 = :\n',r2[0])

legend(loc='upper left',fontsize='small')
title('Linear acceleration4 ')

