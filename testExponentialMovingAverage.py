# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:41:26 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf

# 定义一个变量用于计算滑动平均，初始值为0
v1 = tf.Variable(0, dtype = tf.float32)
# 控制动态衰减率
step = tf.Variable(0, trainable=False)

# 定义一个滑动平均类
ema = tf.train.ExponentialMovingAverage(0.99, step)
# 更新滑动平均的操作。定义一个列表，执行该操作时列表更新
maintain_averages_op = ema.apply([v1])

with tf.Session() as sess:
    # 初始化所有变量
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    
    # 查看初始值，均为0
    print(sess.run([v1, ema.average(v1)]))  # 输出[0.0, 0.0]
    
    # 更新变量v1为5
    sess.run(tf.assign(v1, 5))
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))
    
    # 更新step为10000
    sess.run(tf.assign(step, 10000))
    # 再令v1的值为10
    sess.run(tf.assign(v1, 10))
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))
    # 此时输出应为[10.0, 4.5549998]
    
    # 再运行一下操作
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))
    # 再运行一下操作
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))