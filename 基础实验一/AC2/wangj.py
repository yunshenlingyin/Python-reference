# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:56:19 2019

@author: LGF
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy import *  # 这个包也需要导入，后面的polyval在这个包里面
import numpy as np
import matplotlib.pyplot as plt

ta=np.linspace(0,990,34)
Ta=[32.5,32.5,32.4,32.3,32.3,32.2,32.1,32.1,32.0,32.0,31.9,31.8,31.8,31.7,27.9,
    20.7,19.4,18.3,18.4,18.5,18.5,18.5,18.6,18.6,18.7,18.7,18.7,18.7,18.8,18.8,
    18.8,18.9,19.0,19.0]

plt.figure(dpi=300)
#上一行说明画图的像素是300,没有这一行输出的像素是默认的，默认的像素比较小
plt.scatter(ta, Ta,label='Measured data points')
plt.plot(ta, Ta, )

Y = np.polyfit(ta, Ta, 3)
# Y是一个4*1的矩阵，从左到右依次是x的三次、二次、一次、零次的系数
xx = np.linspace(0,990,1000)
#上一行是从0到990等间距的取1000个点
plt.plot(xx, polyval(Y,xx), label = '3th order polynomial fit')
plt.xlabel('Time/s', fontsize=18)
plt.ylabel('Temperature/$^\circ$C', fontsize=18)
# 特殊符号如摄氏度、sigma，theta等等怎么输出，详细见下方网站
#https://matplotlib.org/users/mathtext.html
plt.plot()
plt.legend(loc='upper right',fontsize = 'small'  )
#上一行是告诉电脑前面的两个label放在右上方，字号小，没有这一行，label就不显示
plt.show()

m1=(30.05+30.05+30.04)/3.
m01=(146.13+146.13+146.13)/3
mm01=(164.03)

m0=m01-m1
m=mm01-m01
print( 'm, m0, m1 =(mass of ice, mass of warm water, mass of container)= ',m, m0,
 m1)
C0=4.18;
C1=0.9;
t0=42.7
t1=36.2
L=(1/m)*(m0*C0+m1*C1)*(t0-t1)
print( 'L = ', L)
