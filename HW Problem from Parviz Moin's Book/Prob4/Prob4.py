# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:16:26 2018

@author: Abdullah
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

U1 = 1.0
U2 = 0.5
f20 = (U1+U2)/2*U1

eta = np.linspace(0.0,10.0,num=1001)
f01 = np.array([0.0,f20,0.0])
f02 = np.array([0.0,f20,0.1])

tol = 1e-6
dev = 1


def ODEs(ic,deta):
    
    f1 = ic[0]
    f2 = ic[1]
    f3 = ic[2]
        
    df1dt = f2
    df2dt = f3
    df3dt = -f1*f3
    
    out = [df1dt,df2dt,df3dt]
        
    return out

numI = 0

while abs(dev) > tol:
    
    numI = numI + 1
    
    F1 = odeint(ODEs, f01, eta)
    F2 = odeint(ODEs, f02, eta)
    dev = F2[-1,0]-F1[-1,0]
    #print(dev)
    f30new = f02[2] + (1-F2[-1,0]) * (f02[2]-f01[2]) / (F2[-1,0]-F1[-1,0])
 
    f01[2] = f02[2] 
    f02[2] = f30new
    
   
f1 = plt.figure()
plt.plot(eta,F2[:,0],':',label='f') 
#plt.plot(eta,F2[:,0],'--',label='fd') 
#plt.plot(eta,F2[:,0],label='fdd') 
plt.legend(loc='upper right')
plt.xlabel('$\eta$')
plt.xlim(0, 6)
plt.ylim(0, 2)
plt.show()


