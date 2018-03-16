# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:42:00 2018

@author: Administrator
"""

import numpy as np
b = 0
a = 0.5

x = np.array([[0,1,1],[0,1,0],[0,0,0],[0,0,1]])
d = np.array([1,1,0,1])
w = np.array([b,0,0])
def sgn(v):
    if v>0:
        return 1;
    else:
        return 0
    
def comy(myw, myx):
    return sgn(np.dot(myw.T, myx))

def neww(oldw, myd, myx, a):
    return oldw+a*(myd-comy(oldw, myx)) * myx

i=0
for xn in x:
    w=neww(w, d[i], xn, a)
    i+=1
    
for xn in x:
    print("%d or %d => %d" % (xn[1],xn[2],comy(w,xn)))

print(w)