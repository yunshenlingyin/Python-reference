# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:15:08 2019

@author: LGF
"""
from scipy import *
from matplotlib.pylab import *
a = 1.5*1e-5
a1 = 2.8*1e-6
a2 = 11.7*1e-6
a3 = 8.7*1e-6
v = a**4/(a1**4/9+a2**4/8+a3**4/50)
print(v)
