
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
x = [0.53,0.73,0.90,1.09,1.25]
y = [40063,40086,40107,40128,40147]

y1 = polyfit(x,y,1)
xx = linspace(min(x)-0.01,max(x)+0.01,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
k = y1[1]
y2 =str(y1)
y2 = 'y ='+y2
u = 40001/k
u = str(u)
y4 = y2 + '\n R='+ y3 + '\n u ='+u
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['figure.dpi'] = 300
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('Velocity/(m/s)')
ylabel('Frequency/s^-1')
axis([min(x)-0.01,max(x)+0.01,min(y)-0.5,max(y)+0.5])
print('r^2 = :\n',r2[0])

print(k,u)
legend(loc='upper left',fontsize='small')
title('Doppler effect')

