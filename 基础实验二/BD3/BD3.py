# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:13:09 2019

@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#解决中文显示的问题，SimSun是宋体，下一行解决的是显示负号的问题，改成‘True’，不显示
#坐标轴上的负号
plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['axes.unicode_minus'] = False


#截止电压的测量，计算普朗克常量
# x 是频率(1/s)，y是电压(V)。
x = 1e9*299792458/np.array([365,405,436,546,577])
y = np.array([1.83,1.36,1.15,0.58,0.50])
y01 = np.polyfit(x,y,1)
y01 = np.poly1d(y01)
xx = np.linspace(min(x),max(x))
fig1,ax1 = plt.subplots(dpi=250)
ax1.set_xlabel('频率/Hz')
ax1.set_ylabel('电压/V')
ax1.plot(x,y,'*',label = '实验数据')
ax1.plot(xx,np.polyval(y01,xx),label=str(y01))
ax1.legend(loc = 'upper left',fontsize = 'small')
ax1.set_title('计算普朗克常量')
plt.show()
plt.savefig('普朗克常量')
#伏安特性曲线，x是电压(V)，y是电流(A)。
#365nm
x1 = np.array([-1.83,5.05,10.13,15.73,20.24,25.42,30.10,30.61])
y1 = np.array([0,44,79,116,138,159,175,176])*1e-10
#405nm
x2 = np.array([-1.36,5.08,10.48,15.17,20.23,25.19,29.06,30.21])
y2 = np.array([0,11,24,32,39,45,47,48])*1e-10
#436nm
x3 = np.array([-1.20,5.09,10.10,15.28,20.25,25.44,30.00,30.62])
y3 = np.array([0,15,32,45,52,58,61,62])*1e-10
#546nm
x4 = np.array([-0.58,5.00,10.26,15.43,20.78,25.29,30.02,30.62])
y4 = np.array([0,4,11,13,14,14,16,16])*1e-10
#577nm
x5 = np.array([-0.50,5.13,10.80,15.08,20.39,25.76,29.46,30.36])
y5 = np.array([0,1,4,5,5,5,5,6])*1e-10
fig2,ax2 = plt.subplots(dpi=250)
ax2.set_xlabel('电压/V')
ax2.set_ylabel('电流/A')
ax2.plot(x1,y1,'*')
ax2.plot(x1,y1,label='365nm')
ax2.plot(x2,y2,'*')
ax2.plot(x2,y2,label='405nm')
ax2.plot(x3,y3,'*')
ax2.plot(x3,y3,label='436nm')
ax2.plot(x4,y4,'*')
ax2.plot(x4,y4,label='546nm')
ax2.plot(x5,y5,'*')
ax2.plot(x5,y5,label='577nm')
ax2.legend(fontsize='small')
ax2.set_title('伏安特性曲线')
plt.show()
plt.savefig('伏安特性曲线')
# I-P的关系，phi是光栅的口径，单位是mm,I1是电流大小,单位是A
phi = np.array([2,4,8])
I1 = np.array([35,140,461])
fig3,ax3 = plt.subplots(dpi=250)
ax3.set_xlabel('光阑口径/mm')
ax3.set_ylabel(r'电流$/10^{-10}A$')
ax3.plot(phi,I1,'*',label = '实验数据')
ax3.plot(phi,I1)
ax3.legend(fontsize='small')
ax3.set_title('口径-光电流的关系')
plt.show()
plt.savefig('口径-光电流的关系')
# I -P的关系，L是距离(mm),I2(A)是电流大小
L = np.array([300,350,400])
I2 = np.array([339,228,165])
fig4,ax4 = plt.subplots(dpi=250)
ax4.set_xlabel('距离/mm')
ax4.set_ylabel(r'电流$/10^{-10}A$')
ax4.plot(L,I2,'*',label='实验数据')
ax4.plot(L,I2)
ax4.legend(fontsize='small')
ax4.set_title('距离-光电流的关系')
plt.show()
plt.savefig('距离-光电流的关系')

