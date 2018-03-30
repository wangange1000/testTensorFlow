# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:52:20 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf

# 定义一个简单的计算图
input1 = tf.constant([1.0, 2.0, 3.0], name = "input1")
input2 = tf.Variable(tf.random_uniform([3]), name="input2")
output = tf.add_n([input1, input2], name="add")

# 生成writer，将当前数据图写入日志
writer = tf.summary.FileWriter("/path/to/log", tf.get_default_graph())
writer.close