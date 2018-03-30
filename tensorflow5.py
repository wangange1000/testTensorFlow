# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:57:29 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2,3], stddev=1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1))

x = tf.placeholder(tf.float32, shape=(3,2), name="input")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

y = tf.sigmoid(y)

# 定义损失函数
cross_entropy = -tf.reduce_mean( y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))+(1-y)*tf.log(tf.clip_by_value(1-y, 1e-10, 1.0)))
learning_rate = 0.001
# 使用方向传播算法
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)

# 注意此处的运行方式
# print(sess.run(y))
print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))

sess.close()