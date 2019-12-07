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
x = [42.6,59.9,80.2,100.1,22.6]
y = [0.4194,0.5656,0.7091,0.8842,0.3063]
y1 = polyfit(x,y,1)
xx = linspace(min(x)-0.1,max(x)+0.1,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
y2 =str(y1)
y3 = str(r2[0])
y4 = 'y ='+ y2 + '\n R^2='+ y3
#plt.rcParams['savefig.dpi'] = 300 
#plt.rcParams['figure.dpi'] = 300
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('Temperature/K')
ylabel('Voltage/V')
axis([min(x)-0.1,max(x)+0.1,min(y)-0.1,max(y)+0.1])
print('R^2 = :\n',r2[0])
print('y1 is :\n',y1)
legend(loc='upper left',fontsize='small')
title('LM35')
