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
x = [88.8,100.8,78.3,69.6,59.5,50.0,40.8,32.3,19.3,9.9,0.3]
y = [810.0,877.0,725.6,642.5,569.3,493.0,419.9,366.9,297.2,247.2,199.9]
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
ylabel('Resistance/$\Omega$')
axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
print('R^2 = :\n',r2[0])
print('y1 is :\n',y1)
legend(loc='upper left',fontsize='small')
title('Pt100')
