# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:09:01 2018

@author: Administrator
"""

"""
@code: 1051739153@qq.com
"""

import numpy as np
import math
b=1
a0=0.1
a=0.0
r=5.0

x=np.array([[1,1,6],[1,2,12],[1,3,9],[1,8,24]])
d=np.array([1,1,-1,-1])
w=np.array([b,0,0])
expect_e=0.005
maxtrycount=30
mycount=0

def sgn(v):
    if v>0:
        return 1
    else:
        return -1
    
def get_e(myw,myx,myd):
    return myd-get_v(myw,myx)

def get_v(myw,myx):
    return sgn(np.dot(myw.T,myx))

def neww(oldw,myd,myx,a):
    mye=get_e(oldw,myx,myd)
    a=a0/(1+float(mycount)/r)
    return (oldw+a*mye*myx, mye)

while True:
    mye=0
    i=0
    for xn in x:
        w,e=neww(w,d[i],xn,a)
        i+=1
        mye+=pow(e,2)
        print(mye)
    mye=math.sqrt(mye)
    mycount+=1
    print("第 %d 次调整后的权值为：" % mycount)
    print(w)
    print("误差：%f" % mye)
    if abs(mye)<expect_e or mycount>maxtrycount: break

