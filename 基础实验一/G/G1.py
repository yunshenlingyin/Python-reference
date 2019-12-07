# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:35:00 2019

@author: LGF
"""
from scipy.optimize import curve_fit
from scipy import *
from matplotlib.pyplot import *
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib
from IPython.core.pylabtools import figsize 
def func(x,a,b,c,d,f):
    return a*exp(b*x)*cos(c*x+d)+f
"""y = np.array([14.0,15.0,16.0,17.0,18.0,19.2,20.2,21.4,
              22.2,23.2,24.0,24.8,25.0,25.4,25.8,25.6,
              25.2,25.0,24.2,23.4,22.6,21.8,21.0,20.0,
              19.2,18.0,17.0,16.8,16.2,16.0,15.8,16.0,
              16.0,16.2,16.8,17.2,18.0,18.8,19.6,20.2,
              21.0,22.0,22.8,23.2,23.8,24.4,24.8,24.8,
              24.6,24.4,23.8,23.4,23.0,22.0,21.4,20.8,
              20.2,19.6,18.8,18.0,17.6,17.0,17.0,16.8,
              16.8,17.0,17.2,17.6,18.0,18.8,19.2,19.8,
              20.4,21.0,21.6,22.2,23.0,23.2,23.4,23.6])"""
y = np.array([21.8,21.8,22.0,22.0,21.4,20.4,19.8,18.8,
              18.0,16.8,15.8,14.6,13.8,12.6,11.6,10.8,
              10.2,9.8,9.8,9.8,10.0,10.2,10.8,11.4,
              12.2,13.0,14.2,15.0,16.0,17.0,17.8,18.8,
              19.2,19.8,20.0,20.2,20.0,19.8,19.4,19.0,
              18.2,17.4,16.6,15.8,14.8,14.0,13.2,12.4,
              11.8,11.2,10.8,11.0,11.0,11.2,11.2,11.8,
              12.2,12.8,13.6,14.2,14.8,15.8,16.4,17.0,
              17.8,18.2,18.8,18.8,19.0,19.0,18.8,18.4,
              18.0,17.8,17.0,16.2,15.4,14.0,13.8,13.2])
x = np.linspace(0.25,20,80)
popt, pcov = curve_fit(func, x, y)
print(popt)
a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]
f = popt[4]
xx = linspace(min(x)-0.05,max(x)+0.05,2000)
yvals = func(xx,a,b,c,d,f)
r2 = stats.pearsonr(x,y)
print('r 等于',r2[0])
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数c:', c)
print('系数d:', d)
print('系数f:', f)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
#绘图
plt.figure(dpi=300)
a = round(a,2)
b = round(b,2)
c = round(c,2)
d = round(d,2)
f = round(f,2)
M = str(a)+'exp('+str(b)+'x)'+'cos('+str(c)+'x'+'+'+str(d)+')'+'+'+str(f)




plot1 = plt.plot(x, y, '*',label='original values')
plot2 = plt.plot(xx, yvals, 'r',label=M)
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300
plt.xlabel('Time/min')
plt.ylabel('X/(m/s)')
axis([min(x)-0.05,max(x)+0.05,min(y)-0.05,max(y)+0.3])
legend(loc='upper left',fontsize='small')
plt.title('Measure G')
plt.show()
print(y.shape)
