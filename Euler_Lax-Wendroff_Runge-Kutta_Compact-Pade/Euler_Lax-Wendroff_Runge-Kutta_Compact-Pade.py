# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:02:34 2018

@author: Abdullah
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0,1.0,101)

dx = x[1]-x[0]
a = 1.0
c = 0.5
dt = c*dx / a

t = 1
itert = int(t/dt)


############## Exact ##############
Utrue = np.zeros((101,itert))

for j in range (itert):
    
    for i in range (x.size):
    
        Utrue[i,j] = np.sin(2*np.pi*(x[i]-a*dt*j))

##########  Euler Method ############

U = np.zeros((101,1))
U[:,0] = np.sin(2*np.pi*x)

for j in range (itert-1):
    
    Uc = np.zeros((101,1))
    Uc[0,0] = U[-1,j]
    
    for i in range (x.size-1):
        
        Uc[i+1,0] = U[i+1,j] - c*(U[i+1,j]-U[i,j])
        Utrue[i,j] = np.sin(2*np.pi*(x[i]-a*dt*j))
        
    U = np.hstack((U,Uc))
    

plt.figure()    
plt.plot(U[:,itert-1])
plt.plot(Utrue[:,itert-1])
plt.gca().legend(('t='+str(t),'Exact'))
        
############# Lax-Wendroff #######################
    
V = np.zeros((101,1))
V[:,0] = np.sin(2*np.pi*x)
V[-1,0] = V[0,0]
V = np.vstack((V[-2,0],V))


for j in range (itert-1):
    
    Vc = np.zeros((102,1))
    
    
    
    
    for i in range (x.size-1):
        
        Vc[i+1,0] = V[i+1,j] - (c/2)*(V[i+2,j]-V[i,j]) + (c**2/2)*(V[i+2,j]-2*V[i+1,j]+V[i,j])
        
    Vc[-1,0] = Vc[1,0]   
    Vc[0,0] = V[-2,j]
    V = np.hstack((V,Vc))
    
        
        
plt.figure()    
plt.plot(V[1:-1,itert-1])
plt.plot(Utrue[:,itert-1])     
plt.gca().legend(('t='+str(t),'Exact'))


################## RK3 #####################

R = np.zeros((101,1))
R[:,0] = np.sin(2*np.pi*x)
R = np.vstack((R[-2,0],R))

for j in range (itert-1):
    
    Rc = np.zeros((102,1))
    Rc1 = np.zeros((102,1))
    Rc2 = np.zeros((102,1))
    
    
    
    
    
    for i in range (x.size-1):
        Rc1[i,0] = R[i+1,j] - (c/2)*(R[i+1,j]-R[i-2,j])
    Rc1[-1,0] = Rc1[0,0]
    
    for i in range (x.size-1):
        Rc2[i,0] = (3/4)*R[i+1,j] + (1/4)*Rc1[i+1,0] - (c/8)*(Rc1[i+1,0]-Rc1[i-2,0])
    Rc2[-1,0] = Rc2[0,0]
    
    for i in range (x.size-1):
        Rc[i+1,0] = (1/3)*R[i+1,j] + (2/3)*Rc2[i,0] - (c/3)*(Rc2[i+1,0]-Rc2[i-1,0])
        
    
        
    Rc[-1,0] = Rc[1,0]
    Rc[0,0] = Rc[-2,0]
    R = np.hstack((R,Rc))
    
#=================================================================   

plt.figure()    
plt.plot(R[1:-1,itert-1])
plt.plot(Utrue[:,itert-1])     
plt.gca().legend(('t='+str(t),'Exact'))

