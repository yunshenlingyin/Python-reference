# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:07:22 2019

@author: LGF
"""
from scipy import *
import numpy as np
from pylab import *
x = np.array([65,75,85,95,105])
x1 = np.ones(5)
y = np.array([-20,17,42,94,127])
P = np.diag([400,400,225,225,144])
A = np.stack((x,x1))
A = A.T
C = np.linalg.inv(A.T.dot(P).dot(A))
X1 = C.dot(A.T).dot(P).dot(y)
sigmax = np.std(x)**2*len(x)/(len(x))
X2 = C*sigmax
print(X1,X2,A.shape)