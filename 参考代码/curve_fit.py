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
y = [-0.60,-0.71,-0.64,-0.62,-0.53,-0.46,-0.30,-0.18,0.00,0.11,0.27,0.39,
0.50,0.57,0.59,0.55,0.50,0.55,0.41,0.32,0.20,-0.06,-0.04,-0.20,
-0.36,-0.44,-0.52,-0.50,-0.52,-0.46,-0.39,-0.30,-0.23,-0.07,0.04,-0.14,
0.21,0.39,0.44,0.48,0.46,0.50,0.46,0.37,0.22,0.16,0.04,0.00,
-0.18,-0.29,-0.29,-0.34,-0.43,-0.44,-0.44,-0.36,-0.29,-0.16,-0.09,0.02]
y = np.array(y)
x = np.linspace(20,1200,60)

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
M = str(a)+'exp('+str(b)+'x)'+'cos('+str(c)+'x'+str(d)+')'+'+'+str(f)




plot1 = plt.plot(x, y, '*',label='original values')
plot2 = plt.plot(xx, yvals, 'r',label=M)
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['figure.dpi'] = 300
plt.xlabel('Time/s')
plt.ylabel('Velocity/(m/s)')
axis([min(x)-0.05,max(x)+0.05,min(y)-0.05,max(y)+0.3])
legend(loc='upper left',fontsize='small')
plt.title('Damped oscillation')
plt.show()

