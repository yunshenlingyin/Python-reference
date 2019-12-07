# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:09:03 2019

@author: LGF
"""
from scipy import *
import numpy as np 
delta_s = 7*1e-2
L = 2.52
theta = delta_s/(4*L)
omega = 0.0128
b = 0.0427
r = 0.00818
d = 0.1
M = 1.5
G = theta*omega**2*b**2*(0.8*r**2+0.5*d**2)/(M*d)
print(G)