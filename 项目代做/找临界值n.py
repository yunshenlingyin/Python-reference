# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:30:51 2019

@author: LGF
"""
import numpy as np
from scipy.special import comb 
import math
p = np.zeros(20)
q1= np.zeros(20)
q2= np.zeros(20)
for i in range(20):
    p[i]=comb(365,i+1)/(365**(i+1))*(math.factorial(i+1))
    #上面一行表示的是准确的概率公式
    q1[i]=1-(i+1)*i/730
    #上面一行是第一种近似
    q2[i]=np.exp(-(i+1)*i/730)
    #上面一行是第二种近似
delta1= np.abs(p-q1)#第一种近似和准确值的差值的绝对值
delta2=np.abs(p-q2)#第二种近似和准确值的差值的绝对值
for i in range(20):
    if delta1[i]<=delta2[i]:
        print(i+1,"较小，此时应该采用第一种近似方法")
    else:
        print(i+1,"较大，此时应该采用第二种近似方法")