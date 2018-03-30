# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 09:57:22 2018

@author: wangange
"""

"""
@code: 1051739153@qq.com
"""

#coding =UTF8

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
print(iris)
rf = RandomForestRegressor(100)
rf.fit(iris.data[:350], iris.target[:350])
instance = iris.data[100]
print(instance)
print("prediction score:" +str(iris.target[100]))
print("real score:" + str(rf.predict(np.array(instance).reshape(1,-1))))