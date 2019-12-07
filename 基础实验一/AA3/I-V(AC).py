# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:27:18 2019

@author: LGF
direct currency 
"""
from scipy import *
from matplotlib.pylab import *
# resistance plot 
I1 = [0,0.737,1.405,2.109,2.813,3.515,4.217,4.922,5.625,6.325,
      7.032]
I1 = [b*1e-3 for b in I1]
V1 = [0,0.3558,0.708,1.063,1.417,1.777,2.125,2.480,2.834,
      3.187,3.543]
fig1 = plt.figure(dpi=300)
plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V1,I1,'*')
plt.plot(V1,I1)
#capacitance plot
I2 = [-0.013,0.030,0.074,0.124,0.169,0.214,0.259,0.304,0.385,0.433,0.485]
I2 = [b*1e-6 for b in I2]
V2 = [0.,0.497,0.993,1.490,1.985,2.481,2.978,3.475,3.97,4.46,4.96]
fig2 = plt.figure(dpi=300)
plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V2,I2,'*')
plt.plot(V2,I2)
#inductance plot 
I3 = [0.104*1e-3,1.412,2.824,4.236,5.644,7.049,8.449,9.856,11.246,12.631,
      14.025]
I3 = [b*1e-3 for b in I3]
V3 = [0.,0.2101,0.418,0.628,0.837,1.047,1.257,1.469,1.682,1.894,2.108]
fig3 = plt.figure(dpi=300)
plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V3,I3,'*')
plt.plot(V3,I3)


