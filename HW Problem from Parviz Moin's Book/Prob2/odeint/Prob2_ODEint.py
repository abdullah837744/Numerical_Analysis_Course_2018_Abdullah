# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 00:30:00 2018

@author: Abdullah
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

time = np.linspace(0.0,25.0,num=1001)
xyz0 = np.array([1,1,1])


def ODEs(xyz,t):
    sigma = 10
    b = 8/3
    r = 20
    
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
        
    dxdt = sigma*(y-x)
    dydt = r*x - y - x*z
    dzdt = x*y - b*z
    
    out = [dxdt,dydt,dzdt]
        
    return out

sol = odeint(ODEs, xyz0, time)

xval = sol[:,0]
yval = sol[:,1]
zval = sol[:,2]

f1 = plt.figure()
plt.plot(xval,yval,'b-') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('XY plane')
plt.savefig('XY plane.png')

f2 = plt.figure()
plt.plot(xval,zval,'b-') 
plt.xlabel('x')
plt.ylabel('z')
plt.title('XZ plane')
plt.savefig('XZ plane.png')

f3 = plt.figure()
plt.plot(yval,zval,'b-') 
plt.xlabel('y')
plt.ylabel('z')
plt.title('YZ plane')
plt.savefig('YZ plane.png')

    
    
        