# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 10:03:02 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf
from numpy.random import RandomState

def get_weight(shape, _lambda):
    # 生成一个变量
    var = tf.Variable(tf.random_normal(shape), dtype = tf.float32)
    # 将这个新变量L2正则化后加入集合
    tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(_lambda)(var))
    # 返回生成的变量
    return var

tf.reset_default_graph()
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')
batch_size = 8

layer_dimension = [2,10,10,10,1]
n_layers = len(layer_dimension)

# 这个变量维护前向传播时最深层的节点，开始的时候就是输入层
cur_layer = x
# 当前层的节点个数
in_dimension = layer_dimension[0]

# 通过一个循环来生成5层全连接的神经网络结构
for i in range(1, n_layers):
    # 下一层节点个数
    out_dimension = layer_dimension[i]
    # 生成当前层中权重的变量
    weight = get_weight([in_dimension, out_dimension], 0.001)
    bias = tf.Variable(tf.constant(0.1, shape=[out_dimension]))
    # 定义激活函数
    cur_layer = tf.nn.relu(tf.matmul(cur_layer, weight) + bias)
    in_dimension = layer_dimension[i]

# 最后一层输出用于计算均方误差
mes_loss = tf.reduce_mean(tf.square(y_ - cur_layer))

# 将均方误差损失函数加入损失集合
tf.add_to_collection('losses', mes_loss)

# 将集合中的损失函数全部加起来就是总的损失函数
loss = tf.add_n(tf.get_collection('losses'))

train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 初始化参数
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[x1 + x2 + rdm.rand()/10.0-0.05] for (x1, x2) in X]
print(tf.get_default_graph())

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    
    Steps = 5000
    # 迭代更新
    for i in range(Steps):
        start = (i*batch_size) % dataset_size
        end = min(start+batch_size, dataset_size)
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
    
    print(tf.trainable_variables())
    for var in tf.trainable_variables():  
        print(var.eval())  