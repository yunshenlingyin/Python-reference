
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
M = 0.10239
C = 0.05
J = 0.030
m = [0.03353,0.06897,0.08152,0.04560]
x = []
for i in range(4):
    x.append(((1-C)*M-m[i])/((1-C)*M + m[i] + J))
    


plt.figure(dpi=300)
y = [3.25,0.50,0.23,2.33]


y1 = polyfit(x,y,1)
xx = linspace(min(x)-0.01,max(x)+0.01,2000)
y1 = np.poly1d(y1)
r2 = stats.pearsonr(x,y)
k = y1[1]
y2 =str(y1)
y2 = 'y ='+y2
y3 = str(r2[0])
y4 = y2 + '\n R='+ y3
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['figure.dpi'] = 300
plot(xx,polyval(y1,xx),label = y4)
plot(x,y,'*')
xlabel('(1-C)*M-m)/((1-C)*M + m + J/R^2')
ylabel('a')
axis([min(x)-0.01,max(x)+0.01,min(y)-0.1,max(y)+0.1])
print('r^2 = :\n',r2[0])

legend(loc='upper left',fontsize='small')
title('Uniform acceleration  ')

