# -*- coding: utf-8 -*-1
"""
Created on Fri Feb  2 14:53:12 2018

@author: Administrator
"""

import tensorflow as tf

    
with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4),reuse=True):
    v = tf.get_variable("v", [1])

print(v)