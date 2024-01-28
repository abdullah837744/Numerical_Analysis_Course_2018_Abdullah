# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:54:33 2018

@author: Abdullah
"""

# Blasius Equation:  fddd + f*fdd = 0
# let, f1 = f ; f2 = fd and f3 = fdd
# So we get, f1d = f2; f2d = f3 and f3d = -f*fdd
# Condition given: f(0)=0, fd(0)=0 and fd(inf)=1
# So we get, f1(0)=0, f2(0)=0 and f2(inf)=1
# So f3(0) needs to be guessed.



import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


eta = np.linspace(0.0,10.0,num=1001)
f01 = np.array([0.0,0.0,0.0])
f02 = np.array([0.0,0.0,0.1])

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

while dev > tol:
    
    numI = numI + 1
    
    F1 = odeint(ODEs, f01, eta)
    F2 = odeint(ODEs, f02, eta)
    dev = F2[-1,1]-F1[-1,1]
    #print(dev)
    f30new = f02[2] + (1-F2[-1,1]) * (f02[2]-f01[2]) / (F2[-1,1]-F1[-1,1])
 
    f01[2] = f02[2] 
    f02[2] = f30new
    
   
f1 = plt.figure()
plt.plot(eta,F2[:,0],':',label='f') 
plt.plot(eta,F2[:,1],'--',label='fd') 
plt.plot(eta,F2[:,2],label='fdd') 
plt.legend(loc='upper right')
plt.xlabel('$\eta$')
plt.xlim(0, 6)
plt.ylim(0, 2)
plt.savefig('Blasius.png')
plt.show()