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
x = [87.9,72.8,59.9,50.6,44.5]
y = [975.9,978.4,978.9,979.1,979.5]
y1 = polyfit(x,y,1)
xx = linspace(min(x)-1,max(x)+1,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
y2 =str(y1)
y3 = str(r2[0])
y4 = 'y ='+ y2 + '\n R^2='+ y3
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['figure.dpi'] = 300
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('Temperature/K')
ylabel('Voltage/mV')
axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
print('R^2 = :\n',r2[0])
print('y1 is :\n',y1)
legend(loc='upper left',fontsize='small')
title('Thermoelectric couple')
