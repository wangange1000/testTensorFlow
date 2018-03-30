# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:59:26 2018

@author: wangange
"""
"""
@code: 0151739153@qq.com
"""

import tensorflow as tf
from numpy.random import RandomState

batch_size = 8

x = tf.placeholder(tf.float32, shape=(None,2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None,1), name='y-input')

w1 = tf.Variable(tf.random_normal([2,1], stddev=1, seed=1))
y = tf.matmul(x, w1)

#定义损失函数
loss_less = 10
loss_more = 1
loss = tf.reduce_sum(tf.where(tf.greater(y,y_), (y-y_)*loss_more, (y_-y)*loss_less))
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 通过一个随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# 对目标数据加入随机噪音
Y = [[x1+x2 + rdm.rand()/10.0-0.05] for (x1,x2) in X]

# 开始训练
with tf.Session() as sess:
    init_opt = tf.global_variables_initializer()
    sess.run(init_opt)
    STEPS = 5000
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)
        sess.run(train_step, feed_dict={x:X[start:end], y_:Y[start:end]})
        print(sess.run(w1))