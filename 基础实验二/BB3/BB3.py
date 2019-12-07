# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
# V = 19.0
# r = 110
# # 橡胶的参数
# F1 = 0.85*0.09**2
# qc1 = V**2/2/F1/r
# R = 0.010
# delta_t1 = 5.2
# rho1 = 1374
# velocity1 = 2.3/3/60
# lambda1 = qc1*R/2/delta_t1
# ll = (40.197892-36.9987)/(678/1.95)
# c1 = qc1/rho1/velocity1/R
# print(qc1, lambda1, c1)
# # 有机玻璃的参数
# F2 = 0.85*0.09**2
# qc2 = V**2/2/F2/r
# R = 0.010
# delta_t2 = 7.35
# rho2 = 1196
# velocity2 = 0.029/0.04/1/60
# lambda2 = qc1*R/2/delta_t2
# c2 = qc2/rho2/velocity2/R
# print(qc2, lambda2, c2)
# t1 = np.arange(0, 8, 1)
# T2 = np.array([33.2, 33.3, 33.6, 34.2, 35.0, 35.7, 36.5, 37.3])
# delta_t1 = np.array([0.7, 6.7, 7.6, 8.0, 8.1, 8.1, 8.1, 8.1])
# fig1 = plt.figure(dpi=250)
# plt.xlabel("时间/min")
# plt.ylabel("温度/$^{\circ} C$")
# plt.plot(t1, T2, label="加热端的温度")
# plt.ylim(delta_t1.min()-1, T2.max()+3)
# plt.plot(t1, delta_t1, label="温度差")
# plt.legend(loc="up left", fontsize="small")
# plt.title("橡胶的温度曲线")
t1 = np.arange(0.0, 16.0, 1.0)
t1 = np.append(t1, np.arange(0.0, 6.0, 1.0)+0.5)
t1.sort()
T2 = np.array([25.6, 25.7, 25.7, 25.7, 25.9, 26.1, 26.5, 26.8, 27.2, 27.6, 27.9, 28.3, 28.8,
               29.7, 30.4, 31.3, 32.1, 33.0, 33.9, 34.8, 35.7, 36.7])
delta_t1 = np.array([1.6, 4.5, 5.3, 6.0, 6.6, 7.0, 7.2, 7.5, 7.6, 7.8, 7.9, 8.0, 8.0, 8.1, 8.1,
                     8.2, 8.2, 8.3, 8.3, 8.3, 8.4, 8.4])
fig1 = plt.figure(dpi=250)
plt.xlabel("时间/min")
plt.ylabel("温度/$^{\circ} C$")
plt.plot(t1, T2, label="加热端的温度")
plt.ylim(delta_t1.min()-1, T2.max()+3)
plt.plot(t1, delta_t1, label="温度差")
plt.legend(loc="upper left", fontsize="small")
plt.title("有机玻璃的温度曲线")

