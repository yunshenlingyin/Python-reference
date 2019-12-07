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
x = [20.1,10.3,0.0,32.1,42.0,52.8,60.7,71.2,79.9,89.6,100.6]
y = [110.0,105.2,101.9,110.9,112.9,117.9,120.9,123.6,127.8,130.9,133.6]
y1 = polyfit(x,y,1)
xx = linspace(0.0,101.9,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
y2 =str(y1)
y3 = str(r2[0])
y4 = 'y ='+ y2 + '\n r^2='+ y3

#'plt.rcParams['savefig.dpi'] = 300'
#'plt.rcParams['figure.dpi'] = 300'
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('Temperature/K')
ylabel('Resistance/$\Omega$')
axis([0.0,100.6,101.9,133.6])
print('r^2 = :\n',r2[0])
print('y1 is :\n',y1)
legend(loc='upper left',fontsize='small')
title('Pt100')
