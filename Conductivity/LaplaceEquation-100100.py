
# coding: utf-8

# In[ ]:

"""
Monte Carlo Simulation of nanostructured thin films

Author: Alejandro Cardenas-Avendano
email: alejandro.cardenasa@konradlorenz.edu.co
Website: https://github.com/alejandroc137
License: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""


# In[59]:

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import Image
import random
#%pylab inline


# In[2]:

si=100
image_data = np.array(Image.open("pelicula.JPG"))
r,g,b = image_data.T
iaux=image_data[:100,:100]
new=r[:si,:si].T
msize=new.shape


# In[3]:

mdim=msize[1]*msize[0]


# Porosity criteria. It has to be a number  $p$ such
# 
# $0<p<256$ 

# `simulated` is a matrix where I put the porosity from the image

# In[72]:

p=10
aux=0
simulated=np.ones(mdim).reshape(msize[0],msize[1])
for i in xrange(msize[1]):
    for j in xrange(msize[0]):
        if new[i,j]<p:
            simulated[i,j]=new[i,j]
            aux+=1
mp=np.zeros(shape=(aux,2))
aux1=0
for i in xrange(msize[1]):
    for j in xrange(msize[0]):
        if new[i,j]<p and new[i,j]!=1 :
            mp[aux1,0]=i
            mp[aux1,1]=j
            aux1+=1


# In[6]:




## Code to solve Laplace's Equation

# This code solves Laplaxe's Equations by an iterative simple method know as "Relaxation"

#  $\nabla^2 \varphi = 0$  $\qquad\mbox{or}\qquad \Delta\varphi = 0$

# Potential's values

# In[7]:

vmax=10
vmin=0


# Number of iterations allowed

# In[8]:

lp=10000


# Matrix to be relaxed 

# In[73]:

m=np.zeros(shape=(msize[1],msize[0]))
Vr=np.zeros(shape=(msize[1],msize[0]))
Vl=np.zeros(shape=(msize[1],msize[0]))
Vu=np.zeros(shape=(msize[1],msize[0]))
Vd=np.zeros(shape=(msize[1],msize[0]))
pr=np.zeros(shape=(msize[1],msize[0]))
pl=np.zeros(shape=(msize[1],msize[0]))
pu=np.zeros(shape=(msize[1],msize[0]))
pd=np.zeros(shape=(msize[1],msize[0]))


# Location of the electrodes

# In[10]:

yvmax=(2.5*msize[0]/10.)
yvmin=(7.5*msize[0]/10.)
xv=(msize[1]*(0.5))
m[xv,yvmax]=vmax
m[xv,yvmin]=vmin


# Visualization of the electrodes

# In[16]:
'''
plt.figure(figsize=(12,12))
plt.contour(m,50)
#plt.colorbar()
plt.show()



# Relaxation

# In[12]:

for r in xrange(lp):
    for x in xrange(1,msize[1]-1):
        for y in xrange(1,msize[0]-1):
            if not ((y==yvmax and x==xv) or (y==yvmin and x==xv)):
                m[x,y]=(m[x+1,y]+m[x-1,y]+m[x,y+1]+m[x,y-1])/4.
    for x in xrange(0,msize[1]):
        m[x,0]=m[x,1]
        m[x,msize[0]-1]=m[x,msize[0]-2]
    for y in xrange(0,msize[0]):
        m[0,y]=m[1,y]
        m[msize[1]-1,y]=m[msize[1]-2,y]


# In[ ]:

[px,py]=np.gradient(m)
X, Y = np.meshgrid(np.linspace(0,si-1,si), np.linspace(0,si-1,si))
figure(figsize=(12,6))
contour(m,100)
colorbar()
quiver(X,Y,-py,-px)

'''
# Now, we can see the result. It is expected to see nice equipotentials

# In this variable I stored the result of the relaxation proccess since it is computational heavy

# In[52]:

import pickle
'''
f = open('store100100.pckl', 'w')
pickle.dump(m, f)
f.close()
'''
f = open('store100100.pckl')
m = pickle.load(f)
f.close()
#'''


# In[53]:

for i in xrange(aux):
    if not((mp[i,0]==xv and mp[i,1]==yvmax) or (mp[i,0]==xv and mp[i,1]==yvmin)):
        m[mp[i,0],mp[i,1]]=vmax


# In[54]:
'''
[px,py]=np.gradient(m)
X, Y = np.meshgrid(np.linspace(0,si-1,si), np.linspace(0,si-1,si))
#plt.figure(figsize=(12,12))
#plt.quiver(X,Y,-py,-px, width=0.003)
plt.contour(m,200)
#plt.colorbar()
plt.show()
plt.imshow(iaux)
'''

### Electrons

# Number of electrons 

# In[69]:

el=1


# In[64]:

steps=np.zeros(shape=(el,1))


# In[70]:

h=0
for q in xrange(1,el+1):
    for y in xrange(1,msize[0]-1):
        for x in xrange(1,msize[1]-1):
            if m[x,y]<m[x,y+1]:
                Vr[x,y] = 0 #Vr tells the potential diference between the poinx x,y and its right neighbour 
            else:
                Vr[x,y] = m[x,y]-m[x,y+1]         
            if m[x,y]<m[x,y-1]:
                Vl[x,y] = 0 #Vl tells the potential diference between the poinx x,y and its left neighbour 
            else: 
                Vl[x,y] = m[x,y]-m[x,y-1]
            if m[x,y]<m[x-1,y]:
                Vu[x,y] = 0 #Vu tells the potential diference between the poinx x,y and its upper neighbour 
            else:
                Vu[x,y] = m[x,y]-m[x-1,y]
            if m[x,y]<m[x+1,y]:
                Vd[x,y] = 0  #Vd tells the potential diference between the poinx x,y and its down neighbour 
            else:
                Vd[x,y] = m[x,y]-m[x+1,y]      
            pr[x,y]= Vr[x,y]/[Vr[x,y]+Vl[x,y]+Vu[x,y]+Vd[x,y]] #Defines the probabilitx of a right jump 
            pl[x,y]= Vl[x,y]/[Vr[x,y]+Vl[x,y]+Vu[x,y]+Vd[x,y]] #Defines the probabilitx of a left jump 
            pd[x,y]= Vd[x,y]/[Vr[x,y]+Vl[x,y]+Vu[x,y]+Vd[x,y]] #Defines the probabilitx of a down jump 
            pu[x,y]= Vu[x,y]/[Vr[x,y]+Vl[x,y]+Vu[x,y]+Vd[x,y]] #Defines the probabilitx of an upper jump 
    #Maximum steps allowed
    k=3*max(msize[1],msize[0])
    #The s matriy will "follow" the electron
    s=np.zeros(shape=(k,2)) 
    #Defines the initial position of the electron
    s[0,1]=yvmax 
    s[0,0]=xv 
    while x!= xv and y!= yvmin:
        y=yvmax
        x=xv
        p=0
        for i in xrange(0,k-1):
            z=random.random()
            if z <=pr[x,y]:              #Jump to the right
                s[i+1,0]=s[i,0]+1
                s[i+1,1]=s[i,1]
                p=p+1
                y=y+1
            elif pr[x,y]<z<=(pr[x,y]+pl[x,y]): #Jump to the left
                s[i+1,0]=s[i,0]-1
                s[i+1,1]=s[i,1]
                p=p+1
                y=y-1
            elif (pr[x,y]+pl[x,y])<z<=(pr[x,y]+pl[x,y]+pu[x,y]):   #Jump to the upper direction
                s[i+1,0]=s[i,0]
                s[i+1,1]=s[i,1]-1
                p=p+1
                x=x-1
            elif (pr[x,y]+pl[x,y]+pu[x,y])<z<=(pr[x,y]+pl[x,y]+pu[x,y]+pd[x,y]):   #Jump to the down direction
                s[i+1,0]=s[i,0]
                s[i+1,1]=s[i,1]+1
                x=x+1
                p=p+1
    steps[h,0]=p
    h=h+1


# In[67]:

results=[np.mean(steps),np.std(steps),np.var(steps)]


# In[68]:

print results


# In[ ]:



