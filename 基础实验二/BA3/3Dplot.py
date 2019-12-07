# -*- coding: utf-8 -*-
"""
@author: GXF
"""
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# x = np.linspace(0.0, 0.3, 7)
x = np.array([0,0.01,0.1,1.0,2.0,-8.0,9.0])
y = 5 * np.linspace(0.0, 0.3, 7)
X, Y = np.meshgrid(x, y)
Z = np.array([[1.038,1.038,1.038,1.037,1.036,1.034,1.03],\
              [1.038,1.038,1.037,1.037,1.036,1.034,1.031],\
              [1.037,1.037,1.038,1.038,1.038,1.036,1.033],\
              [1.036,1.036,1.036,1.036,1.036,1.036,1.033],\
              [1.035,1.035,1.037,1.038,1.038,1.039,1.037],\
              [1.033,1.034,1.036,1.039,1.042,1.043,1.044],\
              [1.031,1.032,1.035,1.038,1.043,1.047,1.05]])


fig = plt.figure()
ax3 = plt.axes(projection='3d')
ax3.set_xlabel("x/mm")
ax3.set_ylabel("y/mm")
ax3.set_zlabel("z/Gs")
ax3.plot_surface(X,Y,Z,cmap='rainbow')
ax3.grid()
plt.show()
