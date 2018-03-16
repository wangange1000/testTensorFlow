# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:27:58 2018

@author: Administrator
"""

import numpy as np

b = 1
a = 0.3
x = np.array([[1,1,3],[1,2,5],[1,1,8],[1,2,15],[1,3,7],[1,4,25]])
d = np.array([1,1,-1,-1,1,-1])
w = np.array([b,0,0])

def sgn(v):
    if v>=0:
        return 1
    else:
        return -1
    
def comy(myw, myx):
    return sgn(np.dot(myw.T, myx))

def neww(oldw, myd, myx, a):
    print(comy(oldw, myx))
    return oldw+a*(myd-comy(oldw,myx))*myx

i=0
for xn in x:
    print(xn)
    w = neww(w, d[i], xn, a)
    i+=1
    print(w)
    
for xn in x:
    print("%d %d => %d" % (xn[1], xn[2], comy(w,xn)))
    
test = np.array([b,9,19])
print("%d %d => %d" % (test[1], test[2], comy(w,test)))

test = np.array([b,9,64])
print("%d %d => %d" % (test[1], test[2], comy(w,test)))

