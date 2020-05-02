# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:35:00 2019

@author: Liu Guanfu 
"""
from scipy.optimize import curve_fit
import scipy.stats as stats
import matplotlib.pyplot as plt


def func(x,a,b,c,d,f):
    return a*exp(b*x)*cos(c*x+d)+f


y = [-0.60,-0.71,-0.64,-0.62,-0.53,-0.46,-0.30,-0.18,0.00,0.11,0.27,0.39,
0.50,0.57,0.59,0.55,0.50,0.55,0.41,0.32,0.20,-0.06,-0.04,-0.20,
-0.36,-0.44,-0.52,-0.50,-0.52,-0.46,-0.39,-0.30,-0.23,-0.07,0.04,-0.14,
0.21,0.39,0.44,0.48,0.46,0.50,0.46,0.37,0.22,0.16,0.04,0.00,
-0.18,-0.29,-0.29,-0.34,-0.43,-0.44,-0.44,-0.36,-0.29,-0.16,-0.09,0.02]
y = np.array(y)
x = np.linspace(20,1200,60)/60

popt, pcov = curve_fit(func, x, y,maxfev=500000)
a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]
f = popt[4]
xx = linspace(min(x)-0.05,max(x)+0.05,2000)
yvals = func(xx,a,b,c,d,f)
r1 = np.cov(y,func(x,a,b,c,d,f))
r = r1[0,1]/np.sqrt(np.product(np.diag(r1)))
print('r等于',r)  
print('系数a:', a)
print('系数b:', b)
print('系数c:', c)
print('系数d:', d)
print('系数f:', f)

M = '{0:0.2f}exp({1:0.2f}x)cos({2:0.2f}x+{3:0.2f})+{4:0.2f}'.format(a,b,c,d,f)
fig = plt.figure(dpi=300)
plt.plot(x, y, '*',label='original values')
plt.plot(xx, yvals, 'r',label=M)
plt.xlabel('Time/min')
plt.ylabel('Velocity/(m/s)')
plt.axis([min(x)-0.05,max(x)+0.05,min(y)-0.05,max(y)+0.3])
plt.legend(loc='upper left',fontsize='small')
plt.title('Damped oscillation')
plt.grid()
plt.show()