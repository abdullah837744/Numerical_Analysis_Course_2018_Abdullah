# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:17:54 2018

@author: Abdullah
"""

import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import Axes3D



def RK4x(x,y,sig,dt):
    
    
        
    k1 = dt*sig*(y-x)
    k2 = dt*sig*(y-(x+k1/2))
    k3 = dt*sig*(y-(x+k2/2))
    k4 = dt*sig*(y-(x+k3))
        
    x = x + k1/6 + (k2+k3)/3 + k4/6
   
    return x

def RK4y(x,y,z,r,dt):
    
        
    k1 = dt*(r*x - y - x*z) 
    k2 = dt*(r*x - (y+k1/2) - x*z)
    k3 = dt*(r*x - (y+k2/2) - x*z)
    k4 = dt*(r*x - (y+k3) - x*z)
        
    y = y + k1/6 + (k2+k3)/3 + k4/6    

    return y

def RK4z(x,y,z,b,dt):

        
    k1 = dt*(x*y - b*z)
    k2 = dt*(x*y - b*(z+k1/2))
    k3 = dt*(x*y - b*(z+k2/2))
    k4 = dt*(x*y - b*(z+k3))
        
    z = z + k1/6 + (k2+k3)/3 + k4/6

    return z


time = np.linspace(0.0,25.0,num=10001)
dt = time[1]-time[0]

sig = 10
b = 8/3
r = 28



#xx = np.zeros((np.size(time,0),1))
#xx[0]=1
#yy = np.zeros((np.size(time,0),1))
#yy[0]=1
#zz = np.zeros((np.size(time,0),1))
#zz[0]=1
#t = np.zeros((np.size(time,0),1))
#    
#    
#for i in range(10000):
#    
#    xx[i+1] = RK4x(xx[i],yy[i],sig,dt)
#    yy[i+1] = RK4y(xx[i],yy[i],zz[i],r,dt)
#    zz[i+1] = RK4z(xx[i],yy[i],zz[i],b,dt)
#    


##########################################

xx1 = np.zeros((np.size(time,0),1))
xx1[0]=6
yy1 = np.zeros((np.size(time,0),1))
yy1[0]=6
zz1 = np.zeros((np.size(time,0),1))
zz1[0]=6


xx2 = np.zeros((np.size(time,0),1))
xx2[0]=6
yy2 = np.zeros((np.size(time,0),1))
yy2[0]=6.01
zz2 = np.zeros((np.size(time,0),1))
zz2[0]=6


t = np.zeros((np.size(time,0),1))
    
    
for i in range(10000):
    
    xx1[i+1] = RK4x(xx1[i],yy1[i],sig,dt)
    yy1[i+1] = RK4y(xx1[i],yy1[i],zz1[i],r,dt)
    zz1[i+1] = RK4z(xx1[i],yy1[i],zz1[i],b,dt)
    
    xx2[i+1] = RK4x(xx2[i],yy2[i],sig,dt)
    yy2[i+1] = RK4y(xx2[i],yy2[i],zz2[i],r,dt)
    zz2[i+1] = RK4z(xx2[i],yy2[i],zz2[i],b,dt)
    
#    
#    
###########################################
f0 = plt.figure()
plt.plot(time,xx1,'b-') 
plt.plot(time,yy1,'r-') 
plt.xlabel('t')
plt.ylabel('x and y')
plt.title('X vs t and Y vs t')
plt.gca().legend(('X vs t','Y vs t'))
plt.savefig('Y vs t.png')
    
    

###########################################    
   
#f1 = plt.figure()
#plt.plot(xx,yy,'b-') 
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('XY plane')
#plt.savefig('XY plane.png')
#
#f2 = plt.figure()
#plt.plot(xx,zz,'b-') 
#plt.xlabel('x')
#plt.ylabel('z')
#plt.title('XZ plane')
#plt.savefig('XZ plane.png')
#
#f3 = plt.figure()
#plt.plot(yy,zz,'b-') 
#plt.xlabel('y')
#plt.ylabel('z')
#plt.title('YZ plane')
#plt.savefig('YZ plane.png')
#
#f4 = plt.figure()
#plt.plot(time,xx,'b-') 
#plt.xlabel('t')
#plt.ylabel('x')
#plt.title('X vs t')
#plt.savefig('X vs t.png')
#
#f5 = plt.figure()
#plt.plot(time,yy,'b-') 
#plt.xlabel('t')
#plt.ylabel('y')
#plt.title('Y vs t')
#plt.savefig('Y vs t.png')
#
#f6 = plt.figure()
#plt.plot(time,zz,'b-') 
#plt.xlabel('t')
#plt.ylabel('z')
#plt.title('Z vs t')
#plt.savefig('Z vs t.png')


### 3D plot #######
#fig = plt.figure()
#ax=fig.gca(projection='3d')
#ax.plot3D(xx[:,0], yy[:,0], zz[:,0])
#ax.set_xlabel('x',fontsize=20)
#ax.set_ylabel('y',fontsize=20)
#ax.set_zlabel('z',fontsize=20)
#plt.savefig('3Dplot.png')
#plt.show()


