# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:00:27 2018

@author: Asha
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

method = 1  # 1 for shooting method and 2 for direct method

if method==1:

    TA = 5.0
    TB = 4.0
    xaxis = np.linspace(0.0,2.0,num=1001)
    T01 = np.array([TA,0.1])
    T02 = np.array([TA,0.5])
    
    
    tol = 1e-6
    dev = 1
    
    
    def ODEs(ic,x):
        
        a = - (x+3)/(x+1)
        b = x+3 / (x+1)**2
        f = 2*(x+1) + 3*b
        
        T1 = ic[0]
        T2 = ic[1]
            
        dT1dt = T2
        dT2dt = f - a*T2 - b*T1
    
        
        out = [dT1dt,dT2dt]
            
        return out
    
    numI = 0
    
    while dev > tol:
        
        numI = numI + 1
        
        TL1 = odeint(ODEs, T01, xaxis)
        TL2 = odeint(ODEs, T02, xaxis)
        dev = abs(TL2[-1,0]-TB)
        #print(TL2)
        T30new = T02[1] + (TB-TL2[-1,0]) * (T02[1]-T01[1]) / (TL2[-1,0]-TL1[-1,0])
     
        T01[1] = T02[1] 
        T02[1] = T30new
        
    

       
    f1 = plt.figure()
    plt.plot(xaxis,TL2[:,0],label='T') 
    #plt.plot(xaxis,TL2[:,1],'--',label='Td') 
    plt.legend(loc='upper right')
    plt.xlabel('x')
    #plt.xlim(0, 6)
    #plt.ylim(0, 2)
    plt.title('Shooting Method')
    plt.savefig('Prob5 Shooting.png')
    plt.show()
    
    print(TL2)
    
    
elif method==2:
    
    x = np.linspace(0.0,2.0,num=1001)
    h = x[1]-x[0]
    T0 = 5
    TL = 4
    grid = x.size - 2
    
    a = - (x+3)/(x+1)
    ac = a[1:-1]
    b = x+3 / (x+1)**2
    bc = b[1:-1]
    f = 2*(x+1) + 3*b
    fc = f[1:-1]
    
#    coeff = np.zeros((grid,grid))
    T = np.zeros(grid)
    
    alpha = 1/h**2 + ac/2*h
    beta = bc - 2/h**2
    gama = 1/h**2 - ac/2*h
    
    fc[0] = fc[0] - gama[0]*T0
    fc[-1]= fc[-1] - alpha[-1]*TL
    
    
#    for j in range(grid):
#        
#        coeff[j,j] = beta[j]
#        
#        if j<= grid-2:
#            coeff[j+1,j] = gama[j+1]
#            coeff[j,j+1] = alpha[j]
            
    
    ######################################
    for i in range(grid):
        if i==0:
             alpha[i] = alpha[i]/beta[i]
             fc[i] = fc[i] / beta[i]
        elif i>0 & i<= grid-2:
            alpha[i] = alpha[i] / (beta[i]-(gama[i]*alpha[i-1]))
            fc[i] = (fc[i]-(gama[i]*fc[i-1])) / (beta[i]-(gama[i]*alpha[i-1]))
        else:
            fc[i] = (fc[i]-(gama[i]*fc[i-1])) / (beta[i]-(gama[i]*alpha[i-1]))
            
            
    T[-1]= fc[-1]        
    for k in range(grid,1,-1):
        
        T[k-2] = fc[k-2] - alpha[k-2]*T[k-1]
        
    f1 = plt.figure()
    plt.plot(x[1:-1],T[:],label='T')  
    plt.legend(loc='upper right')
    plt.xlabel('x')
    plt.title('Direct Method')
    #plt.xlim(0, 6)
    #plt.ylim(0, 2)
    plt.savefig('Prob5 Direct.png')
    plt.show()
    
    
        
        

        
        
    #################################################
            
        
    
    
    