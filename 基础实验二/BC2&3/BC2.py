# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 06:37:59 2019

@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt

#平行光法测量透镜的焦距


#正面

#a1 = np.array([86.6,80.5,91.8,90.4,88.2])#单位：cm  透镜位置
#b1 = np.array([110.4,105.0,115.0,115.9,114.2])#单位：cm   白屏位置
#f1 = b1-a1 #简单测量焦距
#f1_modify = 1/(1/a1+1/(b1-a1))#修正后的焦距
#
#print(f1,f1_modify,"\n",np.mean(f1),np.mean(f1_modify))
#
##反面
#
#a2 = np.array([90.8,89.2,88.5,94.9,93.1])#单位：cm  透镜位置
#b2 = np.array([114.2,112.5,111.7,118.1,116.2])#单位：cm   白屏位置
#f2 = b2-a2
#f2_modify = 1/(1/a2+1/(b2-a2))
#print(f2,f2_modify,"\n",np.mean(f2),np.mean(f2_modify))


#自准直法测会聚透镜的焦距

#正面
#
#a3 = np.array([28.8,22.9,29.2,41.2,30.8])#单位：cm  透镜位置
#b3 = np.array([47.6,41.8,48.0,59.6,50.4])#单位：cm   白屏位置
#f3 = b3-a3
##print(f3,f3.mean(),f3.var())
#
##反面
#
#a4 = np.array([32.1,38.1,41.9,31.4,40.4])#单位：cm  透镜位置
#b4 = np.array([51.0,55.0,60.0,50.0,60.9])#单位：cm   白屏位置
#f4 = b4-a4
#print(f4,f4.mean(),f4.var())
#f41 = np.append(f3,f4,axis=0)
#print(f41.mean(),f41.var())


#测透镜组的焦距

#正面

a5 = np.array([63.5,65.8,70.8,77.4,83.0])
b5 = np.array([74.8,77.3,82.2,89.2,94.5]) 
f5 = b5-a5
print(f5,"\n",f5.mean())

#反面

a6 = np.array([70.5,64.4,61.1,80.6,87.9])
b6 = np.array([81.8,76.0,72.6,92.0,99.3])
f6 = b6-a6
fig = plt.plot(a6,b6)
plt.plot(a6,b6)
plt.show()
print(f6,"\n",f6.mean())
f61 = np.append(f5,f6,axis=0)
print(f61.var())







