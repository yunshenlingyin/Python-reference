# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 08:10:14 2019

@author: LGF
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def worfchaserabbit(w, t, v1, v2, L):
    # 给出位置矢量w，单位均为国际单位 
    # dx/dt, dy/dt, dz/dt的值
    x, y = w
    # worfchaserabbi直接与的计算公式对应
    return np.array([v2*(v1*t-x)/((((v1*t-x)**2+(L-y)**2))**0.5),
                     v2*(L-y)/((((v1*t-x)**2+(L-y)**2))**0.5)])

t = np.arange(0, 5, 0.001) # 创建时间点
# 调用ode对worfchaserabbi进行求解
track1 = odeint(worfchaserabbit, (0.0, 0.0), t, args=(21.0, 30.0, 103.0))

# 绘图
fig = plt.figure(dpi=250)
x = track1[:, 0]
y = track1[:, 1]
plt.plot(x,y)
plt.show()






"""
# 方法二

# -*- coding: utf-8 -*-
"""
#Created on Sun Mar 10 08:04:37 2019

#@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x0 = 0.; y0 = 0.; X0 = 0.; Y0 = 103.; v_x0 = 0.; v_y0 = 30.;  v1 = 21.;
dt = 0.01;
n =500


x y为狼的位置坐标， v_x，v_y 分别是狼的两个速度分量， X Y 是兔子相对于狼的位移的两个分量，
v1 是兔子的速度
单位均为国际单位

x = zeros((n,1),float)
y = zeros((n,1),float)
X = zeros((n,1),float)
Y = zeros((n,1),float)
v_x = zeros((n,1),float)
v_y = zeros((n,1),float)

for i in range(n):
    x[i] = x[i-1] + v_x[i-1]*dt
    y[i] = y[i-1] + v_y[i-1]*dt

    X[i] = 21*i*dt - x[i-1]
    Y[i] = 103 - y[i-1]
    v_x[i] = (30*(X[i]))/((X[i]**2 + Y[i]**2)**0.5)
    v_y[i] = (30*(Y[i]))/((X[i]**2 + Y[i]**2)**0.5)





ylabel('y/m')
xlabel('x/m')
plot(x,y)
show()
"""








