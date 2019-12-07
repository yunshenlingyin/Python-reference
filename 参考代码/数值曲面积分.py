# -*- coding:utf-8 -*-
"""
x=[1:0.1:10];
y=[1:0.1:10];
[x1,y1]=meshgrid(x,y);
z1=2*x1+y1;
z1(z1>10)=nan;
mesh(x1,y1,z1)
dx = x1(1,2)-x1(1,1);
dy = y1(2,1)-y1(1,1);
Fx = diff(z1,1,2)/ dx;
Fy = diff(z1,1,1)/ dy;
S=sqrt(1+Fx(2:end,:).^2+Fy(:,2:end).^2)*dx*dy.*( ~isnan(z1(2:end,2:end))) ;
sum(S(~isnan(S)))
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dx = 0.01
dy = 0.01
x = np.arange(0, 10+dx, dx)
y = np.arange(0, 10+dy, dy)
x, y = np.meshgrid(x, y)
z = 2 * x + y
z[z > 10] = np.nan
Fx = np.diff(z, axis=1)/dx
Fy = np.diff(z, axis=0)/dy
s = np.sqrt(1 + Fx[1:, :]**2 + Fy[:, 1:]**2)*dx*dy*(~np.isnan(z)[1:, 1:])
S = np.sum(s[~np.isnan(z)[1:, 1:]])
print(S)
fig = plt.figure(dpi=250)
ax1 = plt.axes(projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.plot_surface(x, y, z, cmap='rainbow')
plt.show()

