# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:07:22 2019

@author: LGF
"""
from scipy import *
import numpy as np

import datetime
starttime = datetime.datetime.now()
#long running
#do something other
endtime = datetime.datetime.now()
print (endtime - starttime)
"""
x = np.array([0.0,500.0,1000.0,1500.0,2000.0,2500.0,3000.0,3500.0])*1e-6
x1 = np.ones(8)
y = np.array([0.28,0.41,0.54,0.65,0.77,0.87,0.99,1.10])
P = np.diag([1,1,1,1,1,1,1,1])
A = np.stack((x,x1))
A = A.T
C = np.linalg.inv(A.T.dot(A))
X1 = C.dot(A.T).dot(y)
sigmax = np.std(x)**2*len(x)/(len(x))
X2 = C*sigmax
print(X1,X2)
"""
D_outer = np.array([0.087,0.083,0.085,0.082,0.082])

#33,33,33.02,33.04,33.00
D1_std = np.std(D_outer)
D1_mean = np.mean(D_outer)
D_inside = np.array([34.02,34.04,34,34.04,34.02])
D2_std = np.std(D_inside)
D2_mean = np.mean(D_inside)
C1 = np.array([0.7,0.7,0.68,0.69])
C1mean = np.mean(C1)
C1mean1 = C1*0.0197/(np.pi*(0.03402+0.033))
