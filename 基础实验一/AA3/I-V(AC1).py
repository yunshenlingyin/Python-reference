# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:27:18 2019

@author: LGF
direct currency 
"""
from scipy import *
from matplotlib.pylab import *
# resistance plot 
I1 = [0.0008,0.4688,0.9310,1.3865,1.8453,2.3029,2.7630,3.2254,3.6959,
      4.1676,4.6377]
I1 = [b*1e-3 for b in I1]
V1 = [0.002,0.228,0.457,0.693,0.910,1.137,1.364,1.593,1.826,2.060,2.294]
fig1 = plt.figure(dpi=300)
plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V1,I1,'*')
plt.plot(V1,I1,label='resistance')
#capacitance plot
I2 = [0.0024,0.7910,1.5941,2.4003,3.2333,4.0530,4.8922,5.7405,6.6109,7.4882,
      8.3661]
I2 = [b*1e-3 for b in I2]
V2 = [0.001,0.283,0.561,0.830,1.098,1.363,1.626,1.890,2.157,2.423,2.680]

plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V2,I2,'*')
plt.plot(V2,I2,'--',label='capacitance')
#inductance plot 
I3 = [0.0029,0.8419,1.6643,2.4536,3.2581,4.0596,4.8591,5.6604,6.4779,
      7.2959,8.1098]
I3 = [b*1e-3 for b in I3]
V3 = [0.002,0.165,0.333,0.490,0.667,0.837,1.007,1.179,1.355,1.532,1.708]

plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V3,I3,'*')
plt.plot(V3,I3,':',label='inductance')
#diode plot 
V4 = [0.002,0.066,0.135,0.203,0.272,0.338,0.393,0.445,0.493,0.534,0.595,0.817,
      1.020,1.217,1.412,1.580,1.777,1.973,2.169]
I4 = [0.,0.,0.,0.,0.0068,0.0365,0.0700,0.1324,0.1827,0.1984,0.5398,1.1586,
      1.8453,2.5460,3.2519,4.0668,4.7969,5.5314,6.2650]
I4 = [b*1e-3 for b in I4]

plt.ylabel('I/A')
plt.xlabel('U/V')
plt.plot(V4,I4,'*')
plt.plot(V4,I4,'-.',label='diode')
plt.title('Alternating currency ')
legend(loc='upper left',fontsize='small')

