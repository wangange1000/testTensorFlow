# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:20:18 2018

@author: Administrator
"""
import tensorflow as tf

with tf.variable_scope("foo", reuse=True):
    x = 1.0 + tf.get_variable("v", [1])
with tf.variable_scope("foo1", reuse=True):
    v = tf.get_variable("v", [10])
    
    
with tf.variable_scope("foo", reuse=True):
    with tf.name_scope("bar"):
        v = tf.get_variable("v", [1])
        b = tf.Variable(tf.zeros([1]), name='b')
        x = 1.0 + v

print(x)
print(b)
print(v)