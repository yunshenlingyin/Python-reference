# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:46:16 2019

@author: LGF
"""
import numpy as np
import matplotlib.pyplot as plt

n = 100
f = np.zeros(n)
x = np.arange(n)

# initial conditions
width = 10.
f0 = np.exp(-(x-25.)**2/width**2)   # put in a top hat initially

f = np.copy(f0)
fp = np.copy(f)
fnew = np.copy(f)

# alpha = vdt/dx
alpha = 0.5

# number of iterations
niter = int(0.5 * n / alpha)

# set up plots and plot the starting profile
plt.ion()
dat, = plt.plot(x, f)
plt.ylim((-0.5,1.5))
plt.show()

for k in range(niter):

    # lax
    #fnew = 0.5 * (np.roll(f,1) + np.roll(f,-1)) - 0.5 * alpha * (np.roll(f,-1) - np.roll(f,1))

    # leapfrog
    fnew = fp - alpha * (np.roll(f,-1) - np.roll(f,1))
    
    # draw the updated data
    dat.set_ydata(fnew) 
    plt.draw()
    plt.pause(0.1)

    fp[:] = f[:] 
    f[:] = fnew[:]

plt.ioff()
plt.close()
plt.plot(x,f)
plt.plot(x,np.exp(-(x-75)**2/width**2),'r:')
plt.ylim((-0.5,1.5))
plt.show()