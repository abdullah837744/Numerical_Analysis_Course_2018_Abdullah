# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:37:46 2018

@author: Abdullah
"""

import numpy as np
import matplotlib.pyplot as plt

############# Exact Solutio ################
def fun(x):
    out = 4*np.exp(-2*x - (0.01/3)*x**2)
    return out

x_true = np.linspace(0,15,151)
y_true = fun(x_true)

#############################################
begin = 0.0
end = 15.0
y0 = 4.0
#############################################
###### Forward Euler ########################
def Euler(dx,start,final,ic):

    y = np.zeros((round(final/dx+1),1))
    x = np.zeros((round(final/dx+1),1))

    y[0,0]= ic

    i = 0
    while i < np.size(y,0)-1:
        y[i+1,0] = y[i,0] + dx*(-(2+0.01*x[i,0]**2))*y[i,0]
        x[i+1,0] = x[i,0]+dx
        i = i + 1
    return x, y
#########################
  
Ex1,Ey1 = Euler(0.1,begin,end,y0)
Ex2,Ey2 = Euler(0.5,begin,end,y0)
Ex3,Ey3 = Euler(1.0,begin,end,y0)
  
f1 = plt.figure()
plt.plot(x_true,y_true,'b')
plt.plot(Ex1,Ey1,'m*-')
plt.plot(Ex2,Ey2,'ko-')
plt.plot(Ex3,Ey3,'rp-')
plt.gca().legend(('Exact','Euler,dx=0.1','Euler,dx=0.5','Euler,dx=1.0'))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.ylim(-1, 5)
plt.title('Forward Euler')
plt.savefig('Forward Euler.png')
plt.show()
  
########################################
######### Backward Euler ###############
def BEuler(dx,start,final,ic):

    y = np.zeros((round(final/dx+1),1))
    x = np.zeros((round(final/dx+1),1))

    y[0,0]= ic

    i = 0
    while i < np.size(y,0)-1:
        y[i+1,0] = y[i,0] / (1+ dx*(2+0.01*x[i,0]**2))
        x[i+1,0] = x[i,0]+dx
        i = i + 1
    return x, y
#########################
  
BEx1,BEy1 = BEuler(0.1,begin,end,y0)
BEx2,BEy2 = BEuler(0.5,begin,end,y0)
BEx3,BEy3 = BEuler(1.0,begin,end,y0)

  
f2 = plt.figure()
plt.plot(x_true,y_true,'b')
plt.plot(BEx1,BEy1,'m*-')
plt.plot(BEx2,BEy2,'ko-')
plt.plot(BEx3,BEy3,'rp-')
plt.gca().legend(('Exact','BEuler,dx=0.1','BEuler,dx=0.5','BEuler,dx=1.0'))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.ylim(-1, 5)
plt.title('Backward Euler')
plt.savefig('Backward Euler.png')
plt.show()   

############################################
############# Trapezoidal #################
def Trapezoid(dx,start,final,ic):

    y = np.zeros((round(final/dx+1),1))
    x = np.zeros((round(final/dx+1),1))

    y[0,0]= ic

    i = 0
    while i < np.size(y,0)-1:
        y[i+1,0] = y[i,0] * ( (1+(-(2+0.01*x[i,0]**2))/2) / (1-(-(2+0.01*x[i,0]**2))/2) )
        x[i+1,0] = x[i,0]+dx
        i = i + 1
    return x, y
#########################
  
Tx1,Ty1 = Trapezoid(0.1,begin,end,y0)
Tx2,Ty2 = Trapezoid(0.5,begin,end,y0)
Tx3,Ty3 = Trapezoid(1.0,begin,end,y0)
  
f3 = plt.figure()
plt.plot(x_true,y_true,'b')
plt.plot(Tx1,Ty1,'m*-')
plt.plot(Tx2,Ty2,'ko-')
plt.plot(Tx3,Ty3,'rp-')
plt.gca().legend(('Exact','Trapezoid,dx=0.1','Trapezoid,dx=0.5','Trapezoid,dx=1.0'))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.ylim(-1, 5)
plt.title('Trapezoidal')
plt.savefig('Trapezoidal.png')
plt.show()


############################################
########### RK-2 ########################
def RK2(dx,start,final,ic):

    y = np.zeros((round(final/dx+1),1))
    x = np.zeros((round(final/dx+1),1))

    y[0,0]= ic

    i = 0
    while i < np.size(y,0)-1:
        yp = y[i,0] + (dx/2)*(-(2+0.01*x[i,0]**2)*y[i,0])
        y[i+1,0] = y[i,0] + dx*(-(2+0.01*(x[i,0]/2)**2)*yp)
        x[i+1,0] = x[i,0]+dx
        i = i + 1
    return x, y
#########################
  
RK2x1,RK2y1 = RK2(0.1,begin,end,y0)
RK2x2,RK2y2 = RK2(0.5,begin,end,y0)
RK2x3,RK2y3 = RK2(1.0,begin,end,y0)
  
f4 = plt.figure()
plt.plot(x_true,y_true,'b')
plt.plot(RK2x1,RK2y1,'m*-')
plt.plot(RK2x2,RK2y2,'ko-')
plt.plot(RK2x3,RK2y3,'rp-')
plt.gca().legend(('Exact','RK2,dx=0.1','RK2,dx=0.5','RK2,dx=1.0'))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.ylim(-1, 5)
plt.title('RK-2')
plt.savefig('RK-2.png')
plt.show()

###############################################################
########### RK-4 ########################
def RK4(dx,start,final,ic):

    y = np.zeros((round(final/dx+1),1))
    x = np.zeros((round(final/dx+1),1))

    y[0,0]= ic
    

    i = 0
    while i < np.size(y,0)-1:
        
        k1 = dx*(-(2+0.01*x[i,0]**2)*y[i,0])
        k2 = dx*(-(2+0.01*(x[i,0]+dx/2)**2)*(y[i,0]+k1/2))
        k3 = dx*(-(2+0.01*(x[i,0]+dx/2)**2)*(y[i,0]+k2/2))
        k4 = dx*(-(2+0.01*(x[i,0]+dx)**2)*(y[i,0]+k3))
        
        y[i+1,0] = y[i,0] + k1/6 + (k2+k3)/3 + k4/6
        
        x[i+1,0] = x[i,0]+dx
        i = i + 1
    return x, y
#########################
  
RK4x1,RK4y1 = RK4(0.1,begin,end,y0)
RK4x2,RK4y2 = RK4(0.5,begin,end,y0)
RK4x3,RK4y3 = RK4(1.0,begin,end,y0)
  
f5 = plt.figure()
plt.plot(x_true,y_true,'b')
plt.plot(RK4x1,RK4y1,'m*-')
plt.plot(RK4x2,RK4y2,'ko-')
plt.plot(RK4x3,RK4y3,'rp-')
plt.gca().legend(('Exact','RK4,dx=0.1','RK4,dx=0.5','RK4,dx=1.0'))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.ylim(-1, 5)
plt.title('RK-4')
plt.savefig('RK-4.png')
plt.show()
