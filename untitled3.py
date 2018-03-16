# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:53:42 2018

@author: Administrator
"""

import tensorflow as tf

sess = tf.Session()
a = tf.constant([[1.0,2.0],[1.0, 2.0],[1.0, 2.0]])
print(sess.run(tf.sigmoid(a)))

a = tf.constant([-1.0, 2.0])
with tf.Session() as sess:
    b = tf.nn.relu(a)
    print(sess.run(b))