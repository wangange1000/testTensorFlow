# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:53:11 2018

@author: Administrator
"""
"""
@code: 1051739153@qq.com
"""

import random

def RandomSampling(dataMat, number):
    try:
        slice = random.sample(dataMat, number)
        return slice
    except:
        print("sample larger than population")
        
def RepetitionRandomSampling(dataMat, number):
    sample=[]
    for i in range(number):
        sample.append(dataMat[random.randint(0, len(dataMat)-1)])
    return

def SystematicSampling(dataMat, number):
    length=len(dataMat)
    k=length/number
    sample=[]
    i=0
    if k>0:
        while len(sample)!=number:
            sample.append(dataMat[0+i*k])
            i+=1
        return sample
    else:
        return RandomSampling(dataMat, number)
    
def StratifiedSampling(dataMat1, dataMat2, dataMat3, number):
    sample=[]
    num=number/3
    sample.append(RandomSampling(dataMat1, num))
    sample.append(RandomSampling(dataMat2, num))
    sample.append(RandomSampling(dataMat3, num))
    return sample

def width(lst):
    i=0
    for j in lst[0]:
        i+=1
    return i

def AutoNorm(mat):
    n=len(mat)
    m=width(mat)
    MinNum=[9999999999]*m
    MaxNum=[0]*m
    for i in mat:
        for j in range(0,m):
            if i[j]>MaxNum[j]:
                MaxNum[j]=i[j]
    for p in mat:
        for q in range(0,m):
            if p[q]<=MinNum[q]:
                MinNum[q]=p[q]
    
    section=list(map(lambda x:x[0]-x[1], zip(MaxNum, MinNum)))
    print(section)
    NormMat=[]
    
    for k in mat:
        distance=list(map(lambda x:x[0]-x[1], zip(k,MinNum)))
        value=list(map(lambda x:x[0]/x[1], zip(distance, section)))
        NormMat.append(value)
    return NormMat

def GetAverage(mat):
    n=len(mat)
    m=width(mat)
    num=[0]*m;
    for j in range(0,m):
        for i in mat:
            num[j]=num[j]+i[j]
        num[j]=num[j]/n
    return num

def GetVar(average, mat):
    ListMat=[]
    for i in mat:
        ListMat.append(list(map(lambda x:x[0]-x[1], zip(average, i))))
    
    n=len(ListMat)
    m=width(ListMat)
    num=[0]*m
    for j in range(0,m):
        for i in ListMat:
            num[j]=num[j]+(i[j]*i[j])
        num[j]=num[j]/n
    return num

def DenoisMat(mat):
    average=GetAverage(mat)
    variance=GetVar(average,mat)
    section=list(map(lambda x:x[0]+x[1], zip(average, variance)))
    
    n=len(mat)
    m=width(mat)
    num=[0]*m
    denoisMat=[]
    for i in mat:
        for j in range(0, m):
            if i[j]>section[j]:
                i[j]=section[j]
        denoisMat.append(i)
    return denoisMat
