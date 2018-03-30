# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:39:54 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    V = tf.get_variable("v", initializer = tf.zeros_initializer()(shape=[1]))
    
g2 = tf.Graph()
with g2.as_default():
    V = tf.get_variable("v", initializer = tf.ones_initializer()(shape=[1]))
    
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse = True):
        print(sess.run(tf.get_variable("v")))
        
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse = True):
        print(sess.run(tf.get_variable("v")))