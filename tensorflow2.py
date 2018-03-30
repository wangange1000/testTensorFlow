# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:48:32 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf

w1 = tf.Variable(tf.random_normal((2,3), stddev = 1, seed = 1))
w2 = tf.Variable(tf.random_normal((3,1), stddev = 1, seed = 1))

x = tf.constant([[0.7, 0.9]])

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()

sess.run(w1.initializer)
sess.run(w2.initializer)

print(sess.run(y))
print(y.eval(session=sess))
sess.close()