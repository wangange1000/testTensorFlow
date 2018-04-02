# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 08:57:38 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

SUMMARY_DIR = "D:\\testTensorFlow\\"
BATCH_SIZE = 100
TRAIN_STEPS = 3000
tf.reset_default_graph()

# 生成变量监控信息，必定义日志操作。下述var给定需要记录的张量，图表名称与变量名一致
def variable_summaries(var, name):
    # 将监控信息放到同一命名空间下
    with tf.name_scope('summaries'):
        # histogram函数记录张量中元素的取值分布，会生成一个Summary protocol buffer
        tf.summary.histogram(name, var)
        
        # 计算变量平均值，生成平均值日志操作
        # 注意命名空间方式
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean/' + name, mean)
        # 计算变量的标准差
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var-mean)))
        tf.summary.scalar('stddev/' + name, stddev)

# 生成一层全连接网络
def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
    # 同层神经网络放于同一名称空间下
    with tf.name_scope(layer_name):
        with tf.name_scope("weights"):
            weights = tf.Variable(tf.truncated_normal([input_dim, output_dim], stddev=0.1))
            variable_summaries(weights, layer_name + '/weights')
        with tf.name_scope("biases"):
            biases = tf.Variable(tf.constant(0.0, shape=[output_dim]))
            variable_summaries(biases, layer_name + '/biases')
        with tf.name_scope('Wx_plus_b'):
            preactivate = tf.matmul(input_tensor, weights) + biases
            # 记录激活函数之前的结果
            tf.summary.histogram(layer_name + '/pre_activations', preactivate)
        activations = act(preactivate, name='activation')
        # 经过激活函数之后的分布，此处使用ReLU函数
        tf.summary.histogram(layer_name + '/activations', activations)
        return activations
    
def main(_):
    mnist = input_data.read_data_sets("mnist_data", one_hot=True)
    # 定义输入
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 784], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, 10], name='y-input')
    # 还原像素矩阵， 将当前图片信息写入日志
    with tf.name_scope('input_reshape'):
        image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
        tf.summary.image('input', image_shaped_input, 10)
    
    # 只有一个隐含层
    hidden1 = nn_layer(x, 784, 500, 'layer1')
    y = nn_layer(hidden1, 500, 10, 'layer2', act=tf.identity)
    
    # 计算交叉熵并监控
    with tf.name_scope('cross_entropy'):
        cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_))
        tf.summary.scalar('cross_entropy', cross_entropy)
        
    with tf.name_scope('train'):
        train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
        
    # 计算模型在给定数据上的正确率，并记录日志
    with tf.name_scope('accuracy'):
        with tf.name_scope('correct_prediction'):
            correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        with tf.name_scope('accuracy'):
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('accuracy', accuracy)
    
    # 一一调用很麻烦，因此一次整理所有日志操作
    merged = tf.summary.merge_all()
    
    with tf.Session() as sess:
        # 初始化writer
        summary_writer = tf.summary.FileWriter(SUMMARY_DIR, sess.graph)
        tf.global_variables_initializer().run()
        
        for i in range(TRAIN_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            # 每运行一步训练，记录所有日志
            summary, _ = sess.run([merged, train_step], feed_dict={x:xs, y_:ys})
            # 所有日志写入文件，供tensorboard调用
            summary_writer.add_summary(summary, i)
            
    summary_writer.close()
    
if __name__=='__main__':
    tf.app.run()