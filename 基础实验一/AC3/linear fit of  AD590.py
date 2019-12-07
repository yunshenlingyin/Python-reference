# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:21:03 2019

@author: LGF
"""
from scipy import *
from matplotlib.pyplot import *
import scipy.stats as stats

import matplotlib.pyplot as plt

x = [60.8,70.7,80.3,90.1,100.1]
u = [0.3251,0.3330,0.3413,0.3508,0.3603]
y = [a*1000 for a in u]
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
ylabel('Electric current/μA')
axis([min(x)-1,max(x)+1,min(y)-1,max(y)+1])
print('R^2 = :\n',r2[0])
print('y1 is :\n',y1)
legend(loc='upper left',fontsize='small')
title('AD590')
